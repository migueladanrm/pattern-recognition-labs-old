import tkinter as tk

import tkinter.font as tkf

import blueScreenMatting
import histogramEq

window = tk.Tk()

def getButton(window, text, action):
    return tk.Button(window, text=text, font=tkf.Font(size=20), command=action)

def hide():
    global window
    window.withdraw()

def show():
    global window
    window.deiconify()

def show31():
    ## Esto lo hacemos en archivos separados para cada ejercicio
    window = tk.Tk()
    window.title("Ejercicios - Semana 4")

    tk.Label(window, text="Ejercicio 3.1: Color", font=tkf.Font(size=30)).pack(padx=120, pady=10)

def show33():
    hide()
    ## Esto lo hacemos en archivos separados para cada ejercicio
    blueScreenMatting.show(window)


def show35():
    ## Esto lo hacemos en archivos separados para cada ejercicio
    window = tk.Tk()
    window.title("Semana 4")

    tk.Label(window, text="Ejercicio 3.5: Efectos", font=tkf.Font(size=30)).pack(padx=120, pady=10)

def show36():
    ## Esto lo hacemos en archivos separados para cada ejercicio
    hide()
    histogramEq.show(window)

def show318():
    ## Esto lo hacemos en archivos separados para cada ejercicio
    window = tk.Tk()
    window.title("Semana 4")

    tk.Label(window, text="Ejercicio 3.18: Rescalado con alta definición", font=tkf.Font(size=30)).pack(padx=120, pady=10)

def show329():
    ## Esto lo hacemos en archivos separados para cada ejercicio
    window = tk.Tk()
    window.title("Semana 4")

    tk.Label(window, text="Ejercicio 3.29: Arcoíris", font=tkf.Font(size=30)).pack(padx=120, pady=10)


def showMainMenu():
    global window
    window.title("Semana 4")

    tk.Label(window, text="Ejercicios Semana 4", font=tkf.Font(size=25)).pack(padx=120, pady=10)

    options = [
        {"name": "3.1", "action": show31},
        {"name": "3.3", "action": show33},
        {"name": "3.5", "action": show35},
        {"name": "3.6", "action": show36},
        {"name": "3.18", "action": show318},
        {"name": "3.29 (Reto)", "action": show329}
    ]

    for option in options:
        getButton(window, option.get("name"), option.get("action")).pack(padx=60, pady=20, ipadx=40, ipady=10)

    window.mainloop()


if __name__ == '__main__':
    showMainMenu()
