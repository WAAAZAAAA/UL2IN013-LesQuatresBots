# Main.py : programme principal pour controler le robot
from robot import Robot
from mouvements import carre

def main():
    robot = Robot(0, 0, 0)
    carre(robot, 20)

    for _ in range(4):
        robot.tourner(90)
        print("capteur: ", robot.get_cible_capteur())

main()