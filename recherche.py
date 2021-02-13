from tkinter import*
from tkinter import ttk 
import tkinter as tk 
import os
import pygame
from pygame.locals import *


def traiter():
    mes1=ISBN.get()
    print(mes1)

Fenetre=Tk()
Fenetre.title("Skyrock")
Fenetre.geometry('1920x1080')

pygame.init()

fond = PhotoImage(file='menu.gif')
LabPay=Label(Fenetre,image=fond)#image de fond

pygame.quit()
Fenetre.mainloop()
