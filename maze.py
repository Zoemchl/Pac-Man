import pygame
from pygame.locals import *

class Maze:

    def __init__(self, ecran, posx, posy, size_width, size_height, color1, color2, pacx, pacy):

        self.ecran = ecran
        self.posx = posx
        self.posy = posy
        self.pacx = pacx
        self.pacy = pacy
        self.color1 = color1
        self.color2 = color2
        self.matrix = [ 
        [1, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 1, 1, 0],
        [0, 1, 1, 1, 0, 1, 0, 0],
        [0, 0, 1, 1, 0, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 1, 1, 0, 0, 1, 1],
        [0, 0, 0, 1, 1, 0, 1, 0],
        [1, 1, 0, 1, 0, 0, 0, 0],]
        self.size_width = size_width  
        self.size_height = size_height

        

    def Display(self, ecran):
        self.posy = 0
        self.pacy = 50
        for row in self.matrix:
            self.posx = 0
            self.pacx = 50
            for item in row:
                if item == 0:
                    pygame.draw.rect(ecran, self.color1, [self.posx, self.posy, self.size_width, self.size_height ])
                    pygame.draw.circle(ecran, (255, 255, 255),[self.pacx, self.pacy], 10, 0)
                else:
                    pygame.draw.rect(ecran, self.color2, [self.posx, self.posy, self.size_width, self.size_height ])
                self.posx += self.size_width
                self.pacx += self.size_width
            self.posy += self.size_height
            self.pacy += self.size_height
        pygame.display.update()
