from tkinter import*
from tkinter import ttk 
import tkinter as tk 
import os
import pygame

Fenetre=Tk()
Fenetre.title("Saucisse")
Fenetre.geometry('673x534')

def traiter():
    mes1=ISBN.get()
    print(mes1)

ISBN = tk.Entry(Fenetre, textvariable="caca", width=30,font='Impact 13')
ISBN.place(x=220,y=250)
Bouttonsuivant = Button(Fenetre,text="Suite",height=1,command=traiter,font='Impact 12',fg='white',bg='red',cursor='hand2')#boutton pour passer à la page suivante
Bouttonsuivant.place(x=275,y=460)




Fenetre.mainloop()