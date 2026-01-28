# Main.py : programme principal reliant les autres entre eux
import pygame
from robot import Robot
from mouvements import carre

""" Constantes """
LARGEUR, HAUTEUR = 800, 600 # taille de la fenetre en pixels
FPS = 60 # images par seconde (augmenter cette valeur rend l'animation plus fluide mais l'accelere)

robot = Robot(x=0, y=0, rot=0) # creation du robot
mouvement_carre = carre(robot, cote=100) # animation carree de cotes de 100 pixels

def main():
    """ Initialisations pygame """
    pygame.init() # initialisation de pygame
    screen = pygame.display.set_mode((LARGEUR, HAUTEUR)) # taille de la fenetre
    pygame.display.set_caption("Simulation robot") # titre de la fenetre
    clock = pygame.time.Clock() # clock de pygame

    """ Main loop """
    execution = True # fenetre en cours d'execution
    while execution:
        """ Gestion des evenements """
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # fermeture de la fenetre
                execution = False

        """ Mise à jour de la position/rotation du robot (modifie les attributs du robot) """
        try:
            next(mouvement_carre) # lance la prochaine etape du mouvement
        except StopIteration: # le carre est termine
            pass # rien faire

        """ Rendu graphique """
        screen.fill((200, 200, 200)) # 1 - rempli l'ecran de gris (mettez en commentaire cette ligne si vous voulez rire)
        robot.dessine_robot(screen) # 2 - dessine le robot a sa position/rotation actuelle
        pygame.display.flip() # 3 - met a jour l'ecran

        clock.tick(FPS) # x images par seconde

    pygame.quit()

main()