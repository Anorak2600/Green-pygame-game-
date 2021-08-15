import pygame as pg
class Block(pg.sprite.Sprite):
	def __init__(self,x,y):
		pg.sprite.Sprite.__init__(self)
		self.x1 = 10
		self.y1 = 10
		self.sizeb = 18
		self.size = (self.x1,self.y1)
		self.image = pg.image.load('img/block1.png')
		self.rect = self.image.get_rect()
		self.rect.x = int(x/self.sizeb)*self.sizeb
		self.rect.y = int(y/self.sizeb)*self.sizeb
		self.num = 0