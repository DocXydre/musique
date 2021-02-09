def lien (artiste, nom):
    nom.strip()
    nom.replace(" ","-")
    url= 'https://www.paroles.net/'+artiste+'/paroles-'+nom
    return url

print(lien("vald","saucisse de mort"))
