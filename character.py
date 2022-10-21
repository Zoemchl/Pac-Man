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

    def Move(self, direction, allColliders):
        if (direction == 'left'):
            if self.posx >= self.diameter/2:
                for collider in allColliders:
                    if self.posx > collider[0] and ((self.posx - self.diameter/2 - 5) - self.speed) <=(collider[0] + 200):
                        if self.posy >= collider[1] and self.posy <= collider[1]+200:
                            return
            else:
                return
            self.posx -= self.speed

        if (direction == 'right'):
            if self.posx <= 600 - self.diameter/2:
                for collider in allColliders:
                    if self.posx < (collider[0] + 200) and ((self.posx + self.diameter/2 + 5) + self.speed) >=(collider[0]):
                        if self.posy >= collider[1] and self.posy <= collider[1]+200:
                            return
            else:
                return
                
            self.posx += self.speed

        if (direction == 'up'):
            if self.posy >= self.diameter/2:
                for collider in allColliders:
                    if self.posy > collider[1] and ((self.posy - self.diameter/2 - 5) - self.speed) <=(collider[1] + 200):
                        if self.posx >= collider[0] and self.posx <= collider[0]+200:
                            return
            else:
                return
            self.posy -= self.speed
        
        if (direction == 'down'):
            if self.posy <= 600 - self.diameter/2:
                for collider in allColliders:
                    if self.posy < (collider[1] + 200) and ((self.posy + self.diameter/2 + 5) + self.speed) >=(collider[1]):
                        if self.posx >= collider[0] and self.posx <= collider[0]+200:
                            return
            else:
                return
                
            self.posy += self.speed
