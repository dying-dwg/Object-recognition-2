import cv2 as cv
import time
import numpy as np
from matplotlib import pyplot as plt
import os

# Поворачиваю изображение на угол fi и масштабирую его по коэф. K
# + сразу получаю повёрнутое изображение в полярно-логарифмической системе координат
def RotatePolarImage(mainIM, center, K, fi, w, h):

    matrix = cv.getRotationMatrix2D(center, fi, K)
    rotated = cv.warpAffine(mainIM, matrix, (w, h))
    cv.imwrite("Result\\RotateIm.jpg", rotated)
    ConvPol = ConvertPolar(rotated, center, "PolarRotate")
    return ConvPol

# Конвертирует из декартовой СК в полярно-логарифмическую СК
def ConvertPolar(mainIM, center, name):
    # билинейная интерполяция +
    # перевод в полулогарифмическое полярные координаты
    flag = cv.INTER_LINEAR + cv.WARP_POLAR_LOG
    polar = cv.logPolar(mainIM, center, 107, flag)
    rot_polar = np.rot90(polar)
    cv.imwrite("Result\\" + str(name) + ".jpg", rot_polar)

    return rot_polar


def CorrImage(w, h, polar, copyIM):

    BrigIm = np.zeros((2*h, 2*w), dtype='uint8')

    for i, line in enumerate(polar):
        for j, pixel in enumerate(line):
            BrigIm[i][j] = pixel #left
            BrigIm[i][j + w] = pixel #right

    result = cv.matchTemplate(BrigIm, copyIM, cv.TM_CCOEFF_NORMED)

    # + приведение к общей яркости
    minVal, maxVal, minLoc, maxLoc = cv.minMaxLoc(result)

    w, h = copyIM.shape[::-1] # Вернуть форму массива
    rasmer = (maxLoc[0] + w, maxLoc[1] + h)

    print("Вверхний левый край:", rasmer)
    print("Нижний правый край:", maxLoc)
    print("=====")

    # Draw a rectangle of black color of thickness 5 px
    draw = cv.rectangle(BrigIm, maxLoc, rasmer, 255, 5)

    plt.figure()
    plt.imshow(result)
    plt.colorbar()
    plt.savefig('Result\\plot.jpg', bbox_inches='tight')

    plt.figure()
    plt.imshow(result, clim=(-0.5, 0.0))
    plt.colorbar()
    plt.savefig('Result\\plot1.jpg', bbox_inches='tight')

    cv.namedWindow('Find', cv.WINDOW_KEEPRATIO)
    cv.imshow('Find', draw)
    cv.resizeWindow('Find', 800, 800)
    cv.waitKey(0)
    cv.destroyAllWindows()

def ShowImage():
    pictures = os.listdir('Result')
    pic_box = plt.figure(figsize=(16, 4))
    # Поочередно считываем в переменную picture имя изображения из списка pictures. В переменную i записываем номер итерации
    for i, picture in enumerate(pictures):
        # считываем изображение в picture
        picture = cv.imread('Result/' + picture)
        # добавляем ячейку в pix_box для вывода текущего изображения
        pic_box.add_subplot(1, 5, i + 1)
        plt.imshow(picture)
        # отключаем отображение осей
        plt.axis('off')
    # выводим все созданные фигуры на экран

    plt.show()

if __name__ == '__main__':
    start_time = time.time()
    mainIM = cv.imread("main.jpg", cv.IMREAD_GRAYSCALE)

    w, h = mainIM.shape[::-1]
    Rw = w / 2
    Rh = h / 2
    center = (Rw, Rh)

    # Коэффицент мастштабирования K= 1 + 0.05 × N
    K = 1 + 0.05 * 2
    # Вращение ϕ = (+3 × N)°
    fi = 3 * 2

    polar = ConvertPolar(mainIM, center, "PolarMain")
    copyIM = RotatePolarImage(mainIM, center, K, fi, w, h)


    CorrImage(w, h, polar, copyIM)
    ShowImage()