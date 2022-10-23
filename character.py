from maze import Maze
import pygame

class Character:
    def __init__(self, ecran, posx, posy, speed, diameter, matrix):

        self.ecran = ecran
        self.posx = posx
        self.posy = posy
        self.speed = speed
        self.diameter = diameter
        self.matrix = matrix

    def Draw(self, ecran):
        pygame.draw.circle(ecran, (255, 255, 1),

				[(self.posx*self.speed)+self.diameter, (self.posy*self.speed)+self.diameter], self.diameter, 0)

    def Move(self, direction):

        if (direction == 'left'):
            if self.posx > 0:
                if self.matrix[self.posy][self.posx - 1] != 1: 
                    self.posx -= 1
        if (direction == 'right'):
            if self.posx < 7:
                if self.matrix[self.posy][self.posx + 1] != 1: 
                    self.posx += 1
        if (direction == 'up'):
            if self.posy > 0:
                if self.matrix[self.posy - 1][self.posx] != 1: 
                    self.posy -= 1
        if (direction == 'down'):
            if self.posy < 7:
                if self.matrix[self.posy + 1][self.posx] != 1: 
                    self.posy += 1