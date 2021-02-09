from tkinter import*
from tkinter import ttk 
import tkinter as tk 
import os
import bs4 as bs
import urllib.request


Fenetre=Tk()
Fenetre.title("SKYROCK - PREMIER SUR LE RAP")
Fenetre.geometry('673x534')

Amour = ["amour","aime","baise","cœur","amoureux","tendresse","amitié","baiser","Cupidon","Aphrodite","passion","Éros","désir","sentiment","amant","affection","idylle","Vénus","attachement","attirance","platonique","compassion","plaisir","charité","érotique","haine","relation","beauté","adoration","aimer","philtre","altruisme","amourette","bien-aimé","érotisme","joie","mariage","romantique","courtois","émotion","déesse","éternel","luxure","bonheur","conjugal","jalousie","psyché","filial","fraternel","charnel","chaste","sexualité","dévotion","ivresse","philanthropie","couple","fidélité","tendre","sincère","volupté","Dieu","idolâtrie","piété","souffrance","troubadour","chant","chasteté","désespoir","libertinage","romantisme","solitude","désamour","poésie","sacrifice","poème","sensualité","sexuel","chagrin","romance","hymen","séduction","âme","dilection","lyrique","ode","thème","abnégation","bagatelle","bien-aimée","chanson","conquête","déclaration","désintéressement","fou","indifférence","passionné","adultère","amor","enchantement","femme","inceste"]
Argent = ["monnaie","métal","somme","banque","sou","thune","bourse","caisse","denier","argenterie","trésor","dépense","blé","fric","lingot","magot","dépenser","fonds","finance","flouze","oseille","crédit","rembourser","loterie","billet","pèze","amasser","créancier","maille","achat","avarice","écu","médaille","sac","jeu","payer","prêter","dette","pognon","richesse","blanchiment","débourser","prostitution","pute","rançon","rond","bijou","économiser","casino","dollar","papier","prêt","coffre","gucci","louis vuitton","gagner","précieux","dior","vendu","prix","fortune","précieux","bancaire","vendre","versement","impôt","poche","recette","salaire","volé","commerce","espèce","liquide","comptant","désargenter","diamant","gisement","loyer","mercenaire","contrôle","métallique","paiement","plaqué","rapporter","sesterce","vénal","argent","sale","chèque","empocher","endetté","escroquer","inflation","métal","blanc","minerai","radin","soutirer","sulfure","trésorerie","butin","économe","économie","financer","millionnaires","orfèvrerie","papier","PayPal","pièce","acheter","centime","virement","investissement","pièce","racket","transaction","banque","braquage","budget","échange","encaisser","produit","dépensier","verser","cagnotte","dévaliser","marchand","coûtait","milliardaire","montant","payement","tune","affaires"]
Drogue=['gue-dro','opium','cannabis','héroïne','trafic','céllophanée','cocaïne','trafiquant','alcool','stupéfiant','dope','médicament','toxicomanie','addiction','dépendance','psychotrope','dealer','dose','ecstasy','came','LSD','amphétamine','conso','crack','deal','fumette','substance','addictif','sniffer','toxicomane','narcotique','overdose','haschich','désintoxication','rave','tabac','cartel','intraveineuse','surdose','défonce','emprise','psychédélique','shooté','alcaloïde','gang','médicinal','narcoterroriste','marijuana','shit','accoutumance','bicrave','caïd','consommé','illicite','légalisation','manque','mélange','seringue','sexe','trafic de drogue','dopage','hallucinogène','morphine','poison','sevrage','procurer','toxico','compulsif','kétamine','méthamphétamine','narcotrafic','toxique','consommateur','criminalité','délinquance','effet','pharmacie','racket','réseau','vape','coke','Colombie','revendeur','alcoolisme','hallucination','injection','narcotrafiquant','orviétan','antidrogue','arsenic','bad trip','bicraveur','camelote','chlague','chnek','chnouf','choper','contrebande','daube','déchiré','dépouillé','désomorphine','droguier','droguiste','faya','fechnou','fly','foncedé','guedro','illégal','junkie','junky','leurdi','mafia','merde','meuca','meumeu','mixture','narco-État','palliatif','pécho','pété','pharmacologie','police','potion','pouilledé','psychoactif','purge','schnouf','schnouff','se camer','se shooter','séquelle','shoot','stone','stup','Tox','célophané','toxine','trip','triper','tripper','usager','venin','virus']

