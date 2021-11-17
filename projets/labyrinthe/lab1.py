import pygame
from pygame.locals import *

pygame.init()

fenetre = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Amusons-nous avec Mario!")
pygame.key.set_repeat(50, 10)

persoG = pygame.image.load("mario_left.png").convert_alpha()
persoG = pygame.transform.scale(persoG, (42, 42))
persoD = pygame.transform.flip(persoG, True, False)
persorect = persoG.get_rect()

orientation = "gauche"

fond = pygame.image.load("sand.jpg").convert()

carte = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

obstacles = []


def update(carte):
    obstacles = []
    for ligne in range(12):
        for colonne in range(16):
            if carte[ligne][colonne] == 1:
                obstacles.append(pygame.Rect(colonne * 50, ligne * 50, 50, 50))
    return obstacles


obstacles = update(carte)


def bords():
    return [[1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
            [1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1]]


continuer = True
try:
    persorect.left = 200
    persorect.top = 200
    while continuer:
        fenetre.blit(fond, (0, 0))
        for rectangle in obstacles:
            pygame.draw.rect(fenetre, (0, 255, 255), rectangle, 0)
        if orientation == "gauche":
            fenetre.blit(persoG, persorect)
        else:
            fenetre.blit(persoD, persorect)

        pygame.display.flip()

        # gestion des événements
        for event in pygame.event.get():
            if event.type == QUIT:
                continuer = 0
            elif event.type == KEYDOWN:  # appui sur une touche
                if event.key == K_ESCAPE:
                    print("touche Escape")
                    continuer = 0
                elif event.key == K_LEFT:
                    print("touche Gauche")
                    orientation = "gauche"
                    persorect.left -= 5
                    if persorect.left < -100: persorect.left = 800
                    for obstacle in obstacles:
                        if persorect.colliderect(obstacle):
                            persorect.left = obstacle.right
                elif event.key == K_RIGHT:
                    print("touche Droite")
                    orientation = "droite"
                    persorect.left += 5
                    if persorect.right > 900: persorect.right = -100
                    for obstacle in obstacles:
                        if persorect.colliderect(obstacle):
                            persorect.right = obstacle.left
                elif event.key == K_UP:
                    print("touche Haut")
                    persorect.top -= 5
                    if persorect.bottom < -100: persorect.top = 600
                    for obstacle in obstacles:
                        if persorect.colliderect(obstacle):
                            persorect.top = obstacle.bottom
                elif event.key == K_DOWN:
                    print("touche Bas")
                    persorect.bottom += 5
                    if persorect.top > 700: persorect.bottom = 100
                    for obstacle in obstacles:
                        if persorect.colliderect(obstacle):
                            persorect.bottom = obstacle.top
                elif event.key == K_p:
                    print("capture d'écran")
                    pygame.image.save(fenetre, "mario.png")

                elif event.key == K_c:
                    carte = bords()
                    obstacles = update(carte)
                else:
                    print("autre touche")
            elif event.type == MOUSEBUTTONUP:
                xmouse, ymouse = event.pos
                colonne = xmouse // 50
                ligne = ymouse // 50
                carte[ligne][colonne] = 1 - carte[ligne][colonne]
                obstacles = update(carte)


finally:

    pygame.quit()