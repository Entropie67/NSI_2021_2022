import pygame
from pygame.locals import *
from random import randrange,choice
from carteALeatoire import newCarteAvecDepartEtArrivee
from parcoursLargeurCQ import trouver3,trouver4252,cheminLePlusCourt

def calculScore(c,t,coeffCalque,coeffChemin,coeffdif):
    return int((t*20/(10*t+10*c))*1000*coeffCalque*coeffChemin*coeffdif)


def distance(x1,y1,x2,y2):
    return ((x1-x2)**2+(y1-y2)**2)**0.5
    
def creationSprites(spritesheet,taille):
    """ création des listes puis de la liste de sprites """
    feuille=pygame.image.load(spritesheet).convert_alpha()

    #droite chargée depuis la spritesheet
    persoD=[]
    for i in range(6):
        persoD.append(pygame.transform.scale(feuille.subsurface(0+i*64,64,64,64),(taille,taille)))

    # gauche par symétrie
    persoG=[pygame.transform.flip(truc,True, False) for truc in persoD]

    #bas chargée depuis la spritesheet
    persoB=[]
    for i in range(4):
        persoB.append(pygame.transform.scale(feuille.subsurface(0+i*64,2*64,64,64),(taille,taille)))

    #haut chargée depuis la spritesheet
    persoH=[]
    for i in range(4):
        persoH.append(pygame.transform.scale(feuille.subsurface(0+i*64,0,64,64),(taille,taille)))

    #tout dans une seule liste pour améliorer le code
    return [persoD,persoH,persoG,persoB]  # D, H, G, B



#cette fonction lite la liste 
def update(carte,hauteur,largeur,taille):
    """"Cette fonction lit la carte, une liste de listes d'entiers
    carte[i][j] correspond à la i-ème ligne et la j-ème colonne
    0 si vide
    1 si mur -> on crée alors un rectangle """
    obstacles=[] # cide au début
    for ligne in range(hauteur):  # parcours de la carte
        for colonne in range(largeur): # parcours de la carte
            if carte[ligne][colonne]==1: # il orientationfaut créer un bout de mur
                # donc on crée le rectangle et on le rajoute à la liste
                obstacles.append(pygame.Rect(colonne*taille,ligne*taille,taille,taille))
    return obstacles # on renvoie la liste


