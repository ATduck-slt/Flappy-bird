import pyxel

class Oiseau:
    IMG = 0
    U = 0
    V = 16
    WIDTH = 8
    HEIGHT = 8
    GRAVITE = 0.3
    SAUT = -3
    OISEAU_X = 15
    OISEAU_RAYON = 4
    HAUTEUR = 128

    def __init__(self):
        # Position initiale de l'oiseau
        self.y = self.HAUTEUR // 2
        self.vitesse = 0

    def sauter(self):
        # Applique une impulsion vers le haut lorsque l'oiseau saute
        self.vitesse = self.SAUT

    def mettre_a_jour(self):
        # Applique la gravité et met à jour la position verticale de l'oiseau
        self.vitesse += self.GRAVITE
        self.y += self.vitesse
        
    def collision(self, tuyaux):
        # Vérifie les collisions avec les tuyaux
        for tuyau in tuyaux:
            if (self.OISEAU_X + self.OISEAU_RAYON > tuyau.x and self.OISEAU_X - self.OISEAU_RAYON < tuyau.x + tuyau.LARGEUR_TUYAU and
                (self.y - self.OISEAU_RAYON < tuyau.hauteur or self.y + self.OISEAU_RAYON > tuyau.hauteur + tuyau.ESPACE_TUYAU)):
                return True
        # Vérifie si l'oiseau touche le sol ou dépasse le haut de l'écran
        return self.y < 0 or self.y > self.HAUTEUR
