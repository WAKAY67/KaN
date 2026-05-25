import pygame as pg

WIDTH=800
HEIGHT=600

player_size = 50
player_img=pg.image.load('sprites/player/player.png')
player_image=pg.transform.scale(player_img,(player_size,player_size))
player_rect = pg.Rect(WIDTH//2, HEIGHT//2,player_size,player_size)
speed = 5

def update_player():
    keys = pg.key.get_pressed()
    if keys[pg.K_a]:  
        player_rect.x -= speed
    if keys[pg.K_d]: 
        player_rect.x += speed
    if keys[pg.K_w]:  
        player_rect.y -= speed
    if keys[pg.K_s]:  
        player_rect.y += speed
    player_rect.x = max(0, min(WIDTH - player_size, player_rect.x))
    player_rect.y = max(0, min(HEIGHT - player_size, player_rect.y))

def draw_player(screen):
    screen.blit(player_image,player_rect)

def restart_player():
    player_rect.x=WIDTH//2
    player_rect.y=HEIGHT//2