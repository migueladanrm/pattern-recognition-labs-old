import tkinter as tk
import tkinter.font as tkf
# from tkinter import *
from tkinter.filedialog import askopenfilename
from PIL import ImageTk, Image


def create_ui(file):
    window = tk.Tk()
    window.title("Ejercicios - Semana 4")

    tk.Label(window, text="3.1: Balance de color", font=tkf.Font(size=30)).pack(padx=120, pady=10)

    img = ImageTk.PhotoImage(Image.open(file))
    panel = tk.Label(window, image=img)
    panel.image = img
    panel.pack()

    slider = tk.Scale(window, from_=0, to=100, orient=tk.HORIZONTAL)
    slider.pack()

