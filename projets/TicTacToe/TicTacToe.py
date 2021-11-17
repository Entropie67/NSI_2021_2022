import pygame as py
from pygame.locals import *
import os

# https://www.pygame.org/docs/
# Initialisation de Pygame
py.init()
clock = py.time.Clock()

TAILLE = (600, 600)
SILVER = (192, 192, 192)
BLANC = (255, 255, 255)
NOIR = (0, 0, 0)

# création d'une fenêtre
fenetre = py.display.set_mode(TAILLE, RESIZABLE)
py.display.set_caption("Tic-Tac-Toe")
#py.display.set_icon(image)

# création d'un fond de la taille de la fenêtre
background = py.Surface(fenetre.get_size())
background.fill(SILVER)
fenetre.blit(background, (0, 0))
n = TAILLE[0] / 3
liste_rect = [[0] * 3 for i in range(3)]
for i in range(3):
    py.draw.line(fenetre, (0, 0, 255), (i*n, 0), (i *n,  TAILLE[0]), 5)
    for j in range(3):
        rect = py.Rect((j * n, i * n, n, n))
        liste_rect[i][j] = [rect, 0]
        py.draw.rect(fenetre, BLANC, rect)
        py.draw.line(fenetre, (255, 0, 0), (j * n, i * n), (j*n + TAILLE[0], i*n ), 5)

print(liste_rect)

loop = True
compteur = 0
while loop:
    for event in py.event.get():
        if event.type == py.QUIT:
            loop = False
        if event.type == py.MOUSEBUTTONDOWN:
            # left, middle, right = pygame.mouse.get_pressed()
            mouse_xy = py.mouse.get_pos()
            ligne = int(mouse_xy[1] // n)
            colonne = int(mouse_xy[0] // n)
            print(f" Ligne {ligne} et Colonne {colonne}")
            if compteur % 2:
                color = NOIR
            else:
                color = SILVER
            if liste_rect[ligne][colonne][1] == 0:
                py.draw.rect(fenetre, color, liste_rect[ligne][colonne][0])
                liste_rect[ligne][colonne][1] = color
                compteur += 1
                print(liste_rect[ligne][colonne])
                print(mouse_xy)


    # Rafraichissement de l'écran
    py.display.flip()
    clock.tick(10)

#os.system("PAUSE")