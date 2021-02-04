###SCRAPING d'une page WEB avec le module beautifulsoup (bs4)###
###enregistre le texte de la chanson "paroles des reves et des cendres" du rappeur Lino###
import bs4 as bs
import urllib.request


sauce1 = urllib.request.urlopen("https://www.paroles.net/lino/paroles-des-revees-et-des-cendres")
soup1 = bs.BeautifulSoup(sauce1,'html5lib')
fichier = open('texte-lino.txt','w')
tmp = soup1.find('div',"song-text").text #on cherche tous le texte qui se situe dans les balises div de class 'song-texte'
fichier.write(tmp)
fichier.close()





