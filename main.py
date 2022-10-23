from turtle import heading, width
from character import Character
from maze import Maze
import pygame

WIDTH = 800
HEIGHT = 800

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pac-Man")



run = True
Maze = Maze(screen, 0, 0, 100, 100, (0,0,0),(0,0,244), 50, 50)
character = Character(screen, 7, 0, 100, 50, Maze.matrix)


while run:

		pygame.time.delay(150)
		screen.fill((255, 255, 255))
		Maze.Display(screen)
		character.Draw(screen)

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False


		keys = pygame.key.get_pressed()

		if keys[pygame.K_LEFT]:
			character.Move('left')
		if keys[pygame.K_RIGHT]:
			character.Move('right')
		if keys[pygame.K_UP]:
			character.Move('up')
		if keys[pygame.K_DOWN]:
			character.Move('down')
		
		pygame.display.update()

pygame.QUIT