import pygame as pg
from block import *
from tree import *

class Creator(pg.sprite.Sprite):
	def make_tree(x,y):
		self.tree = Tree(x,y)
		return self.tree 
	def make_block(x,y):
		self.block = Block(x,y)
		return self.block 