# building space invaders in python

import pygame
import random
#import time
pygame.init()

# window specifications
screen = pygame.display.set_mode((1000,748))
pygame.display.set_caption('Space Invaders')
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)
bg = pygame.image.load('background_final.jpg')
clock = pygame.time.Clock()
score = 0
 
# loading all the spaceships
yellow_space_ship = pygame.image.load('pixel_ship_yellow.png')
red_space_ship = pygame.image.load('pixel_ship_red_small.png')
green_space_ship = pygame.image.load('pixel_ship_green_small.png')
blue_space_ship = pygame.image.load('pixel_ship_blue_small.png')
red_lazer = pygame.image.load('pixel_laser_red.png')
green_lazer = pygame.image.load('pixel_laser_green.png')
blue_lazer = pygame.image.load('pixel_laser_blue.png')
yellow_lazer = pygame.image.load('pixel_laser_yellow.png')

# these lines are for the entery display
font = pygame.font.SysFont('Century Gothic', 80, True)
font2 = pygame.font.SysFont('Century Gothic', 30, True)
text = font.render('Space Invaders', 1, (255,255,255))
screen.blit(text, (200,300))
pygame.display.update()
i = 0
while i<300:
	pygame.time.delay(10)
	i+=1


class player(object):
	def __init__(self,x,y,height,width):
		self.x = x
		self.y = y
		self.height = height
		self.width = width
		self.vel = 15
		self.health = 10
		self.hitbox = (self.x+2, self.y+1, 60, 65)
		self.bullet_vel = 10
		

	def draw(self,screen):
		screen.blit(yellow_space_ship,(self.x,self.y))

	def shoot_bullet(screen):
		#bullet.y -= bullet.vel
		screen.blit(yellow_lazer,(bullet.x, bullet.y))

	def hit(self):
		if self.health > 0:
			self.health -=1
	
	def red_bullet_hit(self):
		if self.health > 0:
			self.health -= 1
		enemyship.red_bullet_visible = False

	def green_bullet_hit(self):
		if self.health > 0:
			self.health -= 1
		enemyship.green_bullet_visible = False

	def blue_bullet_hit(self):
		if self.health > 0:
			self.health -= 1
		enemyship.blue_bullet_visible = False


class weapon(object):
	def __init__(self,x,y):
		self.x = x
		self.y = y
		self.state = False
		self.visible = True

	def draw(self,screen):
		screen.blit(yellow_lazer,(self.x,self.y))


