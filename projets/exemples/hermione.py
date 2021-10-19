import pygame
from pygame.locals import *

###############################
#      Initialisation         #
###############################

# Initialisation de Pygame
pygame.init()
# création d'une fenête de 640 sur 480
L = 640
H = 480
TAILLE = 64
fenetre = pygame.display.set_mode((L, H))
# Titre de la fenêtre :
pygame.display.set_caption("Mon jeu")
# Initialisation d'une horloge.
# Utile pour gérer la fréquence d'images en jeu
clock = pygame.time.Clock()
# Répétition d'une touche
pygame.key.set_repeat(50, 10)

###############################
#       Le fond               #
###############################
# Un fond en couleur
VIOLET = (127, 0, 255) # Format RGB
# fill pour remplir la fenêtre de la couleur donnée.
fenetre.fill(VIOLET)

# Une image de fond
fond = pygame.image.load("sable.jpg").convert()
# Maintenant il faut coller l'image dans la fenêtre au coordonnées (0, 0)
fenetre.blit(fond, (0, 0))

###############################
#       Le perso              #
###############################
# On charge l'image complète
hermione_toutes = pygame.image.load("hermione.png").convert_alpha()
directions = ["b", "g", "d", "h"]
dico = {}
for i in range(4):
    l = []
    for j in range(6):
        hermione = pygame.Surface.subsurface(hermione_toutes, (32 * j, 32 * i, 32, 32))
        hermione= pygame.transform.scale(hermione, (TAILLE, TAILLE))
        l.append(hermione)

    dico[directions[i]] = l
print(dico)
# On change un peu la taille
hermione1 = pygame.Surface.subsurface(hermione_toutes, (0, 0, 32, 32))
diana_g = pygame.transform.scale(hermione1, (64, 64))
diana_g = diana_g
# On prend aussi le symétrique
diana_d = pygame.transform.flip(diana_g, True, False)
# On crée un rectangle de la même taille que Diana
diana_rec = diana_g.get_rect()
# On place ce rectangle
diana_rec.left = 0
diana_rec.top = 0
# Et enfin, on colle l'image dans le rectangle.
fenetre.blit(dico["d"][0], diana_rec)
# Pour savoir dans quel sens va diana
orientation = "g"

###############################
#      La boucle de jeu       #
###############################
continuer = True
pas = 0
while continuer:
    # gestion des événements non clavier
    # On recolle le fond, pour avoir un fond propre :)
    fenetre.blit(fond, (0, 0))
    for event in pygame.event.get():
        # la croix en haut à droite
        if event.type == QUIT:
            continuer = False
        elif event.type == KEYDOWN:  # appui sur une touche
            pas += 1
            if event.key == K_RIGHT:
                #rint("touche Droite")
                orientation = "d"
                diana_rec.left += 5
            if event.key == K_LEFT:
                #print("touche gauche")
                orientation = "g"
                diana_rec.left -= 5
                if diana_rec.left < 0 - TAILLE:
                    diana_rec.left += L + TAILLE
            if event.key == K_DOWN:
                #print("touche b")
                orientation = "b"
                diana_rec.top += 5
            if event.key == K_UP:
                #print("touche haut")
                orientation = "h"
                diana_rec.top -= 5

    # Il faut coller l'image dans le rectangle à sa nouvelle place.
    fenetre.blit(dico[orientation][pas % 6], diana_rec)

    # On rafraichit à chaque tour de boucle.

    pygame.display.flip()