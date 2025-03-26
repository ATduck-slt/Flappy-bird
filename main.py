import pyxel
import random
from oiseau import Oiseau
from tuyaux import Tuyau
from record import Record

class JeuFlappyBird:
    LARGEUR = 128
    HAUTEUR = 128
    
    def __init__(self):
        # Initialisation de la fenêtre Pyxel et chargement des ressources
        pyxel.init(self.LARGEUR, self.HAUTEUR, title="Flappy Bird")
        pyxel.load("my_resource.pyxres")
        pyxel.playm(0, 1, True)
        
        self.reinitialiser()
        
        # Lancement de la boucle de jeu
        pyxel.run(self.mettre_a_jour, self.dessiner)  

    def reinitialiser(self):
        # Réinitialisation des variables du jeu
        self.oiseau = Oiseau()
        self.tuyaux = [Tuyau(self.LARGEUR)]
        self.meilleur_score = Record()
        self.score = 0
        self.fin_du_jeu = False
        self.scroll_x = 0 

    def mettre_a_jour(self):
        
        if self.fin_du_jeu:
            # Redémarrer le jeu si la touche espace est pressée
            if pyxel.btnp(pyxel.KEY_SPACE):  
                self.reinitialiser()
            return
        
        # Défilement de l'écran
        self.scroll_x = (self.scroll_x + 1) % 128 

        # Gestion du saut de l'oiseau
        if pyxel.btnp(pyxel.KEY_SPACE):  
            self.oiseau.sauter()

        self.oiseau.mettre_a_jour()
        
        # Mise à jour des tuyaux
        for tuyau in self.tuyaux:
            tuyau.mettre_a_jour()

        # Suppression des tuyaux hors écran et ajout de nouveaux
        if self.tuyaux[0].x < -Tuyau.LARGEUR_TUYAU:
            self.tuyaux.pop(0)
            self.tuyaux.append(Tuyau(self.LARGEUR))
            self.score += 1
        
        # Vérification des collisions
        if self.oiseau.collision(self.tuyaux):
            self.fin_du_jeu = True
            

    def dessiner(self):
        pyxel.cls(5)
        pyxel.camera()
        
        # Animation de l'arrière plan
        pyxel.bltm(0, 0, 0, (self.scroll_x //4) % 128, 128, 128, 128)
        
        # Animation de l'oiseau
        coef = pyxel.frame_count //3% 2
        pyxel.blt(self.oiseau.OISEAU_X,
                self.oiseau.y,
                self.oiseau.IMG,
                self.oiseau.U,
                self.oiseau.V + 8*coef,
                self.oiseau.WIDTH,
                self.oiseau.HEIGHT,
                0) 
        
        # Dessin des tuyaux
        for tuyau in self.tuyaux:
            pyxel.rect(tuyau.x, 0, Tuyau.LARGEUR_TUYAU, tuyau.hauteur, 3)
            pyxel.rect(tuyau.x,
                       tuyau.hauteur + Tuyau.ESPACE_TUYAU,
                       Tuyau.LARGEUR_TUYAU,
                       self.HAUTEUR - tuyau.hauteur - Tuyau.ESPACE_TUYAU, 3)
            # Nous avons tenté de donner un graphique au tuyau, mais n'avons pas réussi. Voici notre essai.
            '''pyxel.blt(self.tuyaux.x,
                      0,
                      self.tuyaux.IMG,
                      16,
                      16,
                      self.tuyaux.WIDTH,
                      self.tuyaux.HEIGHT,
                      0)
            pyxel.blt(self.tuyaux.x,
                      self.tuyaux.HEIGHT + self.tuyaux.ESPACE_TUYAU,
                      self.tuyaux.IMG,
                      24,
                      24,
                      self.tuyaux.WIDTH,
                      self.HAUTEUR - self.tuyaux.HEIGHT - self.tuyaux.ESPACE_TUYAU,
                      0)'''
        
        # Affichage du score
        pyxel.text(5, 5, f"Score: {self.score}", 0)
        pyxel.text(4, 4, f"Score: {self.score}", 10)
        
        # Affichage "Game over"
        if self.fin_du_jeu:
            pyxel.text(self.LARGEUR // 2 - 20, self.HAUTEUR // 2, "GAME OVER", 0)
            pyxel.text(self.LARGEUR // 2 - 20, self.HAUTEUR // 2.03, "GAME OVER", 8)
            pyxel.text(self.LARGEUR // 2 - 45, self.HAUTEUR // 1.5, "Press space to continue", 0)
            pyxel.text(self.LARGEUR // 2 - 45, self.HAUTEUR // 1.53, "Press space to continue", 7)
            # Nous avons tenté de donner le record en fin de partie, mais n'avons pas réussi. Voici notre essai.
            '''pyxel.text(self.LARGEUR // 2 - 30, self.HAUTEUR // 2 + 10, f"Record: {self.meilleur_score}", 8)'''

JeuFlappyBird()
