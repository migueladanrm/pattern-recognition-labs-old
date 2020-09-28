import tkinter as tk
import tkinter.font as tkf
from tkinter.filedialog import askopenfilename
from PIL import ImageTk, Image
import numpy as np

import cv2

window = None
image = None
image = None
image2 = None
preW = None


def close():
    global window
    preW.deiconify()
    window.destroy()


def show(preWindow):
    global window, preW
    preW = preWindow
    window = tk.Tk()
    window.title("Blue Screen Matting")
    window.protocol("WM_DELETE_WINDOW", close)

    tk.Label(window, text="Ejercicio 3.3: Blue Screen Matting", font=tkf.Font(size=30)).pack(padx=120, pady=10)

    tk.Button(window, text="Selecciona el archivo de fondo", font=tkf.Font(size=20), command=askForFile).pack(padx=120,
                                                                                                              pady=10)

    tk.Button(window, text="Selecciona el archivo con el objeto", font=tkf.Font(size=20), command=askForFile2).pack(
        padx=120, pady=10)

    tk.Button(window, text="Realizar filtro de fondo", font=tkf.Font(size=20), command=do).pack(padx=120, pady=10)

    window.mainloop()


def askForFile():
    global window, image
    filename = askopenfilename(filetypes=[("image", "*.jpg *.png *.tif")])
    #filename = "C:/Users/Walter Benavides/Pictures/background.png"
    print(filename)
    imgCv2 = cv2.imread(filename)
    # cv2.imshow("IMAGE", imgCv2)
    imgTK = ImageTk.PhotoImage(Image.fromarray(imgCv2))

    image = imgCv2


def askForFile2():
    global window, image2
    filename = askopenfilename(filetypes=[("image", "*.jpg *.png *.tif")])
    #filename = "C:/Users/Walter Benavides/Pictures/objeto.png"
    print(filename)
    imgCv2 = cv2.imread(filename)
    # cv2.imshow("IMAGE", imgCv2)
    imgTK = ImageTk.PhotoImage(Image.fromarray(imgCv2))

    image2 = imgCv2


def do():
    global image, image2
    # cv2.imshow("Fondo restado", image)
    # cv2.imshow("Fondo restado2", image2)
    # cv2.imshow("Compare", cv2.compare(image, image2, cv2.CMP_GT))

    img1 = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    img2 = cv2.cvtColor(image2, cv2.COLOR_RGB2BGR)

    # Load in grayscale mode
    img_gray_mode = cv2.imread("C:/Users/Walter Benavides/Pictures/background.png", 0)

    # diff = img_gray_mode - img_gray

    diff = cv2.bitwise_xor(img1, img2)

    # cv2.imshow('Bitwise_xor', diff)
    # cv2.imshow('diff2', cv2.bitwise_or(img1, img2))
    # cv2.imshow('diff3', cv2.bitwise_not(img1, img2))
    # cv2.imshow('diff4', cv2.bitwise_and(img1, img2))

    suma5 = lambda t: t + 5
    resta5 = lambda t: t - 5

    lower_gray = np.array([resta5(i) for i in np.min(image, axis=(0, 1))])
    upper_gray = np.array([suma5(i) for i in np.max(image, axis=(0, 1))])

    mask = cv2.inRange(image2, lower_gray, upper_gray)

    cv2.imshow("Mask", mask)

    image2_masked = np.copy(image2)

    image2_masked = cv2.cvtColor(image2_masked, cv2.COLOR_RGB2RGBA)

    image2_masked[mask != 0] = [0, 0, 0, 0]

    cv2.imshow("Original/Imagen sin fondo", np.hstack((cv2.cvtColor(image2, cv2.COLOR_RGB2RGBA), image2_masked)))

    #graymode = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

    #print(rgba)
    def getA(gray):
        return gray / 255

    #func = np.vectorize(getA)

    #alpha = func(graymode)

    #print(alpha)

    # def one_alpha(value):
    # return (1 - alpha) * value

    # cv2.imshow("Fondo restado", image * (1 - alpha) + image2 * alpha)
