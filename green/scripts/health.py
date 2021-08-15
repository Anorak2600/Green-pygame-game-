import pygame as pg
class Heart(pg.sprite.Sprite):
	"""docstring for Health"""
	def __init__(self,x,y,num):
		pg.sprite.Sprite.__init__(self)
		self.num = num
		if self.num == 0:
			self.image = pg.image.load('img/heart2.png')
		elif self.num == 1:
			self.image = pg.image.load('img/heart1.png')
		elif self.num == 2:
			self.image = pg.image.load('img/heartt.png')
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
	def update(self):
		if self.num == 0:
			self.image = pg.image.load('img/heart2.png')
		elif self.num == 1:
			self.image = pg.image.load('img/heart1.png')
		elif self.num == 2:
			self.image = pg.image.load('img/heartt.png')				