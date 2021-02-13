def lien (artiste, nom):
    nom = nom.lower()
    nom = nom.strip()
    nom = nom.replace(" ","-")
    url= 'https://www.paroles.net/'+artiste+'/paroles-'+nom
    return url

print(lien("vald","saucisse de mort"))
