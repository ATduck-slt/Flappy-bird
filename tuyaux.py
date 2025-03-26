import pyxel
import random

class Tuyau:
    LARGEUR_TUYAU = 15
    ESPACE_TUYAU = 30
    HAUTEUR = 128
    LARGEUR = 128
    VITESSE_TUYAU = 1.5

    def __init__(self, x):
        # Position initiale du tuyau en X et hauteur aléatoire
        self.x = x
        self.hauteur = random.randint(20, self.HAUTEUR - self.ESPACE_TUYAU - 20)

    def mettre_a_jour(self):
        # Déplacement du tuyau vers la gauche
        self.x -= self.VITESSE_TUYAU