import cv2
import os
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