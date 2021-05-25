import pygame


class Bullet:
	movementSpeed = 3.2
	bullet_images = ['./assets/bullet_1.png', './assets/bullet_2.png', './assets/bullet_3.png']

	def __init__(self, screen, X, Y, level):
		self.__bulletImg = pygame.image.load(self.bullet_images[level])
		self.__bulletX = X
		self.__bulletY = Y
		self.screen = screen

	def move(self):
		self.__bulletY -= self.movementSpeed

	def show(self):
		self.screen.blit(self.__bulletImg, (self.__bulletX, self.__bulletY))

	def getX(self):
		return self.__bulletX

	def getY(self):
		return self.__bulletY
