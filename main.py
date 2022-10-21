from character import Character
from maze import Collider
import pygame

pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Pac-Man")

run = True
character = Character(screen, 27, 20, 5, 20)
collider = Collider(screen)
all_colliders = [[65, 65], [325, 65], [65, 325], [325, 325]]

while run:

	pygame.time.delay(20)
	screen.fill((0, 0, 0))
	character.Draw(screen)
	for block in all_colliders:
		collider.Draw(screen,block[0], block[1])

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

	keys = pygame.key.get_pressed()

	if keys[pygame.K_LEFT]:
		character.Move('left', all_colliders)
	if keys[pygame.K_RIGHT]:
		character.Move('right', all_colliders)
	if keys[pygame.K_UP]:
		character.Move('up', all_colliders)
	if keys[pygame.K_DOWN]:
		character.Move('down', all_colliders)
	pygame.display.update()

