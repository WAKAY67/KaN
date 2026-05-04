import pygame as pg

defeat_enemy=0
shoot_cooldown = 0
shoot_rate = 14
bullets = []
speed_bullets = 10
bullets_size = 10
bullets_img=pg.image.load('sprites/bullet.png')
bullet_image=pg.transform.scale(bullets_img,(bullets_size,bullets_size))

def create_bullets(player_rect , mouse_pose):
    global shoot_cooldown
    
    if shoot_cooldown > 0:
        return
    
    start_pose = pg.math.Vector2(player_rect.centerx , player_rect.centery)
    direction = mouse_pose - start_pose
    if direction.length() != 0:
        direction = direction.normalize()
        
    bullet_rect = pg.Rect(start_pose.x, start_pose.y, bullets_size, bullets_size)
    bullets.append([bullet_rect, direction])
    
    shoot_cooldown = shoot_rate

def update_bullets():
    for i in bullets:
        i[0].center += i[1] * speed_bullets

def draw_bullets(screen):
    for u in bullets:
        screen.blit(bullet_image,u[0])

def collision_check(enemies):
    global defeat_enemy
    for enemy in enemies:
        for bullet in bullets:
            if bullet[0].colliderect(enemy):
                bullets.remove(bullet)
                enemies.remove(enemy)
                defeat_enemy+=1

                
def update_cooldown():
    global shoot_cooldown
    if shoot_cooldown > 0:
        shoot_cooldown -= 1