import bs4 as bs
import urllib.request

sauce1 = urllib.request.urlopen("https://www.paroles.net/vald/paroles-vitrine")
soup1 = bs.BeautifulSoup(sauce1,'html5lib')
fichier = open('texte-vitrine.txt','w')
tmp = soup1.find('div',"song-text").text
fichier.write(tmp)
fichier.close()
