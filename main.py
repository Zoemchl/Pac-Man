from character import Character
import pygame

pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Pac-Man")

run = True
character = Character(screen, 100, 100, 5, 20)
while run:

	pygame.time.delay(20)
	screen.fill((0, 0, 0))
	character.Draw(screen)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

	keys = pygame.key.get_pressed()

	if keys[pygame.K_LEFT] and character.posx > character.speed:
		if character.posx > 25 :
			character.posx -= character.speed 
	if keys[pygame.K_RIGHT] and character.posx < 600 - character.diameter - character.speed:
		character.posx += character.speed
	if keys[pygame.K_UP] and character.posy > character.speed:
		if character.posy > 25 :
			character.posy -= character.speed
	if keys[pygame.K_DOWN] and character.posy < 600 - character.diameter - character.speed:
		character.posy += character.speed

	# if event.type == pygame.KEYDOWN:
	# 	if event.key == pygame.K_RIGHT:
	# 		character.posx += 10
	# 	if event.key == pygame.K_LEFT:
	# 		character.posx += -10
	# 	if event.key == pygame.K_UP:
	# 		character.posy += -10
	# 	if event.key == pygame.K_DOWN:
	# 		character.posy += 10

	pygame.display.update()

