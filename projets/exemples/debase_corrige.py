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
# On charge l'image
diana_g = pygame.image.load("Diana.png").convert_alpha()
# On change un peu la taille
diana_g = pygame.transform.scale(diana_g, (64, 64))
# On prend aussi le symétrique
diana_d = pygame.transform.flip(diana_g, True, False)
# On crée un rectangle de la même taille que Diana
diana_rec = diana_g.get_rect()
# On place ce rectangle
diana_rec.left = 200
diana_rec.top = 200
# Et enfin, on colle l'image dans le rectangle.
fenetre.blit(diana_g, diana_rec)
# Pour savoir dans quel sens va diana
orientation = "gauche"

###############################
#      La boucle de jeu       #
###############################
continuer = True
while continuer:
    # gestion des événements non clavier
    for event in pygame.event.get():
        # la croix en haut à droite
        if event.type == QUIT:
            continuer = False
        elif event.type == KEYDOWN:  # appui sur une touche
            if event.key == K_RIGHT:
                print("touche Droite")
                orientation = "droite"
                diana_rec.left += 5
            if event.key == K_LEFT:
                print("touche gauche")
                orientation = "gauche"
                diana_rec.left -= 5
            if event.key == K_DOWN:
                print("touche bas")
                orientation = "gauche"
                diana_rec.top += 5
            if event.key == K_UP:
                print("touche haut")
                orientation = "gauche"
                diana_rec.top -= 5
    # On recolle le fond, pour avoir un fond propre :)
    fenetre.blit(fond, (0, 0))
    # Il faut coller l'image dans le rectangle à sa nouvelle place.
    if orientation == "gauche":
        fenetre.blit(diana_g, diana_rec)
    elif orientation == "droite":
        fenetre.blit(diana_d, diana_rec)
    # On rafraichit à chaque tour de boucle.

    pygame.display.flip()