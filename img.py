import pygame

pygame.init()
pygame.display.set_caption("Le Babelcasino")
largeur, hauteur = 400, 400

fenetre = pygame.display.set_mode((largeur, hauteur))

fond = pygame.image.load('images/Croupier2.png').convert()
fond3 = pygame.image.load('images/enfer2.png').convert()
roulette = pygame.image.load('images/roulette2.png').convert_alpha()
roulette2 = pygame.image.load('images/roulette3.png').convert_alpha()
diable = pygame.image.load('images/Diable.png').convert_alpha()
entrer = pygame.image.load('images/Entrer-1.png').convert_alpha()
entrer2 = pygame.image.load('images/Entrer-2.png').convert_alpha()
retour = pygame.image.load('images/Retour-1.png').convert_alpha()
retour2 = pygame.image.load('images/Retour-2.png').convert_alpha()
imgpof = pygame.image.load('images/pof1.png').convert_alpha()
imgpof2 = pygame.image.load('images/pof2.png').convert_alpha()
machine_a_sous2 = pygame.image.load('images/machine_a_sous2.png').convert_alpha()
machine_a_sous1 = pygame.image.load('images/machine_a_sous1.png').convert_alpha()
face = pygame.image.load('Pile_ou_face/Piece face.png').convert_alpha()
pile = pygame.image.load('Pile_ou_face/Piece pile.png').convert_alpha()
face2 = pygame.image.load('Pile_ou_face/Piece face2.png').convert_alpha()
pile2 = pygame.image.load('Pile_ou_face/Piece pile2.png').convert_alpha()
icone = pygame.image.load('images/icone.png').convert_alpha()
paradis = pygame.image.load('images/paradis.png').convert_alpha()


pygame.display.set_icon(icone)