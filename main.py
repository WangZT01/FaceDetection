import numpy as np
import cv2
import os
import tkinter as tk
import tkinter.filedialog
from PIL import Image, ImageTk
from faceDetection import getFaceData

IMAGE_SIZE = (112, 92)

'''
resize image to given size
'''


def img_resize(image):
    """
    Resize the input image to 112x92 while maintaining aspect ratio.
    Args:
        image (numpy.ndarray): The input image.
    Returns:
        numpy.ndarray: The resized image.
    """
    height, width = image.shape[0], image.shape[1]

    width_new = 112
    height_new = 92
    if height == height_new and width == width_new:
        return image
    if width / height >= width_new / height_new:
        img_new = cv2.resize(image, (width_new, int(height * width_new / width)))
    else:
        img_new = cv2.resize(image, (int(width * height_new / height), height_new))
    return img_new


def createDatabase(path):
    """
    Create a face image database from the given directory.
    Args:
        path (str): Path to the directory containing face images.
    Returns:
        tuple: (database dictionary, image matrix)
    """
    datebase = dict()
    data_names = os.listdir(path)

    T = []
    if '.DS_Store' in data_names:
        data_names.remove('.DS_Store')
    for name in data_names:

        photosPath = path + name
        photos = os.listdir(photosPath)
        for photo in photos:

            if photo.endswith('.pgm'):
                continue
            # print(photo)
            image = cv2.imread(photosPath + '/' + photo, cv2.IMREAD_GRAYSCALE)
            image = cv2.resize(image, IMAGE_SIZE)

            image = image.reshape(image.size, 1)
            # print(image.shape)
            T.append(image)
            datebase[(len(T) - 1)] = name
            '''
            if name in datebase:
                datebase[name].append(len(T) - 1)
            else:
                datebase[name] = [len(T) - 1]
            '''
    T = np.array(T)

    T = T.reshape(T.shape[0], T.shape[1])
    return datebase, np.mat(T).T


def eigenfaceCore(T):
    """
    Compute the eigenfaces from the training image matrix.
    Args:
        T (numpy.matrix): Matrix of training images.
    Returns:
        tuple: (eigenfaces, mean image, difference matrix)
    """
    m = T.mean(axis=1)
    A = T - m
    L = (A.T) * (A)

    V, D = np.linalg.eig(L)
    L_eig = []
    for i in range(A.shape[1]):
        #         if V[i] >1:
        L_eig.append(D[:, i])
    L_eig = np.mat(np.reshape(np.array(L_eig), (-1, len(L_eig))))

    eigenface = A * L_eig
    return eigenface, m, A


def recognize(database, testImage, eigenface, m, A):
    """
    Recognize the person in the test image using the eigenface method.
    Args:
        database (dict): Mapping from index to person name.
        testImage (str): Path to the test image file.
        eigenface (numpy.matrix): Matrix of eigenfaces.
        m (numpy.matrix): Mean image.
        A (numpy.matrix): Difference matrix.
    Returns:
        str: The recognized person's name.
    """
    _, trainNumber = np.shape(eigenface)

    projectedImage = eigenface.T * (A)

    testImageArray = cv2.imdecode(np.fromfile(testImage, dtype=np.uint8), cv2.IMREAD_GRAYSCALE)

    testImageArray = cv2.resize(testImageArray, IMAGE_SIZE)
    testImageArray = testImageArray.reshape(testImageArray.size, 1)
    testImageArray = np.mat(np.array(testImageArray))
    differenceTestImage = testImageArray - m
    projectedTestImage = eigenface.T * (differenceTestImage)
    distance = []
    for i in range(0, trainNumber):
        q = projectedImage[:, i]

        temp = np.linalg.norm(projectedTestImage - q)
        distance.append(temp)

    minDistance = min(distance)
    index = distance.index(minDistance)
    print("The result is: ", database[index])
    return database[index]


def example(filename):
    """
    Example function to recognize a face from a given image file.
    Args:
        filename (str): Path to the test image file.
    Returns:
        str: The recognized person's name.
    """
    database, T = createDatabase('./ORL/')
    eigenface, m, A = eigenfaceCore(T)
    testimage = filename
    # print(testimage)
    return (recognize(database, testimage, eigenface, m, A))


def gui():
    """
    Launch the GUI for face detection and recognition.
    """
    root = tk.Tk()
    root.title("pca face")
    root.geometry("500x500")

    def faceImport():
        """
        Import face data from webcam for the entered username.
        """
        if usernameLabel.get() == '':
            tkinter.messagebox.showinfo(title='Hi', message='please input your username')
        else:
            getFaceData(usernameLabel.get())
        root.mainloop()

    def result(name):
        """
        Show a message box with the recognized name.
        Args:
            name (str): The recognized person's name.
        """
        tkinter.messagebox.showinfo(title='Hi', message='Hi! ' + str(name))

    def detection():
        """
        Perform face detection and recognition, and display the result in the GUI.
        """
        filename = getFaceDataforRecognition()
        if filename != '':
            s = filename
            im = Image.open(s)
            tkimg = ImageTk.PhotoImage(im)
            l.config(image=tkimg)
            name = example(filename)
            result(name)

            root.mainloop()

    l = tk.Label(root)
    l.pack()

    btn = tk.Button(root, text="face detection", command=detection)
    btn.pack()

    l = tk.Label(root, text='Please input your name here: ', font=('Arial', 12), width=30, height=2)
    l.pack()
    usernameLabel = tk.Entry(root, show=None, font=('Arial', 14))
    usernameLabel.pack()

    btn_Data = tk.Button(root, text="face import", command=faceImport)
    btn_Data.pack()
    root.mainloop()


def getFaceDataforRecognition():
    """
    Capture a single face image from the webcam and save it to './testData/'.
    Returns:
        str: The file path of the saved face image.
    """
    camera = cv2.VideoCapture(0)

    faceDetector = cv2.CascadeClassifier('haarcascade_frontalface_alt2.xml')

    count = 0
    while True:
        success, img = camera.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        gray = cv2.equalizeHist(gray)
        faces = faceDetector.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + w), (255, 0, 0))
            count += 1
            cv2.imwrite("./testData/" + os.sep + str(count) + '.jpg', gray[y: y + h, x: x + w])
            cv2.imshow('image', img)
            print("recording face " + str(count))
        k = cv2.waitKey(1)
        if k == 27:
            break
        elif count >= 1:
            break
    camera.release()
    cv2.destroyAllWindows()
    return "./testData/" + os.sep + str(1) + '.jpg'


if __name__ == "__main__":
    #
    gui()
    # createDatabase('./ORL/')
    # database, metrix = createDatabase('./ORL/')
    # print(database)
