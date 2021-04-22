import pygame
import sys

# to initialize ability to using pygame
pygame.init()

# size window
window_size = width, height = 800, 600

# create the screen
screen = pygame.display.set_mode(window_size)

# loop (game running)
while True:
	# 	get all event in game
	for event in pygame.event.get():
		# 		exit button pressed
		if event.type == pygame.QUIT: sys.exit()