class enemy(object):
	def __init__(self,red_x,green_x,blue_x,red_y,green_y,blue_y):
		self.red_x = red_x
		self.green_x = green_x
		self.blue_x = blue_x
		self.red_y = red_y
		self.green_y = green_y
		self.blue_y = blue_y
		self.redBullet_x = self.red_x
		self.redBullet_y = self.red_y
		self.greenBullet_x = self.green_x
		self.greenBullet_y = self.green_y
		self.blueBullet_x = self.blue_x
		self.blueBullet_y = self.blue_y
		self.red_visible = True
		self.green_visible = True
		self.blue_visible = True
		self.red_bullet_visible = True
		self.green_bullet_visible = True
		self.blue_bullet_visible = True
		self.enemyBullet_vel = 7
		self.vel = 2
		self.red_health = 10
		self.green_health = 10
		self.blue_health = 10

	def red_enemy_hit(self):
		if self.red_health > 0:
			self.red_health -= 1

		if self.red_health == 0:
			self.red_visible = False
			self.red_bullet_visible = False

		#spaceship.bullet_visible = False

	def green_enemy_hit(self):
		if self.green_health > 0:
			self.green_health -= 1

		if self.green_health == 0:
			self.green_visible = False
			self.green_bullet_visible = False

	def blue_enemy_hit(self):
		if self.blue_health > 0:
			self.blue_health -= 1

		if self.blue_health == 0:
			self.blue_visible = False
			self.blue_bullet_visible = False

	def draw(self,screen):
		if self.red_y<748 or self.green_y<748 or self.blue_y<748:
			self.red_y += self.vel
			self.green_y += self.vel
			self.blue_y += self.vel
			self.red_hitbox = (self.red_x+5, self.red_y+1, 60, 45)
			self.green_hitbox = (self.green_x+5, self.green_y+1, 60, 45)
			self.blue_hitbox = (self.blue_x+5, self.blue_y+1, 40, 45)
			
			if self.red_visible:
				# red spaceship config
				screen.blit(red_space_ship,(self.red_x,self.red_y))
				# below line is for hitbox
				#pygame.draw.rect(screen, (255,0,0), self.red_hitbox, 2)
				# healthbar
				pygame.draw.rect(screen, (255,0,0), (self.red_x+11, self.red_y-6, 50, 10))
				pygame.draw.rect(screen, (0,128,0), (self.red_x+11, self.red_y-6, 50-(5*(10-self.red_health)), 10))

			if self.green_visible:
				# green spaceship config
				screen.blit(green_space_ship,(self.green_x, self.green_y))
				# green_hitbox = (self.green_x+5, self.green_y+1, 60, 45)
				# below line is for hitbox
				# pygame.draw.rect(screen, (255,0,0), self.green_hitbox, 2)
				# healthbar
				pygame.draw.rect(screen, (255,0,0), (self.green_x+11, self.green_y-6, 50, 10))
				pygame.draw.rect(screen, (0,128,0), (self.green_x+11, self.green_y-6, 50-(5*(10-self.green_health)), 10))

			if self.blue_visible:
				# blue spaceship config
				screen.blit(blue_space_ship,(self.blue_x,self.blue_y))
				#blue_hitbox = (self.blue_x+5, self.blue_y+1, 40, 45)
				# below line is for hitbox
				# pygame.draw.rect(screen, (255,0,0), self.blue_hitbox, 2)
				# healthbar
				pygame.draw.rect(screen, (255,0,0), (self.blue_x, self.blue_y-6, 50, 10))
				pygame.draw.rect(screen, (0,128,0), (self.blue_x, self.blue_y-6, 50-(5*(10-self.blue_health)), 10))

	def enemy_bullet(self,screen):
		if self.redBullet_y<748 or self.greenBullet_y<748 or self.blueBullet_y<748:
			self.red_bullet_hitbox = (self.redBullet_x+25, self.redBullet_y+27, 20, 41)
			self.green_bullet_hitbox = (self.greenBullet_x+25, self.greenBullet_y+27, 20, 41)
			self.blue_bullet_hitbox = (self.blueBullet_x+15, self.blueBullet_y+37, 20, 41)

			if self.red_bullet_visible:
				screen.blit(red_lazer,(self.redBullet_x-15,self.redBullet_y+5))
				# pygame.draw.rect(screen, (255,0,0), self.red_bullet_hitbox, 2)

			if self.green_bullet_visible:
				screen.blit(green_lazer,(self.greenBullet_x-15,self.greenBullet_y+5))
				# pygame.draw.rect(screen, (255,0,0), self.green_bullet_hitbox, 2)

			if self.blue_bullet_visible:
				screen.blit(blue_lazer,(self.blueBullet_x-25,self.blueBullet_y+15))
				# pygame.draw.rect(screen, (255,0,0), self.blue_bullet_hitbox, 2)


def redrawgamewindow():
	screen.blit(bg,(0,0))
	text = font2.render('Score : ' + str(score), 1, (255,255,255))
	screen.blit(text,(840,10))
	spaceship.draw(screen)
	# spaceship_hitbox = (spaceship.x+2, spaceship.y+1, 60, 65)
	# below line is for the hitbox
	# pygame.draw.rect(screen, (255,0,0), spaceship_hitbox, 2)
	# healthbar
	pygame.draw.rect(screen, (255,0,0), (spaceship.x+8, spaceship.y+69, 50, 10))
	pygame.draw.rect(screen, (0,128,0), (spaceship.x+8, spaceship.y+69, 50-(5*(10-spaceship.health)), 10))

	if bullet.state :
		if bullet.y > 0:
			bullet.draw(screen)

		#print(bullet.y)
		# below line is for hitbox
		# pygame.draw.rect(screen, (255,0,0), bullet_hitbox, 2)

	enemyship.draw(screen)

	enemyship.enemy_bullet(screen)

	if enemyship.red_y>748 or enemyship.green_y>748 or enemyship.blue_y>748:
		enemyship.red_x = random.randint(20,330)
		enemyship.green_x = random.randint(330,660)
		enemyship.blue_x = random.randint(660,950)
		enemyship.red_y = random.randint(0,50)
		enemyship.green_y = random.randint(0,50)
		enemyship.blue_y = random.randint(0,50)
		#enemyship.red_bullet_visible = True
		#enemyship.green_bullet_visible = True
		#enemyship.blue_bullet_visible = True

	if enemyship.redBullet_y>748 or enemyship.greenBullet_y>748 or enemyship.blueBullet_y>748:
		enemyship.redBullet_x = enemyship.red_x
		enemyship.redBullet_y = enemyship.red_y
		enemyship.greenBullet_x = enemyship.green_x
		enemyship.greenBullet_y = enemyship.green_y
		enemyship.blueBullet_x = enemyship.blue_x
		enemyship.blueBullet_y = enemyship.blue_y 

	pygame.display.update()

