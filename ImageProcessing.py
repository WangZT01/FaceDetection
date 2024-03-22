import numpy as np
import cv2
import os
import tkinter as tk
import tkinter.filedialog
from PIL import Image, ImageTk

IMAGE_SIZE = (112, 92)

'''
resize image to given size
'''
def img_resize(image):
    height, width = image.shape[0], image.shape[1]

    width_new = 112
    height_new = 92

    if width / height >= width_new / height_new:
        img_new = cv2.resize(image, (width_new, int(height * width_new / width)))
    else:
        img_new = cv2.resize(image, (int(width * height_new / height), height_new))
    return img_new

def createDatabase(path):

    datebase = dict()
    data_names = os.listdir(path)
    # 计算有几个文件（图片命名都是以 序号.jpg方式）减去Thumbs.db
    T = []
    data_names.remove('.DS_Store')
    for name in data_names:
        # 把所有图片转为1-D并存入T中
        photosPath = path + name
        photos = os.listdir(photosPath)
        for photo in photos:

            if photo.endswith('.pgm'):
                continue
            #print(photo)
            image = cv2.imread(photosPath + '/' + photo, cv2.IMREAD_GRAYSCALE)
            #image = cv2.resize(image, IMAGE_SIZE)
            # 转为1-D
            image = image.reshape(image.size, 1)
            #print(image.shape)
            T.append(image)
            datebase[(len(T) - 1)] = name
            '''
            if name in datebase:
                datebase[name].append(len(T) - 1)
            else:
                datebase[name] = [len(T) - 1]
            '''
    T = np.array(T)
        # 不能直接T.reshape(T.shape[1],T.shape[0]) 这样会打乱顺序，
    T = T.reshape(T.shape[0], T.shape[1])
    return datebase, np.mat(T).T

def eigenfaceCore(T):
    # 把均值变为0 axis = 1代表对各行求均值
    m = T.mean(axis=1)
    A = T - m
    L = (A.T) * (A)
    #     L = np.cov(A,rowvar = 0)
    # 计算AT *A的 特征向量和特征值V是特征值，D是特征向量
    V, D = np.linalg.eig(L)
    L_eig = []
    for i in range(A.shape[1]):
        #         if V[i] >1:
        L_eig.append(D[:, i])
    L_eig = np.mat(np.reshape(np.array(L_eig), (-1, len(L_eig))))
    # 计算 A *AT的特征向量
    eigenface = A * L_eig
    return eigenface, m, A

def recognize(database, testImage, eigenface, m, A):
    _, trainNumber = np.shape(eigenface)
    # 投影到特征脸后的
    projectedImage = eigenface.T * (A)
    # 可解决中文路径不能打开问题
    testImageArray = cv2.imdecode(np.fromfile(testImage, dtype=np.uint8), cv2.IMREAD_GRAYSCALE)
    # 转为1-D
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
    #cv2.imshow("recognize result", cv2.imread('./TrainDatabase' + '/' + str(index + 1) + '.jpg', cv2.IMREAD_GRAYSCALE))
    #cv2.waitKey()
    print("The result is: ", database[index])
    return index + 1


# 进行人脸识别主程序
def example(filename):
    database, T = createDatabase('./ORL/')
    #print(database)
    eigenface, m, A = eigenfaceCore(T)
    testimage = filename
    print(testimage)
    print(recognize(database, testimage, eigenface, m, A))


# 构建可视化界面
def gui():
    root = tk.Tk()
    root.title("pca face")

    # 点击选择图片时调用
    def select():
        filename = tkinter.filedialog.askopenfilename()
        if filename != '':
            s = filename  # jpg图片文件名 和 路径。
            im = Image.open(s)
            tkimg = ImageTk.PhotoImage(im)  # 执行此函数之前， Tk() 必须已经实例化。
            l.config(image=tkimg)
            btn1.config(command=lambda: example(filename))
            btn1.config(text="开始识别")
            btn1.pack()
            # 重新绘制
            root.mainloop()

    # 显示图片的位置
    l = tk.Label(root)
    l.pack()

    btn = tk.Button(root, text="选择识别的图片", command=select)
    btn.pack()

    btn1 = tk.Button(root)  # 开始识别按钮，刚开始不显示
    root.mainloop()


if __name__ == "__main__":
    #
    gui()
    #createDatabase('./ORL/')
    #database, metrix = createDatabase('./ORL/')
    #print(database)