def lien (artiste, nom):
    nom.replace(" ","-")
    url= 'https://www.paroles.net/%27+artiste+%27/paroles-%27+nom
    return url

print(lien("vald","saucisse de mort"))