import json
import pygame as pg
from colors import *
from block import *
from sttings import *
from tree import *
from flag import *
map_x = []
map_y = []
tree_x = []
tree_y =[]
flag_x = []
flag_y =[]
running = True
pg.init()
sc = pg.display.set_mode((size))
clock = pg.time.Clock()
all_flags = pg.sprite.Group()
all_blocks = pg.sprite.Group()
all_trees = pg.sprite.Group()
x_mouse,y_mouse = 0,0
while running:
	for e in pg.event.get():
		if e.type == pg.QUIT:
			running = False
		elif e.type == pg.MOUSEBUTTONDOWN:
			if e.button == 3:
				x_mouse,y_mouse = e.pos
				block = Block(x_mouse,y_mouse)
				hits = pg.sprite.spritecollide(block,all_blocks,True)
				all_blocks.add(block)
				for hit in hits:
					all_blocks.remove(block)
			elif e.button == 1:
				x_mouse,y_mouse = e.pos
				tree = Tree(x_mouse,y_mouse)
				hits = pg.sprite.spritecollide(tree,all_trees,True)
				all_trees.add(tree)
				for hit in hits:
					all_trees.remove(tree)
			elif e.button == 2:
				x_mouse,y_mouse = e.pos
				flag = Flag(x_mouse,y_mouse)
				hits = pg.sprite.spritecollide(flag,all_flags,True)
				all_flags.add(flag)
				for hit in hits:
					all_flags.remove(flag)
		sc.fill((0,0,0))
		all_blocks.draw(sc)
		all_blocks.update()
		all_flags.draw(sc)
		all_flags.update()
		all_trees.draw(sc)
		all_trees.update()		
		pg.display.flip()
		clock.tick(FPS)
for sprite in all_blocks:
	map_x.append(sprite.rect.x)
	map_y.append(sprite.rect.y)
for sprite in all_trees:
	tree_x.append(sprite.rect.x)
	tree_y.append(sprite.rect.y)
for sprite in all_flags:
	flag_x.append(sprite.rect.x)
	flag_y.append(sprite.rect.y)
with open('json/map_convertx.json','w') as mapx:
	json.dump(map_x, mapx)
with open('json/map_converty.json','w') as mapy:
	json.dump(map_y, mapy)
with open('json/treex.json','w') as mapx:
	json.dump(tree_x, mapx)
with open('json/treey.json','w') as mapy:
	json.dump(tree_y, mapy)
with open('json/flagx.json','w') as mapx:
	json.dump(flag_x,mapx)
with open('json/flagy.json','w') as mapy:
	json.dump(flag_y,mapy)
pg.quit()