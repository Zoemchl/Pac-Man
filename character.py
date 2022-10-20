import pygame
pygame.init()

class Character:
    def __init__(self, ecran, posx, posy, speed, diameter):

        self.ecran = ecran
        self.posx = posx
        self.posy = posy
        self.speed = speed
        self.diameter = diameter

    def Draw(self, ecran):
        pygame.draw.circle(ecran, (255, 255, 1),
				[self.posx, self.posy], self.diameter, 0)


