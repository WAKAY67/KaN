import pygame as pg
import random



enemies=[]
cooldown=0
spawnrate=30
enemy_size = 50
enemy_img=pg.image.load('sprites/enemy/monster.png')
enemy_image=pg.transform.scale(enemy_img,(enemy_size,enemy_size))
enemy_speed = 2

def enemy_update(player_rect):
    for enemy in enemies:
        enemy_direction =pg.Vector2( player_rect.center) - pg.Vector2(enemy.center)
        if enemy_direction.length() != 0:
            enemy_direction = enemy_direction.normalize()
        enemy.center += enemy_direction * enemy_speed

def enemy_spawn(width,height):
    sides=['right','left','top','bottom']
    randomside=random.choice(sides)
    if randomside == 'bottom':
        y=height 
        x=random.randint(0,width)
    elif randomside == 'top':
        y=-enemy_size
        x=random.randint(0,width)
    elif randomside == 'left':
        y=random.randint(0,height)
        x=-enemy_size
    elif randomside=='right':
        y=random.randint(0,height)
        x=width
    enemy_rect=pg.Rect(x,y , enemy_size, enemy_size)
    enemies.append(enemy_rect)
    
def enemy_check_collision(player_rect):
    for enemy in enemies:
        if player_rect.colliderect(enemy):
            return True
        else:
            return False

def enemy_draw(screen):
    for enemy in enemies:
        screen.blit(enemy_image,enemy)

def update_spawn(width,height):
    global cooldown 
    cooldown-=1
    if cooldown <=0:
        enemy_spawn(width,height)
        cooldown=spawnrate