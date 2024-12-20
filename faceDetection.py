import cv2
import os


def mkdir(path):
    folder = os.path.exists(path)

    if not folder:
        os.makedirs(path)
        print("---  new folder...  ---")
        print("---  OK  ---")






def preprocessing():
    filepath = './FaceData/photos/'
    fileList = os.listdir(filepath)

    faceDetector = cv2.CascadeClassifier('haarcascade_frontalface_alt2.xml')
    count = 0

    for file in fileList:
        newPath = './FaceData/photos/' + file
        photos = os.listdir(newPath)
        count = 1
        for i in photos:

            photo = newPath + os.sep + i
            img = cv2.imread(photo)
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            gray = cv2.equalizeHist(gray)

            faces = faceDetector.detectMultiScale(gray, 1.3, 5)
            for (x, y, w, h) in faces:
                cv2.rectangle(img, (x, y), (x + w, y + w), (255, 0, 0))
                count += 1
                cv2.imwrite(newPath + os.sep + 'gray_' + str(count) + '.jpg', gray[y: y + h, x: x + w])




def getFaceData(name):
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
            mkdir("./ORL/" + name)
            cv2.imwrite("./ORL/" + name + os.sep + str(count) + '.jpg', gray[y: y + h, x: x + w])
            cv2.imshow('image', img)
            print("recording face " + str(count))


        k = cv2.waitKey(1)
        if k == 27:
            break
        elif count >= 10:
            break
    camera.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':

    #getFace("peter")
    preprocessing()