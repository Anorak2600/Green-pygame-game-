import pygame as pg
from sttings import *
from knife import *
bullets = pg.sprite.Group()
class Player(pg.sprite.Sprite):
	def __init__(self):
		pg.sprite.Sprite.__init__(self)
		self.size = (50,50)
		self.skin_idle = 'img/player_1_idle.png'
		self.skin_run = 'img/player1_run.png'
		self.skin_idler = 'img/player_1_idler.png'
		self.skin_runr = 'img/player1_runr.png'
		self.laser1 = 'img/laser2.png'
		self.laser2 = 'img/laser3.png'
		self.images = ['knight1.png','knight2.png']
		self.image = pg.image.load(self.skin_runr)
		self.rect = self.image.get_rect()
		self.rect.x = 600
		self.rect.y = 300
		self.speed = 2
		self.health = 300
		self.num = 0
		self.napr = 'u'
		self.pr_napr = 'r'
		self.bestscore = 0
		self.score = 0
		self.pos_is = 1
	def shoot(self):
		if self.num >= 30:
			self.num-=30
			if self.napr == 'u':
				knife = Knife(self.rect.x, self.rect.y+17,0,-self.speed,self.laser2)
			elif self.napr == 'l':
				knife = Knife(self.rect.x, self.rect.y+17,-self.speed,0,self.laser1)
			elif self.napr == 'r':
				knife = Knife(self.rect.x, self.rect.y+17,self.speed,0,self.laser1)
			elif self.napr == 'd':
				knife = Knife(self.rect.x, self.rect.y+17,0,self.speed,self.laser2)
			bullets.add(knife)
	def change_skin(self):
#		self.image = pg.image.load(self.images[self.pos_is])
		if self.pos_is <=10 and self.pr_napr == 'l':
			self.image = pg.image.load(self.skin_idle)
		elif self.pos_is > 10 and self.pr_napr == 'l':
			self.image = pg.image.load(self.skin_run)
		if self.pos_is <=10 and self.pr_napr == 'r':
			self.image = pg.image.load(self.skin_idler)
		elif self.pos_is > 10 and self.pr_napr == 'r':
			self.image = pg.image.load(self.skin_runr)
	def update(self):
		self.change_skin()
		if self.num<200:
			self.num+=1
		self.speedx = 0
		self.speedy = 0
		if self.health>300:
			self.health = 300
		key = pg.key.get_pressed()
		if key[pg.K_LEFT]:
			self.napr = 'l'
			self.speedx-=self.speed
			self.pos_is+=1
			self.pr_napr = 'l'
		if key[pg.K_RIGHT]:
			self.napr = 'r'
			self.speedx+=self.speed
			self.pos_is+=1
			self.pr_napr = 'r'
		if key[pg.K_UP]:
			self.napr = 'u'
			self.speedy-=self.speed
			self.pos_is+=1
		if key[pg.K_DOWN]:
			self.napr = 'd'
			self.speedy+=self.speed
			self.pos_is+=1
		if key[pg.K_SPACE]:
			self.shoot()
		if self.rect.x>=Width-9:
			self.rect.x = Width-9
		if self.rect.y>=Height-9:
			self.rect.y = Height-9
		if self.rect.x<=0:
			self.rect.x = 0
		if self.rect.y<=0:
			self.rect.y = 0
		self.rect.x+= self.speedx
		self.rect.y+=self.speedy
		if self.pos_is > 20:
			self.pos_is = 1