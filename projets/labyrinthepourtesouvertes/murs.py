import pygame
from pygame.locals import *
from random import randrange,choice
pygame.init()
 
taille=32
largeur=25 # au moins 5
hauteur=18 # au moins 3
vitesse=taille//4
msDeRepetitionTouches=40
fps=30
c=0 # pour les captures
nbreTeleporteurs=1
 
dansTeleporteur=False
 
fenetre=pygame.display.set_mode((largeur * taille,hauteur *taille))
pygame.display.set_caption("Amusons-nous avec des sprites !")
pygame.key.set_repeat(msDeRepetitionTouches,msDeRepetitionTouches)
perso=pygame.image.load("tp_spriteSheet_64.png").convert_alpha()
clock=pygame.time.Clock()
cube=pygame.transform.scale(pygame.image.load("CUBE5.png").convert_alpha(),(taille,taille))
fond=pygame.image.load("FOND.png").convert_alpha()



persoD=[]
for i in range(6):
    persoD.append(pygame.transform.scale(perso.subsurface(0+i*64,64,64,64),(taille,taille)))
 
persoG=[pygame.transform.flip(truc,True, False) for truc in persoD]
 
persoB=[]
for i in range(4):
    persoB.append(pygame.transform.scale(perso.subsurface(0+i*64,2*64,64,64),(taille,taille)))
 
persoH=[]
for i in range(4):
    persoH.append(pygame.transform.scale(perso.subsurface(0+i*64,0,64,64),(taille,taille)))
 
 
 
persorect=persoG[0].get_rect()
 
orientation="gauche"
a=0
b=0
fullscr=False
 
carte=[]
teleporteurs=[]
 
# une carte pleine de zéros ?
tableau=[]
for colonne in range(largeur):
    tableau.append(0)
for ligne in range(hauteur):
    carte.append(tableau)
 
#liste d'obstacles
obstacles=[]
 
def update(carte):
    obstacles=[]
    for ligne in range(hauteur):
        for colonne in range(largeur):
            if carte[ligne][colonne]==1:
                obstacles.append(pygame.Rect(colonne*taille,ligne*taille,taille,taille))
    return obstacles
 
obstacles=update(carte)
 
def bordsEtLignes():
    carteBords=[]
    #première ligne
    tableau=[]
    for colonne in range(largeur):
        if colonne==largeur//2 :
            tableau.append(0)
        else :
            tableau.append(1)
    carteBords.append(tableau)
    #autres lignes
    for ligne in range(1,hauteur-1):
        tableau=[1,0]
        for colonne in range(2,largeur-2):
            tableau.append((ligne+1)%2)
        tableau.append(0)
        tableau.append(1)
        carteBords.append(tableau)
    #dernière ligne
    tableau=[]
    for colonne in range(largeur):
        if colonne==largeur//2 :
            tableau.append(0)
        else :
            tableau.append(1)
    carteBords.append(tableau)
     
    return carteBords
 
def ajouteTeleporteurs():
    compteur=0
    teleporteurs=[]
    while compteur<nbreTeleporteurs :
        colonne=randrange(1,largeur-1)
        ligne=randrange(1,hauteur-1)
        if carte[ligne][colonne]==0:
            carte[ligne][colonne]=2
            compteur+=1
            print("teleporteur en",colonne,ligne)
            teleporteurs.append(pygame.Rect(colonne*taille,ligne*taille,taille,taille))
    return teleporteurs        
       

    
        
     
