import sys

import pygame

# object in game
from Spaceship import Spaceship

# to initialize ability to using pygame
pygame.init()

# size window
window_size = width, height = 800, 600

# create the screen
screen = pygame.display.set_mode(window_size)

# initialize player
player = Spaceship(screen)

# loop (game running)
while True:
	screen.fill((0, 0, 0))

	# 	get all event in game
	keys = pygame.key.get_pressed()
	# left arrow pressed
	if keys[pygame.K_LEFT]:
		player.move_to_left()
	# right arrow pressed
	if keys[pygame.K_RIGHT]:
		player.move_to_right()

	for event in pygame.event.get():
		# 		exit button pressed
		if event.type == pygame.QUIT: sys.exit()

	# draw spaceship
	player.show()

	# update the screen for every change
	pygame.display.update()
