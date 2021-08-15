import pygame as pg
from sttings import *
class Knife(pg.sprite.Sprite):
	def __init__(self,x,y,sx,sy,image):
		pg.sprite.Sprite.__init__(self)
		self.image = pg.image.load(image)
		self.rect = self.image.get_rect()
		self.x = x
		self.y = y
		self.rect.x,self.rect.y = x,y
		self.speedx = sx
		self.speedy = sy
	def update(self):
		self.rect.y += self.speedy
		self.rect.x += self.speedx
		if self.rect.y < 0:
			self.kill()