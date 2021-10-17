import pygame
from pygame.locals import *


# Initialisation de Pygame
pygame.init()
# création d'une fenête de 640 sur 480
fenetre = pygame.display.set_mode((640, 480))
# Titre de la fenêtre :
pygame.display.set_caption("Mon jeu")
# Initialisation d'une horloge.
# Utile pour gérer la fréquence d'images en jeu
clock = pygame.time.Clock()


continuer = True

# un rectangle que nous déplacerons ...
hitbox = pygame.Rect(80, 120, 40, 40)
# ... à l'aide de ce vecteur
vecteur = [10, 10]

imageG = pygame.image.load("mario_left.png").convert_alpha()
imageD = pygame.transform.flip(imageG, True, False)
joueurRect = imageG.get_rect()  # rectangle de même taille que l'image
joueurRect.centerx = 400
joueurRect.centery = 300
position = "gauche"

while continuer:
    # déplcement du rectangle
    hitbox.move_ip(vecteur)

    # collision avec un mur ?
    if hitbox.right > 640 or hitbox.left < 0:
        vecteur[0] *= -1
    if hitbox.bottom > 480 or hitbox.top < 0:
        vecteur[1] *= -1

    if joueurRect.right < 0:
        joueurRect.left = 640
    elif joueurRect.left > 640:
        joueurRect.right = 0
    if joueurRect.bottom < 0:
        joueurRect.top = 480
    elif joueurRect.top > 480:
        joueurRect.bottom = 0

    if joueurRect.colliderect(hitbox):
        vecteur[0] *= -1
        vecteur[1] *= -1

    # le fond
    fenetre.fill((0, 160, 160))

    if position == "gauche":
        fenetre.blit(imageG, joueurRect)
    else:
        fenetre.blit(imageD, joueurRect)

    # dessiner le cercle
    x, y = hitbox.centerx, hitbox.centery
    pygame.draw.circle(fenetre, (255, 255, 255), (x, y), 20, 1)

    # mettre à jour l'affichage
    pygame.display.flip()

    # 25 images par seconde
    clock.tick(25)

    # gestion des événements non clavier
    for event in pygame.event.get():

        if event.type == QUIT:  # la croix en haut à gauche
            continuer = False

        elif event.type == MOUSEBUTTONUP:  # clic de souris
            hitbox.centerx, hitbox.centery = event.pos

    # touches pressées dans une liste
    tkey = pygame.key.get_pressed()

    if tkey[K_UP]:
        joueurRect.move_ip(0, -5)
    if tkey[K_DOWN]:
        joueurRect.move_ip(0, 5)
    if tkey[K_LEFT]:
        joueurRect.move_ip(-5, 0)
        position = "gauche"
    if tkey[K_RIGHT]:
        joueurRect.move_ip(5, 0)
        position = "droite"
    if tkey[K_ESCAPE]:
        continuer = False

pygame.quit()