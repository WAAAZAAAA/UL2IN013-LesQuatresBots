# Robot.py : définition de la classe Robot
import math
import pygame

class Robot:
    def __init__(self, x:int=0, y:int=0, rot:int=0, rot_tete:int=0, capt:int=50):
        """ Initialisation du robot"""
        self.x = x
        self.y = y
        self.vitesse = 0
        self.rotation = rot # rotation du corps du robot
        self.rotation_tete = rot_tete # rotation de la tete par rapport au corps
        self.portee_capteur = capt # portee du capteur

    def avancer(self, dist:int):
        """ fait avancer le robot dans la direction de sa rotation """
        rad = math.radians(self.rotation)
        self.x += int(dist * math.cos(rad))
        self.y += int(dist * math.sin(rad))

    def tourner(self, a:int):
        """ fait tourner le robot d'un angle a """
        self.rotation = (self.rotation + a) % 360

    def get_location(self):
        """ renvoie la position et l'orientation du robot """
        return self.x, self.y, self.rotation
    
    def get_cible_capteur(self):
        """ renvoie la position regardée par le capteur en fonction de la rotation du robot et celle de sa tete """
        rotation_totale = (self.rotation + self.rotation_tete) % 360
        rad = math.radians(rotation_totale)
        cible_x:int = self.x + int(self.portee_capteur * math.cos(rad))
        cible_y:int = self.y + int(self.portee_capteur * math.sin(rad))

        return cible_x, cible_y
    
    # Fonctions graphiques pour dessiner le robot (pygame)

    def convertion(self, x:int, y:int, screen):
        """ Convertit les coordonées arbitraire en pixels sur l'écran """
        cx = screen.get_width() // 2 + int(x)
        cy = screen.get_height() // 2 - int(y) # y inversé car l'origine (0,0) est en haut a gauche
        return cx, cy

    def dessine_robot(self, screen):
        """ Fonction pour dessiner le robot sur l'écran """
        cx, cy = self.convertion(self.x, self.y, screen)
        pygame.draw.circle(screen, (0, 100, 255), (cx, cy), 10) # corps du robot

        # orientation du robot (ligne blanche)
        rad = math.radians(self.rotation)
        hx = cx + int(15 * math.cos(rad))
        hy = cy - int(15 * math.sin(rad))
        pygame.draw.line(screen, (255, 255, 255), (cx, cy), (hx, hy), 2)

        # capteur du robot (ligne rouge)
        cible_x, cible_y = self.get_cible_capteur()
        tx, ty = self.convertion(cible_x, cible_y, screen)
        pygame.draw.line(screen, (255, 0, 0), (cx, cy), (tx, ty), 1) 