def jeu(resolution,fenetre,poseCalque=True,afficheChemin=False,taille=64):
    #resolution=[1600,960] # à changer

    #On compte les joysticks
    nb_joysticks = pygame.joystick.get_count()
    print("Il y a", nb_joysticks, "joystick(s) branché(s)")

    #Et on en crée un s'il y a en au moins un
    if nb_joysticks > 0:
        mon_joystick = pygame.joystick.Joystick(0)
        mon_joystick.init() #Initialisation
    
    #taille=64  # d'une case, du perso aussi
    largeur=(resolution[0]//(2*taille))*2-1 # au moins 5 : le nombre de cases
    hauteur=(resolution[1]//(2*taille))*2-1 # au moins 3 : le nombre de cases
    vitesse=taille//4   #vitesse devrait être un diviseur de taille

    # pour la nouvelle gestion des déplacements
    vecteur=[(vitesse,0),(0,-vitesse),(-vitesse,0),(0,vitesse)] # D, H, G, B
    liste=[] # pour l'historique des déplacements
    listeOrdi=[]
    rayon=vitesse//2 # rayon des cercles

    calque=pygame.image.load("calque.png").convert_alpha() #820 x 820
    maxRes=max(resolution[0],resolution[1])
    calque=pygame.transform.scale(calque,(maxRes*2,maxRes*2))
    

    msDeRepetitionTouches=20 # 20 et 50 c'est cohérent
    fps=25 # 20 et 50 c'est cohérent
    c=0 # pour les captures
    
    # paramètres de vitesse et de fluidité
    pygame.key.set_repeat(msDeRepetitionTouches,msDeRepetitionTouches)
    clock=pygame.time.Clock() # pour le nombre d'image/sec avec clock.tick après

    carte=newCarteAvecDepartEtArrivee(largeur,hauteur)

    #liste d'obstacles
    obstacles=update(carte,hauteur,largeur,taille)


    perso = creationSprites('black.png',taille)
    persordi =creationSprites('V3IA.png',taille)
    xD,yD=trouver3(carte,hauteur,largeur)
    print("Départ en",xD,yD)
    xA,yA=trouver4252(carte,hauteur,largeur)
    print("Arrivée en",xA,yA)

    #chemin optimal ?
    chemin=cheminLePlusCourt(carte,hauteur,largeur)
    #afficheChemin=False
    
    # crée le rectangle du personnage. Cette case devrait être libre
    persorect=pygame.Rect(taille*xD,taille*yD,taille,taille)
    ordirect=pygame.Rect(taille*xD,taille*yD,taille,taille)
    #orientation="gauche"
    #orientation passe en entier 0 pour droite, 1 pour haut ...

    #pour éviter les sorties du labyrinthe
    obstacles.append(pygame.Rect(taille*xD,taille*(yD-1),taille,taille))
    obstacles.append(pygame.Rect(taille*xA,taille*(yA+1),taille,taille))

    orientation =2 #gauche
    nextorientation=2
    orDientation=3 #bas

    a=0 # a va aller de 0 à 11 et
    # on travaillera modulo 4 ou modulo 6 selon les directions
    b=0 # pour l'ordi

    #police de caracteres
    font=pygame.font.SysFont("comic",200,bold=True,italic=False)



    continuer=True # pour la boucle perpétuelle de jeu

    #persorect.left=200 inutile avec la nouvelle définition de persorect
    #persorect.top=200
    temps_initial=pygame.time.get_ticks()
    longueurMin=len(chemin)
    tempsOptimal=longueurMin*4*1000/fps
    coeffCalque=1
    coeffChemin=1
    # Coefficient de difficulté
    if 40<= longueurMin <50 : coeffDif=0.9
    elif 30<= longueurMin <40 : coeffDif=0.8
    elif 20<= longueurMin <30 : coeffDif=0.7
    elif 10<= longueurMin <20 : coeffDif=0.6
    elif longueurMin <10 : coeffDif=0.5
    else : coeffDif=1
    
    while continuer : # boucle principale

        # le fond et les décors
        # le fond
        fenetre.fill((0,0,0)) 

        # les murs
        for rectangle in obstacles[:-2] :
            pygame.draw.rect(fenetre,(0,255,255),rectangle,0)

        if afficheChemin :
            coeffChemin=0.5
            for (abscisse,ordonnee) in chemin :
                pygame.draw.rect(fenetre,(160,100,100),(abscisse*taille,ordonnee*taille,taille,taille),0)

        # des disques avec la liste des positions antérieures
        degrade=0
        for centre in liste :
            pygame.draw.circle(fenetre,(degrade*6,degrade*6,0),centre, rayon,0)
            degrade+=1
        degrade=0
        for centre in listeOrdi :
            pygame.draw.circle(fenetre,(degrade*2,degrade*2,degrade*2),centre, rayon//2,0)
            degrade+=1
        #Départ 
        pygame.draw.circle(fenetre,(255,0,0),(xD*taille+taille//2,yD*taille+taille//2),taille//3,0)
        
        #arrivée
        pygame.draw.circle(fenetre,(255,0,255),(xA*taille+taille//2,yA*taille+taille//2),taille//3,0)
        
        # avec la fenetrenouvelle liste de listes, une seule ligne
        # grosse magouille mathématique pour gérer le 4 ou 6 suivant les listes
        fenetre.blit(perso[orientation][a%(5+(-1)**orientation)],persorect)
        fenetre.blit(persordi[orDientation][b%(5+(-1)**orDientation)],ordirect)
        
        # Calque ?
        if poseCalque :
            fenetre.blit(calque,(persorect.centerx-maxRes,persorect.centery-maxRes))
        else :
            coeffCalque=0.8
        temps_actuel=pygame.time.get_ticks()
        chrono=temps_actuel-temps_initial

        
        text2=font.render("Temps : "+str(chrono//1000)+ "s",1,(255,255,255))
        fenetre.blit(text2,(10,10))

        score=calculScore(chrono,tempsOptimal,coeffCalque,coeffChemin,coeffDif)
        text2=font.render("Score : "+str(score),1,(255,0,255))
        fenetre.blit(text2,(resolution[0]//4,10))


        # on bascule l'affichage
        pygame.display.flip()
        # avec un nombre d'images par secondes maîtrisé
        clock.tick(fps)

        # jeu fini ?
        if distance(persorect.centerx,persorect.centery,xA*taille+taille//2,yA*taille+taille//2)<taille//8:
            text2=font.render("Gagné en "+str(chrono//1000)+ "s",1,(255,255,255))
            fenetre.blit(text2,(resolution[0]//3,resolution[1]//2))
            pygame.display.flip()
            pygame.time.delay(2000)
            score=calculScore(chrono,tempsOptimal,coeffCalque,coeffChemin,coeffDif)
            continuer=False
        if distance(ordirect.centerx,ordirect.centery,xA*taille+taille//2,yA*taille+taille//2)<taille//8:
            text2=font.render("Perdu en "+str(chrono//1000)+ "s",1,(255,255,255))
            fenetre.blit(text2,(resolution[0]//3,resolution[1]//2))
            pygame.display.flip()
            pygame.time.delay(2000)
            score=0
            continuer=False
			
        #solution "mur droit" version Marchant pour ordi
        b=(b+1)%12 # curseur d'animation
        orDientation=(orDientation+4-1)%4 # on essaie à droite
        choix=False
        while not choix :
            ordirect.move_ip(vecteur[orDientation]) # le déplacement est virtuel
            choix=True # mais passera à False si on trouve un mur
            # Dans un mur ?
            for obstacle in obstacles :
                if ordirect.colliderect(obstacle): # oui
                    choix=False
                    break
            ordirect.move_ip(vecteur[(orDientation+2)%4]) # le déplacement était virtuel
            if not choix : orDientation=(orDientation+1)%4 # on essaie moins à droite
    
        # On se souvient de la position actuelle
        listeOrdi.append((ordirect.centerx,ordirect.centery))
        # On se déplace
        ordirect.move_ip(vecteur[orDientation])
        # S'il y a mur
        for obstacle in obstacles :
            if ordirect.colliderect(obstacle):
                ordirect.move_ip(vecteur[(orDientation+2)%4])
                # on supprime le dernier de la liste
                listeOrdi=listeOrdi[:-1]

        listeOrdi=listeOrdi[-128:]

        #deplacement Perso
        

        if nextorientation != orientation :
            #test nextorientation
            persorect.move_ip(vecteur[nextorientation])
            # S'il y a mur
            if persorect.collidelist(obstacles)==-1:
                orientation=nextorientation
            # quoiqu'il en soit
            persorect.move_ip(vecteur[(nextorientation+2)%4])

        # On se souvient de la position actuelle
        liste.append((persorect.centerx,persorect.centery))

        #tentative de déplacement avec orientation
        persorect.move_ip(vecteur[orientation])
        # S'il y a mur
        if not persorect.collidelist(obstacles)==-1:
            persorect.move_ip(vecteur[(orientation+2)%4])
            liste=liste[:-1]
        else :
            a=(a+1)%12 # curseur d'animation
        
        # On en garde 42
        liste=liste[-42:]
        
        #gestion des événements
        for event in pygame.event.get():   
            if event.type==QUIT: # la croix à cliquer
                continuer=False # on sort
                score=0
            elif event.type==JOYBUTTONDOWN :
                if event.button == 2 :
                    nextorientation=0
                elif event.button == 0 :
                    nextorientation=2
                elif event.button == 1 :
                    nextorientation=3
                elif event.button == 3 :
                    nextorientation=1
                elif event.button == 5 or event.button == 7:
                    poseCalque = not poseCalque
                elif event.button == 6 or event.button == 8:
                    afficheChemin = not afficheChemin

            elif event.type == JOYAXISMOTION:
                if event.axis == 0 :
                    if event.value > 0:
                        nextorientation=0
                    elif event.value < 0:
                        nextorientation=2
                elif event.axis == 1 :
                    if event.value > 0:
                        nextorientation=3
                    elif event.value < 0:
                        nextorientation=1
                        
            elif event.type==KEYDOWN:   #appui sur une touche
                if event.key==K_ESCAPE:
                    #print("touche Escape")
                    continuer=False # on sort
                    score=0
                        
                    #print("On a choisi",orientation)

                elif event.key==K_UP:
                    nextorientation=1
                elif event.key==K_DOWN:
                    nextorientation=3
                elif event.key==K_RIGHT:
                    nextorientation=0
                elif event.key==K_LEFT:
                    nextorientation=2
                
                
                                                                          
                elif event.key==K_p:
                    print("capture d'écran")
                    pygame.image.save(fenetre,"capture%i.png"%c)
                    c+=1

                elif event.key==K_t:
                    poseCalque = not poseCalque
                elif event.key==K_f:
                    afficheChemin = not afficheChemin
                elif event.key==K_c:
                    carte=newCarteAvecDepartEtArrivee(largeur,hauteur)
                    obstacles=update(carte,hauteur,largeur,taille)

                    xD,yD=trouver3(carte,hauteur,largeur)
                    print("Départ en",xD,yD)
                    xA,yA=trouver4252(carte,hauteur,largeur)
                    print("Arrivée en",xA,yA)

                    #chemin optimal ?
                    chemin=cheminLePlusCourt(carte,hauteur,largeur)

                    temps_initial=pygame.time.get_ticks()
    
    

                    # crée le rectangle du personnage.
                    persorect=pygame.Rect(taille*xD,taille*yD,taille,taille)
                    ordirect=pygame.Rect(taille*xD,taille*yD,taille,taille)
                    orientation =2 #gauche
                    nextorientation=2
                    orDientation=3 #bas
                    liste=[] # pour l'historique des déplacements
                    listeOrdi=[]
                    
    

    

    return int(score)
