import cv2
import os
import numpy as np


def renameData():
    filepath = './FaceData/photos/'

    fileList = os.listdir(filepath)
    for file in fileList:
        n = 0
        newPath = './FaceData/photos/' + file
        photos = os.listdir(newPath)

        for i in photos:
            print(i)
            oldname = newPath + os.sep + i
            newname = newPath + os.sep + str(n + 1) + '.jpg'
            os.rename(oldname, newname)
            print(oldname, '=>', newname)
            n += 1

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




def img_resize(image):
    height, width = image.shape[0], image.shape[1]
    width_new = 96
    height_new = 96
    if width / height >= width_new / height_new:
        img_new = cv2.resize(image, (width_new, int(height * width_new / width)))
    else:
        img_new = cv2.resize(image, (int(width * height_new / height), height_new))
    return img_new




def getFace(name):
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
            cv2.imwrite("Facedata/User/" + str(count) + '.jpg', gray[y: y + h, x: x + w])
            #cv2.imshow('image', img)
        k = cv2.waitKey(1)
        if k == 27:
            break
        elif count >= 10:
            break
    cv2.destroyAllWindows()

if __name__ == '__main__':

    #getFace()
    #renameData
    preprocessing()