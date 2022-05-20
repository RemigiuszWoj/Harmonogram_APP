# from tkinter import *
import tkinter

#Okinko
window =tkinter.Tk()
window.title("Metoda pełazajacej magisterki")

#ramka f-cji
ramka_funkcji = tkinter.LabelFrame(window, text="Funkcja")
ramka_funkcji.grid(row=0, column=1, columnspan=8, sticky='W', padx=5, pady=5, ipadx=5, ipady=5)

tkinter.Label (ramka_funkcji, text="Podaj funkcje").grid(row=1,column=0,sticky='W')

pole_fcji = tkinter.Entry(ramka_funkcji, width = 51)
pole_fcji.grid(row=1, column=3, columnspan=8, sticky="WE", pady=5, padx = 5)


window.mainloop()

