import pygame
from fonctions import dessiner_zone_texte, dessiner_bouton
from objets_et_variables import *
from img import *
from Roulette_Russe import pistolet
from PileouFace import pileouface
from sons import *
import sys

pygame.mixer.init()

class Ecran:
    def __init__(self, actif=False):
        self.actif = actif

    def get_actif(self):
        return self.actif

    def set_actif(self, actif):
        self.actif = actif

class Ecran1:
    def __init__(self):
        self.ecran = Ecran(True)
        self.ancien_pseudo = joueur1.get_pseudo()
    def affiche(self):
        if self.ecran.get_actif():
            if joueur1.get_pseudo() == 'Fredou':
                if not pygame.mixer.music.get_busy() or self.ancien_pseudo != joueur1.get_pseudo():
                    pygame.mixer.music.unload()
                    pygame.mixer.music.load(son_champignon)
                    pygame.mixer.music.set_volume(0.1)
                    pygame.mixer.music.play(-1)
                    self.ancien_pseudo = joueur1.get_pseudo()
            else:
                if not pygame.mixer.music.get_busy() or self.ancien_pseudo != joueur1.get_pseudo():
                    pygame.mixer.music.unload()
                    pygame.mixer.music.load(musique_de_fond)
                    pygame.mixer.music.set_volume(0.3)  # Volume pour la musique de fond générale
                    pygame.mixer.music.play(-1)
                    self.ancien_pseudo = joueur1.get_pseudo()
            fenetre.blit(fond, (0, 0))
            if bouton1.get_x() <= pygame.mouse.get_pos()[0] <= bouton1.get_x() + bouton1.get_largeur() and bouton1.get_y() <= pygame.mouse.get_pos()[1] <= bouton1.get_y() + bouton1.get_hauteur():
                fenetre.blit(entrer2, (105, 230))
            else:
                fenetre.blit(entrer, (105, 230))


class Ecran2:
    def __init__(self):
        self.ecran = Ecran()
        self.fond = pygame.image.load('images/casino.jpg').convert()
        self.musique = False
    def set_musique(self):
        self.musique = False
    def affiche(self):
        '''
        Permet d'afficher l'écran principal et de gérer l'animation des boutons et mettre à jour les animations des jeux.
        '''
        if joueur1.get_pseudo() == 'Fredou':
            self.fond = pygame.image.load('images/coeurfredou.png').convert()
        else:
            self.fond = pygame.image.load('images/casino.jpg').convert()
        if joueur1.get_pseudo() == 'Mr.Maurice' or joueur1.get_pseudo() == 'Mr Maurice' or joueur1.get_pseudo() == 'Maurice':
            joueur1.set_pseudo('Le meilleur')  #Mettez nous des tickets et un 20/20 svp
        fenetre.blit(self.fond, (0, 0))
        coin.activer_rotation()
        if ecran2.ecran.get_actif() and 330 <= pygame.mouse.get_pos()[0] <= 390 and 45 <= pygame.mouse.get_pos()[1] <= 75 :
            fenetre.blit(roulette2, (320, 20))
        else:
            fenetre.blit(roulette, (320, 20))
        if bouton1.get_x() <= pygame.mouse.get_pos()[0] <= bouton1.get_x() + bouton1.get_largeur() and bouton1.get_y() <= pygame.mouse.get_pos()[1] <= bouton1.get_y() + bouton1.get_hauteur():
            fenetre.blit(retour2, (105, 230))
        else:
            fenetre.blit(retour, (105, 230))
        dessiner_bouton(fenetre, joueur1.get_pseudo(), bouton2.get_x(), bouton2.get_y(), bouton2.get_largeur(), bouton2.get_hauteur(), blanc, noir, 20)
        dessiner_bouton(fenetre, f"Solde : {joueur1.get_cagnotte()}", bouton3.get_x(), bouton3.get_y(), bouton3.get_largeur(), bouton3.get_hauteur(), blanc, noir, 25)
        if 330 <= pygame.mouse.get_pos()[0] <= 390 and 170 <= pygame.mouse.get_pos()[1] <= 220 :
            fenetre.blit(machine_a_sous2, (320, 160))
        else:
            fenetre.blit(machine_a_sous1, (320, 160))
        if 330 <= pygame.mouse.get_pos()[0] <= 390 and 100 <= pygame.mouse.get_pos()[1] <= 150 :
            fenetre.blit(imgpof2, (320, 90))
        else:
            fenetre.blit(imgpof, (320, 90))
        # Affichage des boutons des choix du pile ou face
        if pileouface.get_actif():
            fenetre.blit(face2, (125, 230))
            fenetre.blit(pile2, (230, 230))
                

        fenetre.blit(coin.get_image(),coin.get_pos())
        coin.update(0.04)

        fenetre.blit(pistolet.get_image(),pistolet.get_pos())
        pistolet.update_def(0.16,joueur1)  
        pistolet.update_vict(0.16,joueur1)  

        fenetre.blit(pileouface.get_image(),(170,140))
        if pileouface.get_actif():
            pileouface.update(0.20, joueur1)

        if joueur1.get_pseudo() == '666' or joueur1.get_pseudo() == 'Satan':
            fenetre.blit(diable, (100, 2))
    

class EcranMort:
    def __init__(self):
        self.ecran = Ecran()
        self.fond =  pygame.image.load('images/enfer2.png').convert()
    def affiche(self):
        '''
        Permet d'afficher l'écran de mort.
        '''
        fenetre.blit(self.fond, (0, 0))

class EcranVictoire:
    def __init__(self):
        self.ecran = Ecran()
        self.retour1 = pygame.image.load('images/Retour-1.png').convert_alpha()
        self.retour2 = pygame.image.load('images/Retour-2.png').convert_alpha()
    def affiche(self):
        '''
        Permet d'afficher l'écran de victoire.
        '''
        fenetre.blit(paradis, (0, 0))
        if bouton1.get_x() <= pygame.mouse.get_pos()[0] <= bouton1.get_x() + bouton1.get_largeur() and bouton1.get_y() <= pygame.mouse.get_pos()[1] <= bouton1.get_y() + bouton1.get_hauteur():
            fenetre.blit(self.retour2, (105, 230))
        else:
            fenetre.blit(self.retour1, (105, 230))

ecran1 = Ecran1()
ecran2 = Ecran2()
ecran_mort = EcranMort()
ecran_victoire = EcranVictoire()