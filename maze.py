import pygame
from pygame.locals import *
pygame.init()

class Collider:
    def __init__(self, ecran):

        self.ecran = ecran

    def Draw(self, ecran, posx, posy):
					pygame.draw.rect(ecran, (0,   255,   0),
					Rect(posx, posy, 200, 200))
