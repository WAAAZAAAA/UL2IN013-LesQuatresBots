# Main.py : programme principal pour controler le robot
from robot import Robot
from mouvements import carre

def main():
    robot = Robot(0, 0, 0)
    carre(robot, 20)

main()