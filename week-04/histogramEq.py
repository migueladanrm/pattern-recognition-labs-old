import tkinter as tk
import tkinter.font as tkf
from tkinter.filedialog import askopenfilename

import cv2
from PIL import ImageTk
from PIL import Image
import numpy as np

window = None
preW = None
image = None


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

    tk.Button(window, text="Selecciona la imagen a cargar", font=tkf.Font(size=20), command=askForFile).pack(padx=120,
                                                                                                             pady=10)

    tk.Button(window, text="Realizar ecualización del histograma", font=tkf.Font(size=20), command=do).pack(padx=120,
                                                                                                            pady=10)

    window.mainloop()


def askForFile():
    global window, image
    filename = askopenfilename(filetypes=[("image", "*.jpg *.png *.tif")])

    imgCv2 = cv2.imread(filename)

    #imgTK = ImageTk.PhotoImage(Image.fromarray(imgCv2))

    image = imgCv2


def do():
    global image

    R, G, B = cv2.split(image)

    output1_R = cv2.equalizeHist(R)
    output1_G = cv2.equalizeHist(G)
    output1_B = cv2.equalizeHist(B)

    equ = cv2.merge((output1_R, output1_G, output1_B))

    result = np.hstack((image, equ))

    cv2.imshow("Original/Ecualizada", result)
