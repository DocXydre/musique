from tkinter import*
from tkinter import ttk 
import tkinter as tk 
import os
import pygame

Fenetre=Tk()
Fenetre.title("Saucisse")
Fenetre.geometry('1920x1080')

fond = PhotoImage(file='menu.gif')

pygame.init()
intro=pygame.mixer.Sound("skyrock.wav")

LabPay=Label(Fenetre,image=fond)#image de fond
LabPay.pack()

def traiter():
    mes1=ISBN.get()
    print(mes1)

intro.play
blaze= tk.Entry(Fenetre, textvariable="vald", width=30,font='Impact 13')
blaze.place(x=220,y=250)
nom= tk.Entry(Fenetre, textvariable="lezarman", width=30,font='Impact 13')
nom.place(x=220,y=350)
Bouttonsuivant = Button(Fenetre,text="Suite",height=1,command=traiter,font='Impact 12',fg='white',bg='red',cursor='hand2')#boutton pour passer à la page suivante
Bouttonsuivant.place(x=220,y=460)

pygame.quit()
Fenetre.mainloop()