import pygame


class Spaceship:

	def __init__(self, screen):
		self.__playerImg = pygame.image.load('./assets/spaceship64.png')
		self.__playerX = 368
		self.__playerY = 500
		self.screen = screen

	# show player
	def show(self):
		self.screen.blit(self.__playerImg, (self.__playerX, self.__playerY))
