import pygame
from pygame.locals import *

class Maze:

    def __init__(self, ecran, posx, posy, size_width, size_height, color1, color2):

        self.ecran = ecran
        self.posx = posx
        self.posy = posy
        self.color1 = color1
        self.matrix = [ 
        [0, 0, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 0, 1, 0, 0, 1],
        [1, 0, 0, 0, 1, 0, 1, 1],
        [1, 1, 0, 0, 1, 0, 0, 0],
        [0, 1, 1, 1, 1, 1, 1, 1],
        [0, 1, 0, 0, 1, 1, 0, 0],
        [1, 1, 1, 0, 0, 1, 0, 1],
        [0, 0, 1, 0, 1, 1, 1, 1],]

        

    def Display(self, ecran):
        self.posy = 0
        for row in self.matrix:
            self.posx = 0
            for item in row:
                if item == 0:
                    pygame.draw.rect(ecran, self.color1, [self.posx, self.posy, self.size_width, self.size_height ])
                else:
                    pygame.draw.rect(ecran, self.color2, [self.posx, self.posy, self.size_width, self.size_height ])

                self.posx += self.size_width
            self.posy += self.size_height
        pygame.display.update()