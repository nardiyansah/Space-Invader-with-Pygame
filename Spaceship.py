import pygame


class Spaceship:
	movementSpeed = 0.1

	def __init__(self, screen):
		self.__playerImg = pygame.image.load('./assets/spaceship64.png')
		self.__playerX = 368
		self.__playerY = 500
		self.screen = screen

	# show player
	def show(self):
		self.screen.blit(self.__playerImg, (self.__playerX, self.__playerY))

	def move_to_right(self):
		self.__playerX += self.movementSpeed

	def move_to_left(self):
		self.__playerX -= self.movementSpeed
