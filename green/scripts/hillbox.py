import pygame as pg
class Hillbox(pg.sprite.Sprite):
	"""docstring for Health"""
	def __init__(self,x,y,num):
		pg.sprite.Sprite.__init__(self)
		self.num = num
		self.image = pg.image.load('')
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y