def traiter():
    URL_parolesnet=URL_entry.get()
    print(URL_parolesnet)
    sauce1 = urllib.request.urlopen(URL_parolesnet)
    soup1 = bs.BeautifulSoup(sauce1,'html5lib')
    fichier = open('texte.txt','w')
    tmp = soup1.find('div',"song-text").text #on cherche tous le texte qui se situe dans les balises div de class 'song-texte'
    fichier.write(tmp)
    fichier.close()
    nb_amour = 0
    nb_argent = 0
    nb_drogue = 0 
    lire = open('texte.txt','r')
    chanson = lire.read()
    for i in range(len(Amour)):
        #compteur = boyer_moore('texte.txt',Amour[i])
        compteur = boyer_moore(chanson,Amour[i])
        nb_amour = nb_amour + compteur
    for i in range(len(Argent)):
        compteur2 = boyer_moore(chanson,Argent[i])
        nb_argent = nb_argent + compteur2
    
    for i in range(len(Drogue)):
        compteur3 = boyer_moore(chanson,Drogue[i])
        nb_drogue = nb_drogue + compteur3
    print(nb_amour)
    print(nb_argent)
    print(nb_drogue)
    if max(nb_amour,nb_argent,nb_drogue) == nb_amour:
        print("C'est une chanson d'amour")

    if max(nb_amour,nb_argent,nb_drogue) == nb_argent:
        print("C'est une chanson d'argent")
        
    if max(nb_amour,nb_argent,nb_drogue) == nb_drogue:
        print("C'est une chanson de drogue")

def table_sauts(cle) :
    """la fonction renvoie la table de décalage en utilisant la formule :
    pour toute lettre de cle : decalage = longueur de cle - index de la lettre -1
    sauf dernière lettre et toutes les autres : decalage = longueur de cle
    precondition :
        cle : string
    postcondition :
        dict
    """
    d = {}
    for i in range(len(cle)-1) :
        d[cle[i]] = len(cle)-i-1
    for lettre in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' :
        if lettre not in d.keys() :
            d[lettre] = len(cle)
    return d
def boyer_moore (texte, cle):
    texte = texte.upper()
    cle = cle.upper()
    long_txt = len(texte)
    long_cle = len(cle)
    positions = [] #liste des positions où l'on trouve le motif
    if long_cle <= long_txt :
        decalage = table_sauts(cle) #on charge la table des décalages
    i=0
    trouve = False
    while (i <= long_txt-long_cle):
        for j in range (long_cle -1, -1, -1): #On part du dernier indice de la cle jusque 0 en décalant de -1 à chaque fois
            trouve = True
            if texte[i+j] != cle[j] : # Si on tombe sur une lettre différentes de celle de la clé
                if (texte[i+j] in decalage and decalage[texte[i+j]]<=j):
                    i+=decalage[texte[i+j]] # on décale dans le texte en utilisant la table de décalage
                else :
                    i+=j+1 # si la lettre n'est pas dans la table de décalage alors on décale du nombre de lettres restantes à explorer sur la clé
                trouve = False
                break #on sort de la boucle for car on a trouvé une lettre qui ne convient pas
        if trouve : #si toutes les lettres convenait donc on a trouvé une occurence de la clé dans texte
            positions.append(i) #on ajoute à la liste des positions où l'on trouve la clé dans le texte
            i=i+1
            trouve = False #on remet trouvé à False car on cherche la prochaine occurence
    return len(positions)

URL_entry = tk.Entry(Fenetre, textvariable="caca", width=30,font='Impact 13')
URL_entry.place(x=220,y=250)
Bouttonsuivant = Button(Fenetre,text="Suite",height=1,command=traiter,font='Impact 12',fg='white',bg='red',cursor='hand2')#boutton pour passer à la page suivante
Bouttonsuivant.place(x=275,y=460)



Fenetre.mainloop()