spaceship = player(100, 550, 64, 64)
bullet = weapon(spaceship.x-18, spaceship.y-58)
enemyship = enemy(random.randint(20,302),random.randint(352,638),random.randint(682,950),random.randint(0,50),random.randint(0,50),random.randint(0,50))
bullets = []
run = True

# game loop
while run:
	#clock.tick(90)
	pygame.time.delay(10)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

	keys = pygame.key.get_pressed()

	if keys[pygame.K_LEFT] and spaceship.x>=spaceship.vel:
		spaceship.x-=spaceship.vel

	if keys[pygame.K_RIGHT] and spaceship.x<980-spaceship.width:
		spaceship.x+=spaceship.vel

	if keys[pygame.K_UP] and spaceship.y>=spaceship.vel:
		spaceship.y-=spaceship.vel

	if keys[pygame.K_DOWN] and spaceship.y<728-spaceship.width:
		spaceship.y+=spaceship.vel

	if keys[pygame.K_ESCAPE]:
		run = False

	if keys[pygame.K_SPACE]:
		# spaceship_hitbox = (x, y, breadth, length)
		bullet.x = spaceship.x-18
		bullet.y = spaceship.y-58
		#print(bullet.y)
		bullet.state = True

	if bullet.y > 0:
		bullet.y -= 10

	spaceship_hitbox = (spaceship.x+2, spaceship.y+1, 60, 65)
	
	bullet_hitbox = (bullet.x+40, bullet.y+20, 20, 41)

	enemyship.enemy_bullet(screen)
	enemyship.redBullet_y += enemyship.enemyBullet_vel
	enemyship.greenBullet_y += enemyship.enemyBullet_vel
	enemyship.blueBullet_y += enemyship.enemyBullet_vel

	enemyship.draw(screen)

	# spaceship to enemyship collisions

	if enemyship.red_visible == True:
		if spaceship_hitbox[1] < enemyship.red_hitbox[1] + enemyship.red_hitbox[3] and spaceship_hitbox[1] + spaceship_hitbox[3] > enemyship.red_hitbox[1]:
			if spaceship_hitbox[0] +spaceship_hitbox[2] > enemyship.red_hitbox[0] and spaceship_hitbox[0] < enemyship.red_hitbox[0] + enemyship.red_hitbox[2]:
				spaceship.hit()

	if enemyship.green_visible == True:
		if spaceship_hitbox[1] < enemyship.green_hitbox[1] + enemyship.green_hitbox[3] and spaceship_hitbox[1] + spaceship_hitbox[3] > enemyship.green_hitbox[1]:
			if spaceship_hitbox[0] +spaceship_hitbox[2] > enemyship.green_hitbox[0] and spaceship_hitbox[0] < enemyship.green_hitbox[0] + enemyship.green_hitbox[2]:
				spaceship.hit()

	if enemyship.blue_visible == True:
		if spaceship_hitbox[1] < enemyship.blue_hitbox[1] + enemyship.blue_hitbox[3] and spaceship_hitbox[1] + spaceship_hitbox[3] > enemyship.blue_hitbox[1]:
			if spaceship_hitbox[0] +spaceship_hitbox[2] > enemyship.blue_hitbox[0] and spaceship_hitbox[0] < enemyship.blue_hitbox[0] + enemyship.blue_hitbox[2]:
				spaceship.hit()

	# bullet to spaceship collisions

	if enemyship.red_bullet_visible == True:
		if spaceship_hitbox[1] < enemyship.red_bullet_hitbox[1] + enemyship.red_bullet_hitbox[3] and spaceship_hitbox[1] + spaceship_hitbox[3] > enemyship.red_bullet_hitbox[1]:
			if spaceship_hitbox[0] +spaceship_hitbox[2] > enemyship.red_bullet_hitbox[0] and spaceship_hitbox[0] < enemyship.red_bullet_hitbox[0] + enemyship.red_bullet_hitbox[2]:
				spaceship.red_bullet_hit()

	if enemyship.green_bullet_visible == True:
		if spaceship_hitbox[1] < enemyship.green_bullet_hitbox[1] + enemyship.green_bullet_hitbox[3] and spaceship_hitbox[1] + spaceship_hitbox[3] > enemyship.green_bullet_hitbox[1]:
			if spaceship_hitbox[0] +spaceship_hitbox[2] > enemyship.green_bullet_hitbox[0] and spaceship_hitbox[0] < enemyship.green_bullet_hitbox[0] + enemyship.green_bullet_hitbox[2]:
				spaceship.green_bullet_hit()

	if enemyship.blue_bullet_visible == True:
		if spaceship_hitbox[1] < enemyship.blue_bullet_hitbox[1] + enemyship.blue_bullet_hitbox[3] and spaceship_hitbox[1] + spaceship_hitbox[3] > enemyship.blue_bullet_hitbox[1]:
			if spaceship_hitbox[0] +spaceship_hitbox[2] > enemyship.blue_bullet_hitbox[0] and spaceship_hitbox[0] < enemyship.blue_bullet_hitbox[0] + enemyship.blue_bullet_hitbox[2]:
				spaceship.blue_bullet_hit()

	# collision with the spaceship's bullet


	if bullet_hitbox[1] < enemyship.red_hitbox[1] + enemyship.red_hitbox[3] and bullet_hitbox[1] + bullet_hitbox[3] > enemyship.red_hitbox[1]:
		if bullet_hitbox[0] + bullet_hitbox[2] > enemyship.red_hitbox[0] and bullet_hitbox[0] < enemyship.red_hitbox[0] + enemyship.red_hitbox[2]:
			enemyship.red_enemy_hit()
			score += 10

	if bullet_hitbox[1] < enemyship.green_hitbox[1] + enemyship.green_hitbox[3] and bullet_hitbox[1] + bullet_hitbox[3] > enemyship.green_hitbox[1]:
		if bullet_hitbox[0] + bullet_hitbox[2] > enemyship.green_hitbox[0] and bullet_hitbox[0] < enemyship.green_hitbox[0] + enemyship.green_hitbox[2]:
			enemyship.green_enemy_hit()
			score += 10

	if bullet_hitbox[1] < enemyship.blue_hitbox[1] + enemyship.blue_hitbox[3] and bullet_hitbox[1] + bullet_hitbox[3] > enemyship.blue_hitbox[1]:
		if bullet_hitbox[0] + bullet_hitbox[2] > enemyship.blue_hitbox[0] and bullet_hitbox[0] < enemyship.blue_hitbox[0] + enemyship.blue_hitbox[2]:
			enemyship.blue_enemy_hit()
			score += 10

	if spaceship.health<=0:
		text1 = font.render('You Lost', 1, (255,255,255))
		screen.blit(text2, (400,390))
		pygame.display.update()
		i = 0
		while i<300:
			pygame.time.delay(10)
			i+=1
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					i = 301
					pygame.quit()

	if enemyship.red_health<=0 and enemyship.green_health<=0 and enemyship.blue_health<=0 and spaceship.health>0:
		#print("You won")
		text = font.render('You Won', 1, (255,255,255))
		screen.blit(text, (350, 300))
		pygame.display.update()
		i = 0
		while i<300:
			pygame.time.delay(10)
			i+=1
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					i = 301
					pygame.quit()

	redrawgamewindow()

pygame.quit()