import pygame as pg
import json
import sys
from charackter import *
from sttings import *
from colors import *
from block import *
from tree import *
from health import *
from flag import *
map_x = []
map_y = []
tree_x = []
tree_y = []
flag_x = []
flag_y = []
charr = ''
ch = 0
pg.init()
try :
	with open('json/map_convertx.json') as file:
		map_x = json.load(file)
	with open('json/map_converty.json') as file:
		map_y = json.load(file)
	with open('json/treex.json') as file:
		tree_x = json.load(file)
	with open('json/treey.json') as file:
		tree_y = json.load(file)
	with open('json/flagx.json') as file:
		flag_x = json.load(file)
	with open('json/flagy.json') as file:
		flag_y = json.load(file)
except FileNotFoundError:
	print('error.txt')
	with open('error.txt','w') as er:
		er.write('no file map_converty.json or map_convertx.json,open creator')
try:
	pg.mixer.music.load('voices/mus.mp3')
	pg.mixer.music.play(loops = -1)
except FileNotFoundError:
	print('error.txt')
	with open('error.txt','w') as er:
		er.write('cant load mus.mp3,please re-install game')
sc = pg.display.set_mode(size)
clock = pg.time.Clock()
blocks = pg.sprite.Group()
all_sprites = pg.sprite.Group()
player = Player()
all_players = pg.sprite.Group()
all_players.add(player) 
heart1 = Heart(20,20,0)
heart2 = Heart(40,20,0)
heart3 = Heart(60,20,0)
hearts = pg.sprite.Group()
hearts.add(heart1)
hearts.add(heart2)
hearts.add(heart3)
trees = pg.sprite.Group()
flags = pg.sprite.Group()
bg = pg.image.load('img/fone.png')
with open('json/statics.json','r') as stat:
	player.bestscore = json.load(stat)
for i in range(0,len(map_x)):
	block = Block(map_x[i],map_y[i])
	blocks.add(block)
for i in range(0,len(tree_x)):
	tree = Tree(tree_x[i],tree_y[i])
	trees.add(tree)
for i in range(0,len(flag_x)):
	flag = Flag(flag_x[i],flag_y[i])
	flags.add(flag)
def change():
	if player.health>0:
		heart1.num = 0
	if player.health>50:
		heart1.num = 1
	if player.health>100:
		heart1.num = 2
	if player.health>100:
		heart2.num = 0
	if player.health>150:
		heart2.num = 1
	if player.health>200:
		heart2.num = 2
	if player.health>200:
		heart3.num = 0
	if player.health>250:
		heart3.num = 1
	if player.health==300:
		heart3.num = 2	
def updater():
	all_players.draw(sc)
	all_players.update()
	blocks.draw(sc)
	blocks.update()
	bullets.draw(sc)
	bullets.update()
	trees.draw(sc)
	trees.update()
	hearts.draw(sc)
	hearts.update()
	flags.draw(sc)
	flags.update()
	change()
while running:
	for e in pg.event.get():
		if e.type == pg.QUIT:
			running = False
	sc.blit(bg,(0,0))
	updater()		
#	pg.draw.rect(sc,Blue[0],(20,40,player.num,20))
	pg.display.flip()
	hits = pg.sprite.groupcollide(all_players,blocks,False,False)
	if player.health <= 0:
		running = False
	for hit in hits:
		player.health-=1               
	clock.tick(FPS) 
with open('statics.json','w') as stat:
	if player.bestscore < player.score:
		player.bestscore = player.score
	json.dump(player.bestscore,stat)
pg.quit()