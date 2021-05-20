import math
import random

import pygame


class Alien:
    movementSpeed = 1.8

    def __init__(self, screen):
        self.__alienImg = pygame.image.load('./assets/ufo64.png')
        self.__alienX = random.randint(20, 710)
        self.__alienY = random.randint(-500, 0)
        self.screen = screen

    def hit_spaceship(self, spaceshipX, spaceshipY):
        distance = math.sqrt(
            pow(self.__alienX - spaceshipX, 2) + pow(self.__alienY - spaceshipY, 2))
        return distance < 55

    def show(self):
        self.screen.blit(self.__alienImg, (self.__alienX, self.__alienY))

    def move(self):
        self.__alienY += self.movementSpeed

    def getX(self):
        return self.__alienX

    def getY(self):
        return self.__alienY
