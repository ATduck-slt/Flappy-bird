import pyxel

class Record:
    def __init__(self):
        self.meilleur_score = 0

    def mettre_a_jour(self, score):
        # Mis à jour du record
        if score > self.meilleur_score:
            self.meilleur_score = score

    def afficher(self):
        # Affichage du record
        str(f"Record: {self.meilleur_score}")
            
            