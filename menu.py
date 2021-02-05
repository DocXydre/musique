#Import de toute les bibliothèque utile au code
from tkinter import*
from tkinter import ttk 
import tkinter as tk 
import os
import pygame

#définition de la fenêtre
Fenetre=Tk()#type
Fenetre.geometry('673x534')#taille
Fenetre.title("Bibliorecherche - Ajouter un livre " )#nom

#Variables
value5 = tk.StringVar(Fenetre)
value5.set("Catégorie")
value6 = tk.StringVar(Fenetre)
value6.set("Année de publication")


#Fonctions
def sortie():#fermer la fenêtre 
    Fenetre.destroy()

def effacer():
    value1.set("Numéro ISBN")
    value2.set("Titre de l'oeuvre")
    value3.set("Auteur de l'oeuvre")
    value4.set("Thème de l'oeuvre")
def effacer2():
    value5.set("Thème de l'oeuvre")
    value6.set("Année de publication")
    
def suivant():
    global mes1
    global mes2
    global mes3
    global mes4
    mes1=ISBN.get()
    mes2=Titre.get()
    mes3=Auteur.get()
    mes4=thème.get()
    ISBN.destroy()
    Titre.destroy()
    Auteur.destroy()
    thème.destroy()
    info.destroy()
    Bouttoneffacer.destroy()
    Bouttontraiter = Button(Fenetre,text="Enregistrer l'oeuvre",height=1,command=traiter,font='Impact 12',fg='white',bg='red',cursor='hand2')
    Bouttontraiter.place(x=275,y=460)
    #Partie 2 après avoir cliquer sur le boutton suite !
    Bouttoneffacer2 = Button(Fenetre,text='Effacer tout',width=10,height=1,command=effacer2,font='Impact 12',fg='white',bg='red',cursor='hand2')
    Bouttoneffacer2.place(x=50,y=375)
    Catégorie.place(x=220,y=250)
    Annéepub.place(x=220,y=300)

#Partie ajout: LA PLUS IMPORTANTE    
def traiter():
    global mes1#variables
    global mes2
    global mes3
    global mes4
    global mes5
    global mes6
    mes5=Catégorie.get()#récupère le contenu des zones entrées
    mes6=Annéepub.get()
    Récap = 'Le livre que vous avez enregistré est '+mes2+ ' son auteur est '+mes3+'\n'+'est sorti en: '+mes6+' ,il fait partie de la catégorie:'+mes5+'\n'+'son thème est: '+mes4+' et son numéro ISBN est: '+mes1
    Récapitulatif= Label(text=Récap)
    Récapitulatif.place(x=190,y=350)
    code2=mes1+';'+mes2+';'+mes3+';'';'+mes5+';'+mes4+';'+mes6
    #PARTIE IMPORTANT DE LA FONCTION AJOUT DANS UN FICHIER
    fichier= 'livres.csv' #on donne un nom à notre fichier, la livres.csv c'est mon fichier ou il y a les infos
    magie = open(fichier,"a")#on ouvre le fichier 
    magie.write(code2)#on écrit dans le fichier 
    magie.close()#on ferme le fichier 
    mess = Label(Fenetre,text='Votre oeuvre a bien été enregistrée :)')#petit message facultatif pour dire que l'opération à été faite
    #FIN DE LA PARTIE IMPORTANTE
    mess.place(x=250,y=500)
    print (code2)
    
def deums():
    cmd = 'Info.py'
    os.system(cmd)
    

#Import des images
Paysage = PhotoImage(file='add1.gif')
info1 = PhotoImage(file='inter.gif')



LabPay=Label(Fenetre,image=Paysage)#image de fond
LabPay.pack()

