import pygame as pg
class Flag(pg.sprite.Sprite):
	def __init__(self,x,y):
		pg.sprite.Sprite.__init__(self)
		self.x1 = 10
		self.y1 = 10
		self.sizeb = 18
		self.fl1 = 'img/flag.png'
		self.fl2 = 'img/flag1.png'
		self.size = (self.x1,self.y1)
		self.image = pg.image.load(self.fl1)
		self.rect = self.image.get_rect()
		self.rect.x = int(x/self.sizeb)*self.sizeb
		self.rect.y = int(y/self.sizeb)*self.sizeb
		self.num = 0
	def change(self,sel):
		self.image = pg.image.load(sel)
	def update(self):
		if self.num <=16:
			self.change(self.fl1)
		elif self.num > 16:
			self.change(self.fl2)
		self.num+=1
		if self.num == 32:
			self.num = 0