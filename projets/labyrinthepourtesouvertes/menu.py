import pygame
import traceback
from pygame.locals import *
from laby import jeu
import pickle

pygame.init()
i=16
continuer = True
selection=0

afficheChemin=False
poseCalque=True
pygame.key.set_repeat(200,200)
resolution=[4096,2160]
taillePrevue=64
nb_joysticks = pygame.joystick.get_count()
print("Il y a", nb_joysticks, "joystick(s) branché(s)")

if nb_joysticks >0:
    mon_joystick = pygame.joystick.Joystick(0)
    mon_joystick.init()

def rajoute(score,nom,scores):
    scores.append([score,nom])
    # Tri de la liste
    scores.sort()
    scores.reverse()
    return scores

def sauvegarde(scores):
    # Sauvegarde de la liste dans le même dossier dans un fichier -> parametres
    f =open('parametres', 'wb') 
    pickle.dump(scores, f) 
    f.close()

def charge() :
    # Chargement depuis le fichier parametres
    f = open('parametres', 'rb') 
    liste = pickle.load(f)
    f.close()
    # affichage
    return liste
#scores=[[222,"Léa la Génie !"]]
scores=charge()
message="test"
taillePolice=resolution[0]//40
        
try:
    fenetre=pygame.display.set_mode((resolution[0],resolution[1]), FULLSCREEN)
    pygame.display.set_caption("laby v9 16 mars 2019")
    while continuer:
        if taillePrevue>128:taillePrevue=128
        if taillePrevue<42:taillePrevue=44

        fenetre.fill((180,180,180))# ou bien une image de fond
        pygame.draw.rect(fenetre,(0,0,0),(0.02*resolution[0],resolution[1]//3,0.3*resolution[0],resolution[1]//4),0)
        pygame.draw.rect(fenetre,(255,255,0),(resolution[0]//8,resolution[1]//16,resolution[0]//5,resolution[1]//8),0)
        chaine="JOUER" 
        font=pygame.font.SysFont("broadway",taillePolice,bold=True,italic=False) 
        text=font.render(chaine,1,(0,0,0)) 
        fenetre.blit(text,(resolution[0]//8+0.05*resolution[0],resolution[1]//8-0.02*resolution[1])) 
        i+=2
        if i>254:i=16
        fontPseudo=pygame.font.SysFont("broadway",taillePolice//2,bold=False,italic=True) 
        textePseudo=font.render("Nom :",1,(0,255,255))
        fenetre.blit(textePseudo,(0.05*resolution[0],3*resolution[1]//8))
        textePseudo=font.render(message,1,(0,255,255))
        fenetre.blit(textePseudo,(0.05*resolution[0],resolution[1]//2))
	
	#taille
        pygame.draw.rect(fenetre,(255,0,0),(resolution[0]//8,15*resolution[1]//16-int((taillePrevue/128)*resolution[1]//4),resolution[0]//8,int((taillePrevue/128)*resolution[1]//4)),0)
        texte=font.render("Taille : "+str(taillePrevue),1,(255,0,0))
        fenetre.blit(texte,(resolution[0]//8,14*resolution[1]//16-int((taillePrevue/128)*resolution[1]//4)))

        
        # recuperer les scores et les afficher a coté des pseudos correspondants
        nombre=min(len(scores),5)
        for i in range (nombre):
             textePseudo=font.render(scores[i][1],1,(0,0,0))
             fenetre.blit(textePseudo,(3*resolution[0]//8,(2+i)*resolution[1]//8))
             textePseudo=font.render(str(scores[i][0]),1,(0,0,0))
             fenetre.blit(textePseudo,(6.5*resolution[0]//8,(2+i)*resolution[1]//8))
        pygame.draw.rect(fenetre,(0,0,0),(2.8*resolution[0]//8,0.2*resolution[1],4.6*resolution[0]//8,5.4*resolution[1]//8),4)
           
         
        

        if selection==1:
            pygame.draw.rect(fenetre,(0,0,0),(resolution[0]//8,resolution[1]//16,resolution[0]//5,resolution[1]//8),4)
            pygame.display.flip()
            pygame.time.delay(1000)
            score= jeu(resolution,fenetre,poseCalque,afficheChemin,taillePrevue)
            scores=rajoute(score,message,scores)
            selection=0
            pygame.key.set_repeat(200,200)

        for event in pygame.event.get():   
            if event.type==QUIT:
                continuer=False
            
            elif event.type==MOUSEBUTTONUP :
                xmouse,ymouse=event.pos
                if resolution[0]//8 <= xmouse <resolution[0]//8+resolution[0]//4 and resolution[1]//16 <= ymouse <resolution[1]//16 + resolution[1]//8 :
                    #return la fonction qui génère le labyrinthe
                    selection=1
                    
            elif event.type==JOYBUTTONDOWN :
                if event.button == 0 :
                    selection=1
                elif event.button == 3 :
                    taillePrevue+=4
                elif event.button == 1 :
                    taillePrevue-=4
                
            elif event.type==KEYDOWN:   
                if event.key==K_ESCAPE:
                    continuer =False
                elif event.key==K_UP:
                    taillePrevue+=4
                elif event.key==K_DOWN:
                    taillePrevue-=4
                elif event.key==K_BACKSPACE:
                    message=message[:-1]
                elif event.key==K_RETURN: 
                    selection=1
                elif len(message)<24: 
                    message+=event.dict['unicode']
        pygame.display.flip()

finally:
    pygame.quit()
    sauvegarde(scores)
