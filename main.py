import math
import sys

import pygame
import pygame_menu

# object in game
from Alien import Alien
from Bonus import Bonus
from Spaceship import Spaceship

# STATE
STATE_MENU = "MENU"
IN_GAME = "PLAYING"
GAME_OVER = "GAME OVER"
STATE = STATE_MENU

# to initialize ability to using pygame
pygame.init()

# size window
window_size = width, height = 800, 600

# create the screen
screen = pygame.display.set_mode(window_size)

# background
background = pygame.image.load('./assets/background.png')

heartX = 10
heartY = 45

# initialize score
score = 0
font = pygame.font.Font('freesansbold.ttf', 28)
scoreX, scoreY = 10, 10

# initialize n enemies
n_enemies = 6
enemyList = []
for i in range(n_enemies):
	enemyList.append(Alien(screen))
# initialize n bonus
n_bonus = 3
bonusList = []
for i in range(n_bonus):
	bonusList.append(Bonus(screen))
# bullet list
bulletList = []


def isCollision(alienList=[], bulletList=[]):
	for alien in alienList:
		for bullet in bulletList:
			distance = math.sqrt(pow((alien.getX() - bullet.getX()), 2) + pow((alien.getY() - bullet.getY()), 2))
			if distance < 46:
				bulletList.remove(bullet)
				alienList.remove(alien)
				alienList.append(Alien(screen))
				return True
	return False


def show_score(x, y):
	scoreFont = font.render("Score : " + str(score), True, (255, 255, 255))
	screen.blit(scoreFont, (x, y))


def show_heart(heart, x, y):
	heartFont = font.render("Life : " + str(heart), True, (255, 255, 255))
	screen.blit(heartFont, (x, y))


def game_over():
	game_over_font = pygame.font.Font('freesansbold.ttf', 48)
	game_over_text = game_over_font.render("GAME OVER", True, (255, 255, 255))
	screen.blit(game_over_text, (220, 250))


def start():
	global STATE
	STATE = IN_GAME
	global score
	score = 0
	bonus = 0
	# initialize player
	player = Spaceship(screen)

	# loop (game running)
	while True:
		screen.fill((0, 0, 0))
		screen.blit(background, (0, 0))
		if STATE == IN_GAME:
			# playing game
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
				if event.type == pygame.QUIT:
					sys.exit()
				# 	spaceship shoots
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_SPACE:
						bulletList.append(player.shoot())

			# draw enemies
			for i in range(n_enemies):
				if enemyList[i].getY() > 650:
					enemyList.remove(enemyList[i])
					enemyList.append(Alien(screen))
				if enemyList[i].hit_spaceship(player.getX(), player.getY()):
					player.lose_one_heart()
					player.reset_level()
					enemyList.remove(enemyList[i])
					enemyList.append(Alien(screen))
				enemyList[i].show()
				enemyList[i].move()

			for i in range(n_bonus):
				if bonusList[i].getY() > 650:
					bonusList.remove(bonusList[i])
					bonusList.append(Bonus(screen))
				if bonusList[i].hit_spaceship(player.getX(), player.getY()):
					bonus += 1
					if bonus >= 10:
						player.level_up()
						bonus = 0
					bonusList.remove(bonusList[i])
					bonusList.append(Bonus(screen))
				bonusList[i].show()
				bonusList[i].move()

			# movement bullet
			for bullet in bulletList:
				if bullet.getY() < -20:
					bulletList.remove(bullet)
				bullet.show()
				bullet.move()

			# isThere alien has been shooted ?
			if isCollision(enemyList, bulletList):
				score += 1
				Alien.movementSpeed += Alien.movementSpeed * 0.1

			# draw spaceship
			player.show()

			# draw score
			show_score(scoreX, scoreY)

			# draw life
			show_heart(player.getHeart(), heartX, heartY)

			# game over ?
			if player.getHeart() <= 0:
				del player
				STATE = GAME_OVER

		elif STATE == GAME_OVER:
			# display game over text and menu
			for event in pygame.event.get():
				# 		exit button pressed
				if event.type == pygame.QUIT:
					sys.exit()

			game_over()

		# update the screen for every change
		pygame.display.update()


# make menu
menu = pygame_menu.Menu('Welcome', 300, 400, theme=pygame_menu.themes.THEME_BLUE)
menu.add.button('Play', start)
menu.add.button('Quit', pygame_menu.events.EXIT)

menu.mainloop(screen)
