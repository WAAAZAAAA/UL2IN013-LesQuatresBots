# Robot.py : définition de la classe Robot
import math

class Robot:
    def __init__(self, x:float=0.0, y:float=0.0, rot:int=0):
        """ position x,y du robot et sa rotation en degrés """
        self.x = x
        self.y = y
        self.rotation = rot

    def avancer(self, dist:float):
        """ fait avancer le robot dans la direction de sa rotation """
        rad = math.radians(self.rotation)
        self.x += dist * math.cos(rad)
        self.y += dist * math.sin(rad)

        # arrondir pour nettoyer les micro-erreurs de calcul sur flottant
        self.x = round(self.x, 4)
        self.y = round(self.y, 4)

    def tourner(self, a:int):
        """ fait tourner le robot d'un angle a """
        self.rotation = (self.rotation + a) % 360

    def get_location(self):
        """ renvoie la position et l'orientation du robot """
        return self.x, self.y, self.rotation