#1ère partie
Bouttonsortie = Button(Fenetre,text='Sortir',width=10,height=1,command=sortie,font='Impact 12',fg='white',bg='red',cursor='hand2')#boutton pour sortir
Bouttonsortie.place(x=550,y=460)
Bouttonsuivant = Button(Fenetre,text="Suite",height=1,command=suivant,font='Impact 12',fg='white',bg='red',cursor='hand2')#boutton pour passer à la page suivante
Bouttonsuivant.place(x=275,y=460)
Bouttoneffacer = Button(Fenetre,text='Effacer tout',width=10,height=1,command=effacer,font='Impact 12',fg='white',bg='red',cursor='hand2')#boutton pour sortir
Bouttoneffacer.place(x=50,y=375)
value1 = tk.StringVar(Fenetre)
value1.set("Numéro ISBN")
ISBN = tk.Entry(Fenetre, textvariable=value1, width=30,font='Impact 13')
ISBN.place(x=220,y=250)
value2 = tk.StringVar(Fenetre)
value2.set("Titre de l'oeuvre")
Titre = tk.Entry(Fenetre, textvariable=value2,width=30, font='Impact 13')
Titre.place(x=220,y=300)
value3 = tk.StringVar(Fenetre)
value3.set("Auteur de l'oeuvre")
Auteur = tk.Entry(Fenetre, textvariable=value3, width=30, font='Impact 13')
Auteur.place(x=220,y=350)
value4 = tk.StringVar(Fenetre)
value4.set("Thème de l'oeuvre")
thème = ttk.Combobox(Fenetre,textvariable=value4,values=["January", "February","March","April"],width=28, font='Impact 13')
thème.place(x=220,y=400)
info=Button(Fenetre,image=info1,command=deums)
info.place(x=475,y=250)

Catégorie = ttk.Combobox(Fenetre,textvariable=value5,values=["Bande Dessinée, Comics & Manga", "Romans & Fictions","Arts & Culture","Documents & Médias","Enseignement & Education","Erotisme","Esotérisme","Santé & Bien-être","Histoire & Géographie","Jeunesse","Langues","Littérature & Lettres","Loisirs, Vie pratique& Société","Religions & Spiritualité","Sciences Humaines","Sciences & Techniques","Sciences Sociales"],width=28, font='Impact 13')
Annéepub = ttk.Combobox(Fenetre,textvariable=value6,values=["1899","1900",  "1901",	"1902",	"1903",	"1904"	,"1905"	,"1906"	,"1907"	,"1908"	,"1909","1910",	"1911",	"1912",	"1913",	"1914"	,"1915"	,"1916"	,"1917"	,"1918"	,"1919","1920",	"1921",	"1922",	"1923",	"1924"	,"1925"	,"1926"	,"1927"	,"1928"	,"1929","1930",	"1931",	"1932",	"1933",	"1934"	,"1935"	,"1936"	,"1937"	,"1938"	,"1939","1940",	"1941",	"1942",	"1943",	"1944"	,"1945"	,"1946"	,"1947"	,"1948"	,"1949","1950",	"1951",	"1952",	"1953",	"1954"	,"1955"	,"1956"	,"1957"	,"1958"	,"1959","1960",	"1961",	"1962",	"1963",	"1964"	,"1965"	,"1966"	,"1967"	,"1968"	,"1969","1970",	"1971"	,"1972"	,"1973","1974","1975",	"1976",	"1977"	,"1978"	,"1979","1980",	"1981"	,"1982"	,"1983"	,"1984","1985",	"1986",	"1987"	,"1988"	,"1989","1990",	"1991"	,"1992"	,"1993"	,"1994","1995",	"1996",	"1997"	,"1998"	,"1999","2000",	"2001"	,"2002"	,"2003"	,"2004","2005",	"2006",	"2007"	,"2008"	,"2009","2010",	"2011"	,"2012","2013"	,"2014","2015",	"2016",	"2017"	,"2018"	,"2019","2020"],width=28, font='Impact 13')
mes1=ISBN.get()
mes2=Titre.get()
mes3=Auteur.get()
mes4=thème.get()
mes5=Catégorie.get()
mes6=Annéepub.get()


Fenetre.mainloop()#Lancement de la fenêtre
pygame.quit()# cette dernière ligne permet de quitter correctement pygame sans bugs