continuer=True
try:
    persorect.left=200
    persorect.top=200
    while continuer :
        fenetre.blit(fond,(0,0))
        for rectangle in obstacles :
            fenetre.blit(cube,rectangle)
        for rectangle in teleporteurs :
            pygame.draw.rect(fenetre,(255,255,0),rectangle,0)
        for rectangle in teleporteurs :
            if (persorect.centerx-rectangle.centerx)**2+(persorect.centery-rectangle.centery)**2<taille//4 and not dansTeleporteur:
                copie=teleporteurs[:]
                copie.remove(rectangle)
                newRect=choice(copie)
                #animation pour Tom
                for i in range (8):
                    pygame.draw.rect(fenetre,(i*30,255-i*30,255-i*30),rectangle,0)
                    pygame.display.flip()
                    pygame.time.delay(50)
                     
                persorect.centerx=newRect.centerx
                persorect.centery=newRect.centery
 
                #autre animation pour Tom - special dedicace
                if orientation=="gauche":
                    fenetre.blit(persoG[a],persorect)
                elif orientation=="droite":
                    fenetre.blit(persoD[a],persorect)
                elif orientation=="haut":
                    fenetre.blit(persoH[b],persorect)
                else :
                    fenetre.blit(persoB[b],persorect)
                for i in range (8):
                    pygame.draw.rect(fenetre,(255-i*30,i*30,i*30),newRect,0)
                    pygame.display.flip()
                    pygame.time.delay(50)
                     
                 
                dansTeleporteur=True
        if dansTeleporteur:
            dansTeleporteur=False
            for rectangle in teleporteurs :
                if persorect.colliderect(rectangle):
                    dansTeleporteur=True
                    break
             
         
        if orientation=="gauche":
            fenetre.blit(persoG[a],persorect)
        elif orientation=="droite":
            fenetre.blit(persoD[a],persorect)
        elif orientation=="haut":
            fenetre.blit(persoH[b],persorect)
        else :
            fenetre.blit(persoB[b],persorect)
 
         
         
        pygame.display.flip()
        clock.tick(fps)
         
        #gestion des événements
        for event in pygame.event.get():   
            if event.type==QUIT:
                continuer=0
            elif event.type==KEYDOWN:   #appui sur une touche
                if event.key==K_ESCAPE:
                    #print("touche Escape")
                    continuer=0
                elif event.key==K_LEFT:
                    #print("touche Gauche")
                    orientation="gauche"
                    a=(a+1)%6
                    persorect.left-=vitesse
                    if persorect.left<-taille:persorect.left=largeur*taille+taille
                    for obstacle in obstacles :
                        if persorect.colliderect(obstacle):
                            persorect.left=obstacle.right
                elif event.key==K_RIGHT:
                    #print("touche Droite")
                    orientation="droite"
                    a=(a+1)%6
                    persorect.left+=vitesse
                    if persorect.right>largeur*taille+taille:persorect.right=-100
                    for obstacle in obstacles :
                        if persorect.colliderect(obstacle):
                            persorect.right=obstacle.left
                elif event.key==K_UP:
                    #print("touche Haut")
                    orientation="haut"
                    persorect.top-=vitesse
                    b+=1
                    if b>3:b=0
                     
                    if persorect.bottom<-taille:persorect.top=hauteur*taille
                    for obstacle in obstacles :
                        if persorect.colliderect(obstacle):
                            persorect.top=obstacle.bottom
                elif event.key==K_DOWN:
                    #print("touche Bas")
                    orientation="bas"
                    persorect.bottom+=vitesse
                    b=(b+1)%4
                    if persorect.top>hauteur*taille+taille:persorect.bottom=0
                    for obstacle in obstacles :
                        if persorect.colliderect(obstacle):
                            persorect.bottom=obstacle.top
                elif event.key==K_p:
                    print("capture d'écran")
                    pygame.image.save(fenetre,"cm 2011-11-16 capture tp note %i.png"%c)
                    c+=1
 
                elif event.key==K_c:
                    carte=bordsEtLignes()
                    obstacles=update(carte)
                elif event.key==K_t:
                    print("teleporteurs")
                    teleporteurs=ajouteTeleporteurs()
                elif event.key==K_f:
                    fullscr=not fullscr

                    if fullscr : fenetre=pygame.display.set_mode((largeur * taille,hauteur *taille),FULLSCREEN)
                    else : fenetre=pygame.display.set_mode((largeur*taille,hauteur*taille))

                        
                else :
                    print("autre touche")
            elif event.type==MOUSEBUTTONUP:
                xmouse,ymouse=event.pos
                colonne=xmouse//taille
                ligne=ymouse//taille
                carte[ligne][colonne]=1-carte[ligne][colonne]
                obstacles=update(carte)
        
             
finally:
             
    pygame.quit()
