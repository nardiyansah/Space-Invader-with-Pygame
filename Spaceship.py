import pygame

from Bullet import Bullet


class Spaceship:
	movementSpeed = 2.3
	spaceship_images = ['./assets/spaceship_1.png', './assets/spaceship_2.png', './assets/spaceship_3.png']

	def __init__(self, screen):
		self.__playerImg = pygame.image.load(self.spaceship_images[0])
		self.__playerX = 368
		self.__playerY = 500
		self.__heart = 3
		self.__level = 0
		self.screen = screen

	# show player
	def show(self):
		self.screen.blit(self.__playerImg, (self.__playerX, self.__playerY))

	def move_to_right(self):
		if self.__playerX + self.movementSpeed < 738:
			self.__playerX += self.movementSpeed

	def move_to_left(self):
		if self.__playerX - self.movementSpeed > 0:
			self.__playerX -= self.movementSpeed

	def getX(self):
		return self.__playerX

	def getY(self):
		return self.__playerY

	def getHeart(self):
		return self.__heart

	def level_up(self):
		if self.__level < 2:
			self.__level += 1
			self.__playerImg = pygame.image.load(self.spaceship_images[self.__level])

	def reset_level(self):
		self.__level = 0
		self.__playerImg = pygame.image.load(self.spaceship_images[self.__level])

	def shoot(self):
		return Bullet(self.screen, self.__playerX + 24, self.__playerY, self.__level)

	def lose_one_heart(self):
		self.__heart -= 1

