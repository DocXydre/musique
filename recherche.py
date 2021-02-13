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
Fenetre.title("Saucisse")
Fenetre.geometry('1920x1080')

pygame.init()

#BOUCLE ACCUEIL
continuer_accueil = 1
notice = 0
recherche = 0

while continuer_accueil :
    fond = PhotoImage(file='menu.gif')
    LabPay=Label(Fenetre,image=fond)#image de fond
    LabPay.pack()
    intro=pygame.mixer.Sound("skyrock.wav")
    intro.play(loops=-1, maxtime=0, fade_ms=0)
    bug.set_volume(0.25)

    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_F1:
                continuer_accueil = 0	
                recherche = 1	    
            if event.key == K_F2:
                continuer_accueil = 0
                notice = 1

         
if notice == 1:
    fond = PhotoImage(file='menu.gif')
    LabPay=Label(Fenetre,image=fond)#image de fond
    LabPay.pack()
    intro=pygame.mixer.Sound("skyrock.wav")
    intro.play(loops=-1, maxtime=0, fade_ms=0)
    bug.set_volume(0.25)

if recherche == 1:
    fond = PhotoImage(file='menu.gif')
    LabPay=Label(Fenetre,image=fond)#image de fond
    LabPay.pack()
    intro=pygame.mixer.Sound("skyrock.wav")
    intro.play(loops=-1, maxtime=0, fade_ms=0)
    bug.set_volume(0.25)
    blaze= tk.Entry(Fenetre, textvariable="vald", width=30,font='Impact 13')
    blaze.place(x=220,y=250)
    nom= tk.Entry(Fenetre, textvariable="lezarman", width=30,font='Impact 13')
    nom.place(x=220,y=350)
    Bouttonsuivant = Button(Fenetre,text="Suite",height=1,command=traiter,font='Impact 12',fg='white',bg='red',cursor='hand2')#boutton pour passer à la page suivante
    Bouttonsuivant.place(x=220,y=460)



pygame.quit()
Fenetre.mainloop()
