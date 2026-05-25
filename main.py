import pygame as pg
import random
import player
import enemy
import bullets

pg.init()
WIDTH = 800 
HEIGHT = 600
FPS = 60
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption('KaN')
clock = pg.time.Clock()

font = pg.font.Font(None, 36)
big_font=pg.font.Font(None,72)
start_time = pg.time.get_ticks()
game_over=False
running = True
while running:
    clock.tick(FPS)
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if game_over == False:
            if event.type == pg.MOUSEBUTTONDOWN:
                mouse_pose = pg.math.Vector2(pg.mouse.get_pos())
                bullets.create_bullets(player.player_rect , mouse_pose)
        if game_over == True and event.type==pg.KEYDOWN:
            if event.key== pg.K_r:
                player.restart_player()
                bullets.respawn_bullets()
                enemy.respawn_enemy()
                start_time= pg.time.get_ticks()
                game_over= False
            
    # обновление
    if game_over==False:
        player.update_player()
        enemy.enemy_update(player.player_rect)
        bullets.update_bullets()
        bullets.update_cooldown()   
        bullets.collision_check(enemy.enemies)
        enemy.update_spawn(WIDTH, HEIGHT)

        if enemy.enemy_check_collision(player.player_rect)== True:
            game_over=True

    # время
    current_time = (pg.time.get_ticks() - start_time) // 1000
    time_text = font.render(f"Time: {current_time}", True, (255, 255, 255))
    
    score_text=font.render(f'score:{bullets.defeat_enemy}',True,(255,255,255))
    

    screen.fill('#a9e06c')

    # отрисовка
    screen.blit(time_text, (10, 10))
    player.draw_player(screen)
    enemy.enemy_draw(screen)
    bullets.draw_bullets(screen)
    screen.blit(score_text,(10,40))

    if game_over== True:
        gameover=big_font.render(f'game over',True,'red')
        screen.blit(gameover,(300,200))


    pg.display.update()



pg.quit()