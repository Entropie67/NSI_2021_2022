def afficheCarte(carte,largeur,hauteur):
    for ligne in range(hauteur):
        for colonne in range(largeur):
            print(carte[ligne][colonne],end='\t')
        print()
    print()


def destinationsPossibles(carte,x,y,rang,largeur,hauteur):
    liste=[]
    if x+1<largeur and (carte[y][x+1]==0 or carte[y][x+1]>rang+1 or carte[y][x+1]>rang+1):
        liste.append((x+1,y))
    if x-1>=0 and (carte[y][x-1]==0 or carte[y][x-1]>rang+1 or carte[y][x-1]>rang+1):
        liste.append((x-1,y))
    if y+1<hauteur and (carte[y+1][x]==0 or carte[y+1][x]>rang+1 or carte[y+1][x]>rang+1):
        liste.append((x,y+1))
    if y-1>=0 and (carte[y-1][x]==0 or carte[y-1][x]>rang+1 or carte[y-1][x]>rang+1):
        liste.append((x,y-1))
    return liste


def marqueSuivantsOuTrouve(carte,x,y,rang,largeur,hauteur):
    suivants=destinationsPossibles(carte,x,y,rang,largeur,hauteur)
    for point in suivants:
        x=point[0]
        y=point[1]
        if carte[y][x]==4252 :
            print("trouvé et le rang est",rang)
        else :
            carte[y][x]=rang+1
            #afficheCarte(carte,largeur,hauteur)
            marqueSuivantsOuTrouve(carte,x,y,rang+1,largeur,hauteur)



def trouver3(carte,hauteur,largeur):
    for ligne in range(hauteur):
        for colonne in range(largeur):
            if carte[ligne][colonne]==3:
                yd=ligne #correction ici
                xd=colonne #correction ici
                break
                break
    return xd,yd


def trouver4252(carte,hauteur,largeur):
    for ligne in range(hauteur):
        for colonne in range(largeur):
            if carte[ligne][colonne]==4252:
                ya=ligne #correction ici
                xa=colonne #correction ici
                break
                break
    return xa,ya


#recherche du minimal 
def trouverLePlusPetitMinimalPlusGrandQueUn(xa,ya,carte,hauteur,largeur):
    xcherche,ycherche=xa,ya
    # j'ai corrigé ici y'avait xa-1>0 c'est xa>0
    if xa>0 and carte[ya][xa-1]<carte[ycherche][xcherche] and carte[ya][xa-1]>1 :
        xcherche=xa-1
    if xa+1<largeur and carte[ya][xa+1]<carte[ycherche][xcherche] and carte[ya][xa+1]>1 :
        xcherche=xa+1
    #idem avec ya
    if ya>0 and carte[ya-1][xa]<carte[ycherche][xcherche] and carte[ya-1][xa]>1 :
        ycherche=ya-1
    if ya+1<hauteur and carte[ya+1][xa]<carte[ycherche][xcherche] and carte[ya+1][xa]>1 :
        ycherche=ya+1
    return xcherche,ycherche

def cheminLePlusCourt(carte,hauteur,largeur):
    #afficheCarte(carte,largeur,hauteur)
    xd,yd=trouver3(carte,hauteur,largeur)
    #print(xd,yd)
    marqueSuivantsOuTrouve(carte,xd,yd,3,largeur,hauteur)
    #afficheCarte(carte,largeur,hauteur)

    xa,ya=trouver4252(carte,hauteur,largeur)
    #print(xa,ya)
    chemin=[(xa,ya)]
    x,y=xa,ya
    while carte[y][x]>3:
        x,y=trouverLePlusPetitMinimalPlusGrandQueUn(x,y,carte,hauteur,largeur)
        #print(x,y)
        chemin.append((x,y))
    chemin.reverse()
    #print(chemin)
    #print(len(chemin),"étapes")
    return chemin
    

#A décommenter pour les tests
#from carteALeatoire import newCarteAvecDepartEtArrivee
#largeur=11
#hauteur=13
#carte=newCarteAvecDepartEtArrivee(largeur,hauteur)
#cheminLePlusCourt(carte,hauteur,largeur)
