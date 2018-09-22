import random
import pygame
SCREEN_RECT = pygame.Rect(0,0,480,700)
CREANT_ENEMY_EVENT = pygame.USEREVENT
CREANT_BULLET_EVENT = pygame.USEREVENT+1
class GameSprite(pygame.sprite.Sprite):
	def __init__(self,imagename,speed = 1):
		super().__init__()
		self.image = pygame.image.load(imagename)
		self.rect = self.image.get_rect()
		self.speed = speed
	def update(self):
		self.rect.y += self.speed
class EnemySprite(GameSprite):
	def __init__(self):
		imagename = "./images/enemy-2.gif"
		super().__init__(imagename,5)
		self.rect.bottom = 0
		self.rect.x = random.randint(0,SCREEN_RECT.width-self.rect.width)
	def update(self):
		super().update()
		if self.rect.y >= SCREEN_RECT.height:
			self.kill()
class BackgroundSprite(GameSprite):
	def __init__(self,isalt = True):
		imagename = "./images/background.png"
		super().__init__(imagename,5)
		if not isalt:		
			self.rect.bottom = 0
	def update(self):
		super().update()
		if self.rect.top >= SCREEN_RECT.height:
			self.rect.bottom = 0
class HeroSprite(GameSprite):
	def __init__(self):
		imagename = "./images/hero.gif"
		super().__init__(imagename,0)
		self.rect.centerx = SCREEN_RECT.centerx 
		self.rect.bottom = SCREEN_RECT.height - 100
	def update(self):
		self.rect.x += self.speed
		if self.rect.left <= 0:
				self.rect.left = 0
		if self.rect.right > SCREEN_RECT.right:
				self.rect.right = SCREEN_RECT.right
		self.rect.y += self.speed1
		if self.rect.width <= 0:
				self.rect.width = 0
		if self.rect.bottom > SCREEN_RECT.bottom:
				self.rect.bottom = SCREEN_RECT.bottom
		if self.rect.top <= SCREEN_RECT.top:
				self.rect.top = SCREEN_RECT.top
class BulletSprite(GameSprite):
	def __init__(self):
			imagename = "images/bullet1.png"
			super().__init__(imagename,-5)
	def update(self):
			super().update()
			if self.rect.bottom <= 0:
					self.kill()


