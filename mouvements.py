# Mouvements.py : mouvements programmés pour le robot

def carre(robot, cote:int):
    """ fait faire un carré au robot, yield a chaque etape pour laisser la main a pygame
    cote: longueur des cotés du carré
    """
    for _ in range(4):
        distance = 0
        while distance < cote:
            robot.avancer(1)
            distance += 1
            yield # attend que main lance la prochaine etape

        for _ in range(45):
            robot.tourner(2)
            yield # idem