# coding:utf-8
import os
from numpy import *
import numpy as np
import cv2
import matplotlib.pyplot as plt
from pylab import mpl


def img2vector(image):
    """
    Convert an image file to a 1D vector.
    Args:
        image (str): Path to the image file.
    Returns:
        numpy.ndarray: The image as a 1D vector.
    """
    img = cv2.imread(image, 0)
    rows, cols = img.shape
    imgVector = np.zeros((1, rows * cols))
    imgVector = np.reshape(img, (1, rows * cols))
    return imgVector


orlpath = "./ORL"


def load_orl(k):
    """
    Load the ORL face dataset and split into training and testing sets.
    Args:
        k (int): Number of training images per person (1-9).
    Returns:
        tuple: (train_face, train_label, test_face, test_label)
    """
    train_face = np.zeros((40 * k, 112 * 92))
    train_label = np.zeros(40 * k)
    test_face = np.zeros((40 * (10 - k), 112 * 92))
    test_label = np.zeros(40 * (10 - k))

    sample = random.permutation(10) + 1
    for i in range(40):
        people_num = i + 1
        for j in range(10):
            image = './ORL' + '/s' + str(people_num) + '/' + str(sample[j]) + '.jpg'

            img = cv2.imread(image, 0)
            rows, cols = img.shape
            imgVector = np.zeros((1, rows * cols))
            imgVector = np.reshape(img, (1, rows * cols))
            img = imgVector

            if j < k:

                train_face[i * k + j, :] = img
                train_label[i * k + j] = people_num
            else:

                test_face[i * (10 - k) + (j - k), :] = img
                test_label[i * (10 - k) + (j - k)] = people_num

    return train_face, train_label, test_face, test_label


def PCA(data, r):
    """
    Perform Principal Component Analysis (PCA) on the data.
    Args:
        data (numpy.ndarray): The data matrix.
        r (int): Number of principal components to retain.
    Returns:
        tuple: (final_data, data_mean, V_r)
    """
    data = np.float32(np.mat(data))
    rows, cols = np.shape(data)
    data_mean = np.mean(data, 0)
    A = data - np.tile(data_mean, (rows, 1))
    C = A * A.T
    D, V = np.linalg.eig(C)
    V_r = V[:, 0:r]
    V_r = A.T * V_r
    for i in range(r):
        V_r[:, i] = V_r[:, i] / np.linalg.norm(V_r[:, i])  # Feature vector normalization

    final_data = A * V_r
    return final_data, data_mean, V_r


def face_rec():
    """
    Perform face recognition on the ORL dataset using PCA and plot the accuracy for different k values.
    """
    r = 30
    print("10d %d" % (r))
    x_value = []
    y_value = []
    for k in range(1, 10):
        train_face, train_label, test_face, test_label = load_orl(k)

        data_train_new, data_mean, V_r = PCA(train_face, r)
        num_train = data_train_new.shape[0]
        num_test = test_face.shape[0]
        temp_face = test_face - np.tile(data_mean, (num_test, 1))
        data_test_new = temp_face * V_r
        data_test_new = np.array(data_test_new)
        data_train_new = np.array(data_train_new)

        true_num = 0
        for i in range(num_test):
            testFace = data_test_new[i, :]
            diffMat = data_train_new - np.tile(testFace, (num_train, 1))
            sqDiffMat = diffMat ** 2
            sqDistances = sqDiffMat.sum(axis=1)
            sortedDistIndicies = sqDistances.argsort()
            indexMin = sortedDistIndicies[0]
            if train_label[indexMin] == test_label[i]:
                true_num += 1
            else:
                pass

        accuracy = float(true_num) / num_test
        x_value.append(k)
        y_value.append(round(accuracy, 2))

        print('%d photos from each persons，The classify accuracy is: %.2f%%' % (k, accuracy * 100))

    if r == 30:
        y3_value = y_value
        plt.plot(x_value, y3_value, marker="o", markerfacecolor="red")
        for a, b in zip(x_value, y_value):
            plt.text(a, b, (a, b), ha='center', va='bottom', fontsize=10)

        plt.title("30d accuracy", fontsize=14)
        plt.xlabel("K means: ", fontsize=14)
        plt.ylabel("accuracy", fontsize=14)
        plt.show()

    L3, = plt.plot(x_value, y3_value, marker="o", markerfacecolor="red")

    plt.legend([L3], ["30"], loc=1)
    plt.title("compare each d", fontsize=14)
    plt.xlabel("K means", fontsize=14)
    plt.ylabel("accuracy", fontsize=14)
    plt.show()


if __name__ == '__main__':
    face_rec()
