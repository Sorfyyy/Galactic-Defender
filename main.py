import pygame 
pygame.init()

pygame.display.set_caption('Galactic Defender')
icon = pygame.image.load('images/Galactic_Defender_icon.png')
pygame.display.set_icon(icon)

clock = pygame.time.Clock()

bg_x = 0
bg_y = 0

screen = pygame.display.set_mode((1280, 720))
bg = pygame.image.load('images/bg.jpg')
bg = pygame.transform.scale(bg, (1280, 720))

ship1 = pygame.image.load('images/ship1.png')
ship2 = pygame.image.load('images/ship2.png')
ship3 = pygame.image.load('images/ship3.png')
ship4 = pygame.image.load('images/ship4.png')

space_ship_animation = [
    pygame.transform.scale((ship1), (150, 150)),
    pygame.transform.scale((ship2), (150, 150)),
    pygame.transform.scale((ship3), (150, 150)),
    pygame.transform.scale((ship4), (150, 150))
]

boom1 = pygame.image.load('images/boom1.png')
boom2 = pygame.image.load('images/boom2.png')
boom3 = pygame.image.load('images/boom3.png')
boom4 = pygame.image.load('images/boom4.png')

boom_animation = [
    pygame.transform.scale((boom1), (150, 150)),
    pygame.transform.scale((boom2), (150, 150)),
    pygame.transform.scale((boom3), (150, 150)),
    pygame.transform.scale((boom4), (150, 150))
]

boom_anim_count = 0
boom_anim_time = 0
boom_anim_delay = 100  
explosion_active = False
explosion_pos = (0, 0)



bg_music = pygame.mixer.Sound('sounds/bg_space_music.mp3')
bg_music.play(loops=-1)

laser = pygame.mixer.Sound('sounds/laser.mp3')

ship_anim_count = 0
ship_x = 550
ship_y = 550
ship_speed = 10


bullet = pygame.image.load('images/bullet.png')
bullets = []
bullet_speed = 50

alien1 = pygame.image.load('images/alien1.png')
alien2 = pygame.image.load('images/alien2.png')
alien3 = pygame.image.load('images/alien3.png')
alien4 = pygame.image.load('images/alien4.png')

alien1_1 = pygame.transform.scale(alien1, (100, 100))
alien1_2 = pygame.transform.scale(alien1, (100, 100))
alien1_3 = pygame.transform.scale(alien1, (100, 100))
alien1_4 = pygame.transform.scale(alien1, (100, 100))
alien1_5 = pygame.transform.scale(alien1, (100, 100))

alien2_1 = pygame.transform.scale(alien2, (100, 100))
alien2_2 = pygame.transform.scale(alien2, (100, 100))
alien2_3 = pygame.transform.scale(alien2, (100, 100))
alien2_4 = pygame.transform.scale(alien2, (100, 100))
alien2_5 = pygame.transform.scale(alien2, (100, 100))

alien3_1 = pygame.transform.scale(alien3, (100, 100))
alien3_2 = pygame.transform.scale(alien3, (100, 100))
alien3_3 = pygame.transform.scale(alien3, (100, 100))
alien3_4 = pygame.transform.scale(alien3, (100, 100))
alien3_5 = pygame.transform.scale(alien3, (100, 100))

alien4_1 = pygame.transform.scale(alien4, (100, 100))
alien4_2 = pygame.transform.scale(alien4, (100, 100))
alien4_3 = pygame.transform.scale(alien4, (100, 100))
alien4_4 = pygame.transform.scale(alien4, (100, 100))
alien4_5 = pygame.transform.scale(alien4, (100, 100))

alien1_speed = 10
alien2_speed = 12
alien3_speed = 13
alien4_speed = 16


alien1_speed_y = 0.4
alien2_speed_y = 0.4
alien3_speed_y = 0.4
alien4_speed_y = 0.4


alien1_1_x = 50
alien1_1_y = 50

alien1_2_x = 1000
alien1_2_y = 50

alien1_3_x = 500
alien1_3_y = 50

alien1_4_x = 750
alien1_4_y = 50

alien1_5_x = 250
alien1_5_y = 50



alien2_1_x = 50
alien2_1_y = 50
alien2_1_count = 0

alien2_2_x = 250
alien2_2_y = 50
alien2_2_count = 0

alien2_3_x = 500
alien2_3_y = 50
alien2_3_count = 0

alien2_4_x = 750
alien2_4_y = 50
alien2_4_count = 0

alien2_5_x = 1000
alien2_5_y = 50
alien2_5_count = 0



alien3_1_x = 50
alien3_1_y = 50
alien3_1_count = 0

alien3_2_x = 250
alien3_2_y = 50
alien3_2_count = 0

alien3_3_x = 500
alien3_3_y = 50
alien3_3_count = 0

alien3_4_x = 750
alien3_4_y = 50
alien3_4_count = 0

alien3_5_x = 1000
alien3_5_y = 50
alien3_5_count = 0



alien4_1_x = 50
alien4_1_y = 50
alien4_1_count = 0

alien4_2_x = 250
alien4_2_y = 50
alien4_2_count = 0

alien4_3_x = 500
alien4_3_y = 50
alien4_3_count = 0

alien4_4_x = 750
alien4_4_y = 50
alien4_4_count = 0

alien4_5_x = 1000
alien4_5_y = 50
alien4_5_count = 0



alien1_all_dead = False
alien1_1_alive = True
alien1_2_alive = True
alien1_3_alive = True
alien1_4_alive = True
alien1_5_alive = True

alien2_all_dead = False
alien2_1_alive = True
alien2_2_alive = True
alien2_3_alive = True
alien2_4_alive = True
alien2_5_alive = True

alien3_all_dead = False
alien3_1_alive = True
alien3_2_alive = True
alien3_3_alive = True
alien3_4_alive = True
alien3_5_alive = True

alien4_all_dead = False
alien4_1_alive = True
alien4_2_alive = True
alien4_3_alive = True
alien4_4_alive = True
alien4_5_alive = True

alien1_1_moving_right = True
alien1_2_moving_right = True
alien1_3_moving_right = True
alien1_4_moving_right = True
alien1_5_moving_right = True

alien2_1_moving_right = True
alien2_2_moving_right = True
alien2_3_moving_right = True
alien2_4_moving_right = True
alien2_5_moving_right = True

alien3_1_moving_right = True
alien3_2_moving_right = True
alien3_3_moving_right = True
alien3_4_moving_right = True
alien3_5_moving_right = True

alien4_1_moving_right = True
alien4_2_moving_right = True
alien4_3_moving_right = True
alien4_4_moving_right = True
alien4_5_moving_right = True


alien1_in_game = []
alien2_in_game = []
alien3_in_game = []
alien4_in_game = []


alien1_timer = pygame.USEREVENT + 1
pygame.time.set_timer(alien1_timer, 2000)


label = pygame.font.Font('fonts/space_font.ttf')

lose_label = label.render('GAME OVER', False, (94, 2, 2))
lose_label = pygame.transform.scale(lose_label, (450, 125))

win_label = label.render('YOU WIN', False, (94, 2, 2))
win_label = pygame.transform.scale(win_label, (450, 125))

restart_label = label.render('RESTART', False, (204, 22, 22))
restart_label = pygame.transform.scale(restart_label, (300, 100))
restart_label_rect = restart_label.get_rect(topleft = (490, 250))

win_restart_label = label.render('RESTART', False, (204, 22, 22))
win_restart_label = pygame.transform.scale(restart_label, (300, 100))
win_restart_label_rect = win_restart_label.get_rect(topleft = (490, 250))

exit_label = label.render('EXIT', False, (250, 250, 250))
exit_label = pygame.transform.scale(exit_label, (150, 75))
exit_label_rect = exit_label.get_rect(topleft = (555, 450))

exit2_label = label.render('EXIT', False, (250, 250, 250))
exit2_label = pygame.transform.scale(exit_label, (150, 75))
exit2_label_rect = exit_label.get_rect(topleft = (555, 550))

play_label = label.render('PLAY', False, (250, 250, 250))
play_label = pygame.transform.scale(play_label, (200, 75))
play_label_rect = play_label.get_rect(topleft = (535, 175))

settings_label = label.render('SETTINGS', False, (250, 250, 250))
settings_label = pygame.transform.scale(settings_label, (275, 75))
settings_label_rect = settings_label.get_rect(topleft = (495, 310))

alien1_speed_y_label = label.render('Enemy Y speed difficult:', False, (250, 250, 250))
alien1_speed_y_label= pygame.transform.scale(alien1_speed_y_label, (525, 65))

y_speed_difficult_eazy = label.render('EAZY', False, (250, 250, 250))
y_speed_difficult_eazy = pygame.transform.scale(y_speed_difficult_eazy, (125, 50))
y_speed_difficult_eazy_rect = y_speed_difficult_eazy.get_rect(topleft = (585, 160))

y_speed_difficult_normal = label.render('NORMAL', False, (250, 250, 250))
y_speed_difficult_normal = pygame.transform.scale(y_speed_difficult_normal, (225, 45))
y_speed_difficult_normal_rect = y_speed_difficult_normal.get_rect(topleft = (765, 160))

y_speed_difficult_hard = label.render('HARD', False, (250, 250, 250))
y_speed_difficult_hard = pygame.transform.scale(y_speed_difficult_hard, (125, 50))
y_speed_difficult_hard_rect = y_speed_difficult_hard.get_rect(topleft = (1050, 160))



alien1_speed_x_label = label.render('Enemy X speed difficult:', False, (250, 250, 250))
alien1_speed_x_label = pygame.transform.scale(alien1_speed_x_label, (525, 65))

x_speed_difficult_eazy = label.render('EAZY', False, (250, 250, 250))
x_speed_difficult_eazy = pygame.transform.scale(x_speed_difficult_eazy, (125, 50))
x_speed_difficult_eazy_rect = x_speed_difficult_eazy.get_rect(topleft = (585, 310))

x_speed_difficult_normal = label.render('NORMAL', False, (250, 250, 250))
x_speed_difficult_normal = pygame.transform.scale(x_speed_difficult_normal, (225, 45))
x_speed_difficult_normal_rect = x_speed_difficult_normal.get_rect(topleft = (765, 310))

x_speed_difficult_hard = label.render('HARD', False, (250, 250, 250))
x_speed_difficult_hard = pygame.transform.scale(x_speed_difficult_hard, (125, 50))
x_speed_difficult_hard_rect = x_speed_difficult_hard.get_rect(topleft = (1050, 310))


space_ship_speed = label.render('SHIP SPEED:', False, (250, 250, 250))
space_ship_speed= pygame.transform.scale(space_ship_speed, (525, 65))

ship_speed_difficult_eazy = label.render('EAZY', False, (250, 250, 250))
ship_speed_difficult_eazy = pygame.transform.scale(ship_speed_difficult_eazy, (125, 50))
ship_speed_difficult_eazy_rect = ship_speed_difficult_eazy.get_rect(topleft = (585, 50))

ship_speed_difficult_normal = label.render('NORMAL', False, (250, 250, 250))
ship_speed_difficult_normal = pygame.transform.scale(ship_speed_difficult_normal, (225, 45))
ship_speed_difficult_normal_rect = ship_speed_difficult_normal.get_rect(topleft = (765, 50))

ship_speed_difficult_hard = label.render('HARD', False, (250, 250, 250))
ship_speed_difficult_hard = pygame.transform.scale(ship_speed_difficult_hard, (125, 50))
ship_speed_difficult_hard_rect = ship_speed_difficult_hard.get_rect(topleft = (1050, 50))



bullets_count_label = label.render('BULLETS COUNT:', False, (250, 250, 250))
bullets_count_label = pygame.transform.scale(bullets_count_label, (525, 65))

bullets_difficult_eazy = label.render('EAZY', False, (250, 250, 250))
bullets_difficult_eazy = pygame.transform.scale(bullets_difficult_eazy, (125, 50))
bullets_difficult_eazy_rect = bullets_difficult_eazy.get_rect(topleft = (585, 460))

bullets_difficult_normal = label.render('NORMAL', False, (250, 250, 250))
bullets_difficult_normal = pygame.transform.scale(bullets_difficult_normal, (225, 45))
bullets_difficult_normal_rect = bullets_difficult_normal.get_rect(topleft = (765, 460))

bullets_difficult_hard = label.render('HARD', False, (250, 250, 250))
bullets_difficult_hard = pygame.transform.scale(bullets_difficult_hard, (125, 50))
bullets_difficult_hard_rect = bullets_difficult_hard.get_rect(topleft = (1050, 460))


bullets_count = 1000
win = False
menu_settings = False
menu = True
gameplay = True
running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False
        if gameplay and event.type == pygame.KEYUP and event.key == pygame.K_SPACE:
            bullets.append(bullet.get_rect(topleft=(ship_x + 67, ship_y - 30)))
            bullets_count -= 1
            laser.play()
        if event.type == alien1_timer:
            alien1_in_game.append(alien1.get_rect(topleft = (100, 20)))
    clock.tick(30)
    
    
    
    if menu:
    
        screen.blit(bg, (0, bg_y))
        screen.blit(bg, (0, bg_y + 720))
        bg_y -= 10
        if bg_y <= -720:
            bg_y = 0
        
        screen.blit(play_label, (play_label_rect))
        screen.blit(exit_label, (exit_label_rect))
        screen.blit(settings_label, (settings_label_rect))
        mouse = pygame.mouse.get_pos()
        if play_label_rect.collidepoint(mouse) and not menu_settings and pygame.mouse.get_pressed()[0]:
            menu = False
        elif exit_label_rect.collidepoint(mouse) and not menu_settings and pygame.mouse.get_pressed()[0]:
            pygame.quit()
            running = False
        elif settings_label_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            menu_settings = True
            
            
        if menu_settings:
            screen.blit(bg, (0, bg_y))
            screen.blit(bg, (0, bg_y + 720))
            bg_y -= 10
            if bg_y <= -720:
                bg_y = 0

            screen.blit(exit2_label, (exit2_label_rect))
            screen.blit(alien1_speed_y_label, (25, 150))
            screen.blit(y_speed_difficult_eazy, (y_speed_difficult_eazy_rect))
            screen.blit(y_speed_difficult_normal, (y_speed_difficult_normal_rect))
            screen.blit(y_speed_difficult_hard, (y_speed_difficult_hard_rect))

            screen.blit(alien1_speed_x_label, (25, 300))
            screen.blit(x_speed_difficult_eazy, (x_speed_difficult_eazy_rect))
            screen.blit(x_speed_difficult_normal, (x_speed_difficult_normal_rect))
            screen.blit(x_speed_difficult_hard, (x_speed_difficult_hard_rect))

            screen.blit(bullets_count_label, (25, 450))
            screen.blit(bullets_difficult_eazy, (bullets_difficult_eazy_rect))
            screen.blit(bullets_difficult_normal, (bullets_difficult_normal_rect))
            screen.blit(bullets_difficult_hard, (bullets_difficult_hard_rect))

            screen.blit(space_ship_speed, (25, 40))
            screen.blit(ship_speed_difficult_eazy, (ship_speed_difficult_eazy_rect))
            screen.blit(ship_speed_difficult_normal, (ship_speed_difficult_normal_rect))
            screen.blit(ship_speed_difficult_hard, (ship_speed_difficult_hard_rect))


            mouse = pygame.mouse.get_pos()
            if exit2_label_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
                menu_settings = False
            elif y_speed_difficult_eazy_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
                alien1_speed_y = 0.4
                alien2_speed_y = 0.4
                alien3_speed_y = 0.4
                alien4_speed_y = 0.4
            elif y_speed_difficult_normal_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
                alien1_speed_y = 0.4
                alien2_speed_y = 0.5
                alien3_speed_y = 0.6
                alien4_speed_y = 0.8
            elif y_speed_difficult_hard_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
                alien1_speed_y = 0.4
                alien2_speed_y = 0.6
                alien3_speed_y = 0.8
                alien4_speed_y = 1
            
            
            elif x_speed_difficult_eazy_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
                alien1_speed = 10
                alien2_speed = 12
                alien3_speed = 13
                alien4_speed = 16
            elif x_speed_difficult_normal_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
                alien1_speed = 10
                alien2_speed = 14
                alien3_speed = 16
                alien4_speed = 20
            elif x_speed_difficult_hard_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
                alien1_speed = 10
                alien2_speed = 16
                alien3_speed = 19
                alien4_speed = 24


            elif bullets_difficult_eazy_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
                bullets_count = 1000
            elif bullets_difficult_normal_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
                bullets_count = 100
            elif bullets_difficult_hard_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
                bullets_count = 45


            elif ship_speed_difficult_eazy_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
                ship_speed = 15
            elif ship_speed_difficult_normal_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
                ship_speed = 10
            elif ship_speed_difficult_hard_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
                ship_speed = 8
                
                
                

    if (not menu) and (not menu_settings):

        screen.blit(bg, (0, bg_y))
        screen.blit(bg, (0, bg_y + 720))
            
        if gameplay:

            bg_y -= 10
            if bg_y <= -720:
                bg_y = 0

            
            screen.blit(space_ship_animation[ship_anim_count], (ship_x, ship_y))

            if ship_anim_count == 3:
                ship_anim_count = 0
            else:
                ship_anim_count += 1

            keys = pygame.key.get_pressed()
            

            if (keys[pygame.K_d] or keys[pygame.K_RIGHT]) and ship_x < 1145:
                ship_x += ship_speed
            elif (keys[pygame.K_a] or keys[pygame.K_LEFT]) and ship_x > 5:
                ship_x -= ship_speed 


            ship_rect = space_ship_animation[0].get_rect(topleft = (ship_x, ship_y))
            alien1_1_rect = alien1_1.get_rect(topleft = (alien1_1_x, alien1_1_y))
            alien1_2_rect = alien1_2.get_rect(topleft = (alien1_2_x, alien1_2_y))
            alien1_3_rect = alien1_3.get_rect(topleft = (alien1_3_x, alien1_3_y))
            alien1_4_rect = alien1_4.get_rect(topleft = (alien1_4_x, alien1_4_y))
            alien1_5_rect = alien1_5.get_rect(topleft = (alien1_5_x, alien1_5_y))

            alien2_1_rect = alien2_1.get_rect(topleft = (alien2_1_x, alien2_1_y))
            alien2_2_rect = alien2_2.get_rect(topleft = (alien2_2_x, alien2_2_y))
            alien2_3_rect = alien2_3.get_rect(topleft = (alien2_3_x, alien2_3_y))
            alien2_4_rect = alien2_4.get_rect(topleft = (alien2_4_x, alien2_4_y))
            alien2_5_rect = alien2_5.get_rect(topleft = (alien2_5_x, alien2_5_y))

            alien3_1_rect = alien3_1.get_rect(topleft = (alien3_1_x, alien3_1_y))
            alien3_2_rect = alien3_2.get_rect(topleft = (alien3_2_x, alien3_2_y))
            alien3_3_rect = alien3_3.get_rect(topleft = (alien3_3_x, alien3_3_y))
            alien3_4_rect = alien3_4.get_rect(topleft = (alien3_4_x, alien3_4_y))
            alien3_5_rect = alien3_5.get_rect(topleft = (alien3_5_x, alien3_5_y))

            alien4_1_rect = alien3_1.get_rect(topleft = (alien4_1_x, alien4_1_y))
            alien4_2_rect = alien3_2.get_rect(topleft = (alien4_2_x, alien4_2_y))
            alien4_3_rect = alien3_3.get_rect(topleft = (alien4_3_x, alien4_3_y))
            alien4_4_rect = alien3_4.get_rect(topleft = (alien4_4_x, alien4_4_y))
            alien4_5_rect = alien3_5.get_rect(topleft = (alien4_5_x, alien4_5_y))


            #if alien1_in_game:
                #for (i, el) in enumerate(alien1_in_game):
                    #screen.blit(alien1, el)
                    #el.x += 10
                    
                    #if el.x >= 1145:
                        #el.x -= 50
                    

                    #if el.x  < -800:
                        #alien1_in_game.pop(i)


                #if ship_rect.colliderect(el):
                    #gameplay = False
                

            


            if alien1_1_alive:
                if alien1_1_moving_right:
                    alien1_1_x += alien1_speed
                    alien1_1_y += alien1_speed_y
                    if alien1_1_x >= 1145:
                        alien1_1_moving_right = False
                else:
                    alien1_1_x -= alien1_speed
                    alien1_1_y += alien1_speed_y
                    if alien1_1_x < 0:
                        alien1_1_moving_right = True
                screen.blit(alien1_1, (alien1_1_x, alien1_1_y))
            if ship_rect.colliderect(alien1_1_rect):
                gameplay = False
                alien1_1_alive = False
                alien1_2_alive = False
                alien1_3_alive = False
                alien1_4_alive = False
                alien1_5_alive = False

            if alien1_2_alive:
                if alien1_2_moving_right:
                    alien1_2_x += alien1_speed
                    alien1_2_y += alien1_speed_y
                    if alien1_2_x >= 1145:
                        alien1_2_moving_right = False
                else:
                    alien1_2_x -= alien1_speed
                    alien1_2_y += alien1_speed_y
                    if alien1_2_x < 0:
                        alien1_2_moving_right = True
                screen.blit(alien1_2, (alien1_2_x, alien1_2_y))
            if ship_rect.colliderect(alien1_2_rect):
                gameplay = False
                alien1_1_alive = False
                alien1_2_alive = False
                alien1_3_alive = False
                alien1_4_alive = False
                alien1_5_alive = False

            if alien1_3_alive:
                if alien1_3_moving_right:
                    alien1_3_x += alien1_speed
                    alien1_3_y += alien1_speed_y
                    if alien1_3_x >= 1145:
                        alien1_3_moving_right = False
                else:
                    alien1_3_x -= alien1_speed
                    alien1_3_y += alien1_speed_y
                    if alien1_3_x < 0:
                        alien1_3_moving_right = True
                screen.blit(alien1_3, (alien1_3_x, alien1_3_y))
            if ship_rect.colliderect(alien1_3_rect):
                gameplay = False
                alien1_1_alive = False
                alien1_2_alive = False
                alien1_3_alive = False
                alien1_4_alive = False
                alien1_5_alive = False

            if alien1_4_alive:  
                if alien1_4_moving_right:
                    alien1_4_x += alien1_speed
                    alien1_4_y += alien1_speed_y
                    if alien1_4_x >= 1145:
                        alien1_4_moving_right = False
                else:
                    alien1_4_x -= alien1_speed
                    alien1_4_y += alien1_speed_y
                    if alien1_4_x < 0:
                        alien1_4_moving_right = True
                screen.blit(alien1_4, (alien1_4_x, alien1_4_y))
            if ship_rect.colliderect(alien1_4_rect):
                gameplay = False
                alien1_1_alive = False
                alien1_2_alive = False
                alien1_3_alive = False
                alien1_4_alive = False
                alien1_5_alive = False

            if alien1_5_alive:
                if alien1_5_moving_right:
                    alien1_5_x += alien1_speed
                    alien1_5_y += alien1_speed_y
                    if alien1_5_x >= 1145:
                        alien1_5_moving_right = False
                else:
                    alien1_5_x -= alien1_speed
                    alien1_5_y += alien1_speed_y
                    if alien1_5_x < 0:
                        alien1_5_moving_right = True
                screen.blit(alien1_5, (alien1_5_x, alien1_5_y))
            if ship_rect.colliderect(alien1_5_rect):
                gameplay = False
                alien1_1_alive = False
                alien1_2_alive = False
                alien1_3_alive = False
                alien1_4_alive = False
                alien1_5_alive = False






            if alien2_1_alive and alien1_all_dead:
                if alien2_1_moving_right:
                    alien2_1_x += alien2_speed
                    alien2_1_y += alien2_speed_y
                    if alien2_1_x >= 1145:
                        alien2_1_moving_right = False
                else:
                    alien2_1_x -= alien2_speed
                    alien2_1_y += alien2_speed_y
                    if alien2_1_x < 0:
                        alien2_1_moving_right = True
                screen.blit(alien2_1, (alien2_1_x, alien2_1_y))
            if ship_rect.colliderect(alien2_1_rect):
                gameplay = False
                alien2_1_alive = False
                alien2_2_alive = False
                alien2_3_alive = False
                alien2_4_alive = False
                alien2_5_alive = False

            if alien2_2_alive and alien1_all_dead:
                if alien2_2_moving_right:
                    alien2_2_x += alien2_speed
                    alien2_2_y += alien2_speed_y
                    if alien2_2_x >= 1145:
                        alien2_2_moving_right = False
                else:
                    alien2_2_x -= alien2_speed
                    alien2_2_y += alien2_speed_y
                    if alien2_2_x < 0:
                        alien2_2_moving_right = True
                screen.blit(alien2_2, (alien2_2_x, alien2_2_y))
            if ship_rect.colliderect(alien2_2_rect):
                gameplay = False
                alien2_1_alive = False
                alien2_2_alive = False
                alien2_3_alive = False
                alien2_4_alive = False
                alien2_5_alive = False

            if alien2_3_alive and alien1_all_dead:
                if alien2_3_moving_right:
                    alien2_3_x += alien2_speed
                    alien2_3_y += alien2_speed_y
                    if alien2_3_x >= 1145:
                        alien2_3_moving_right = False
                else:
                    alien2_3_x -= alien2_speed
                    alien2_3_y += alien2_speed_y
                    if alien2_3_x < 0:
                        alien2_3_moving_right = True
                screen.blit(alien2_3, (alien2_3_x, alien2_3_y))
            if ship_rect.colliderect(alien2_3_rect):
                gameplay = False
                alien2_1_alive = False
                alien2_2_alive = False
                alien2_3_alive = False
                alien2_4_alive = False
                alien2_5_alive = False

            if alien2_4_alive and alien1_all_dead:
                if alien2_4_moving_right:
                    alien2_4_x += alien2_speed
                    alien2_4_y += alien2_speed_y
                    if alien2_4_x >= 1145:
                        alien2_4_moving_right = False
                else:
                    alien2_4_x -= alien2_speed
                    alien2_4_y += alien2_speed_y
                    if alien2_4_x < 0:
                        alien2_4_moving_right = True
                screen.blit(alien2_4, (alien2_4_x, alien2_4_y))
            if ship_rect.colliderect(alien2_4_rect):
                gameplay = False
                alien2_1_alive = False
                alien2_2_alive = False
                alien2_3_alive = False
                alien2_4_alive = False
                alien2_5_alive = False

            if alien2_5_alive and alien1_all_dead:
                if alien2_5_moving_right:
                    alien2_5_x += alien2_speed
                    alien2_5_y += alien2_speed_y
                    if alien2_5_x >= 1145:
                        alien2_5_moving_right = False
                else:
                    alien2_5_x -= alien2_speed
                    alien2_5_y += alien2_speed_y
                    if alien2_5_x < 0:
                        alien2_5_moving_right = True
                screen.blit(alien2_5, (alien2_5_x, alien2_5_y))
            if ship_rect.colliderect(alien2_5_rect):
                gameplay = False
                alien2_1_alive = False
                alien2_2_alive = False
                alien2_3_alive = False
                alien2_4_alive = False
                alien2_5_alive = False






            if alien3_1_alive and alien2_all_dead: 
                if alien3_1_moving_right:
                    alien3_1_x += alien3_speed
                    alien3_1_y += alien3_speed_y
                    if alien3_1_x >= 1145:
                        alien3_1_moving_right = False
                else:
                    alien3_1_x -= alien3_speed
                    alien3_1_y += alien3_speed_y
                    if alien3_1_x < 0:
                        alien3_1_moving_right = True
                screen.blit(alien3_1, (alien3_1_x, alien3_1_y))
            if ship_rect.colliderect(alien3_1_rect):
                gameplay = False
                alien3_1_alive = False
                alien3_2_alive = False
                alien3_3_alive = False
                alien3_4_alive = False
                alien3_5_alive = False

            if alien3_2_alive and alien2_all_dead:
                if alien3_2_moving_right:
                    alien3_2_x += alien3_speed
                    alien3_2_y += alien3_speed_y
                    if alien3_2_x >= 1145:
                        alien3_2_moving_right = False
                else:
                    alien3_2_x -= alien3_speed
                    alien3_2_y += alien3_speed_y
                    if alien3_2_x < 0:
                        alien3_2_moving_right = True
                screen.blit(alien3_2, (alien3_2_x, alien3_2_y))
            if ship_rect.colliderect(alien3_2_rect):
                gameplay = False
                alien3_1_alive = False
                alien3_2_alive = False
                alien3_3_alive = False
                alien3_4_alive = False
                alien3_5_alive = False

            if alien3_3_alive and alien2_all_dead:
                if alien3_3_moving_right:
                    alien3_3_x += alien3_speed
                    alien3_3_y += alien3_speed_y
                    if alien3_3_x >= 1145:
                        alien3_3_moving_right = False
                else:
                    alien3_3_x -= alien3_speed
                    alien3_3_y += alien3_speed_y
                    if alien3_3_x < 0:
                        alien3_3_moving_right = True
                screen.blit(alien3_3, (alien3_3_x, alien3_3_y))
            if ship_rect.colliderect(alien3_3_rect):
                gameplay = False
                alien3_1_alive = False
                alien3_2_alive = False
                alien3_3_alive = False
                alien3_4_alive = False
                alien3_5_alive = False

            if alien3_4_alive and alien2_all_dead:
                if alien3_4_moving_right:
                    alien3_4_x += alien3_speed
                    alien3_4_y += alien3_speed_y
                    if alien3_4_x >= 1145:
                        alien3_4_moving_right = False
                else:
                    alien3_4_x -= alien3_speed
                    alien3_4_y += alien3_speed_y
                    if alien3_4_x < 0:
                        alien3_4_moving_right = True
                screen.blit(alien3_4, (alien3_4_x, alien3_4_y))
            if ship_rect.colliderect(alien3_4_rect):
                gameplay = False
                alien3_1_alive = False
                alien3_2_alive = False
                alien3_3_alive = False
                alien3_4_alive = False
                alien3_5_alive = False

            if alien3_5_alive and alien2_all_dead:
                if alien3_5_moving_right:
                    alien3_5_x += alien3_speed
                    alien3_5_y += alien3_speed_y
                    if alien3_5_x >= 1145:
                        alien3_5_moving_right = False
                else:
                    alien3_5_x -= alien3_speed
                    alien3_5_y += alien3_speed_y
                    if alien3_5_x < 0:
                        alien3_5_moving_right = True
                screen.blit(alien3_5, (alien3_5_x, alien3_5_y))
            if ship_rect.colliderect(alien3_5_rect):
                gameplay = False
                alien3_1_alive = False
                alien3_2_alive = False
                alien3_3_alive = False
                alien3_4_alive = False
                alien3_5_alive = False






            if alien4_1_alive and alien3_all_dead: 
                if alien4_1_moving_right:
                    alien4_1_x += alien4_speed
                    alien4_1_y += alien4_speed_y
                    if alien4_1_x >= 1145: 
                        alien4_1_moving_right = False
                else:
                    alien4_1_x -= alien4_speed
                    alien4_1_y += alien4_speed_y
                    if alien4_1_x < 0:
                        alien4_1_moving_right = True
                screen.blit(alien4_1, (alien4_1_x, alien4_1_y))
            if ship_rect.colliderect(alien4_1_rect):
                gameplay = False
                alien4_1_alive = False
                alien4_2_alive = False
                alien4_3_alive = False
                alien4_4_alive = False
                alien4_5_alive = False

            if alien4_2_alive and alien3_all_dead:
                if alien4_2_moving_right:
                    alien4_2_x += alien4_speed
                    alien4_2_y += alien4_speed_y
                    if alien4_2_x >= 1145:
                        alien4_2_moving_right = False
                else:
                    alien4_2_x -= alien4_speed
                    alien4_2_y += alien4_speed_y
                    if alien4_2_x < 0:
                        alien4_2_moving_right = True
                screen.blit(alien4_2, (alien4_2_x, alien4_2_y))
            if ship_rect.colliderect(alien4_2_rect):
                gameplay = False
                alien4_1_alive = False
                alien4_2_alive = False
                alien4_3_alive = False
                alien4_4_alive = False
                alien4_5_alive = False

            if alien4_3_alive and alien3_all_dead:
                if alien4_3_moving_right:
                    alien4_3_x += alien4_speed
                    alien4_3_y += alien4_speed_y
                    if alien4_3_x >= 1145:
                        alien4_3_moving_right = False
                else:
                    alien4_3_x -= alien4_speed
                    alien4_3_y += alien4_speed_y
                    if alien4_3_x < 0:
                        alien4_3_moving_right = True
                screen.blit(alien4_3, (alien4_3_x, alien4_3_y))
            if ship_rect.colliderect(alien4_3_rect):
                gameplay = False
                alien4_1_alive = False
                alien4_2_alive = False
                alien4_3_alive = False
                alien4_4_alive = False
                alien4_5_alive = False

            if alien4_4_alive and alien3_all_dead:
                if alien4_4_moving_right:
                    alien4_4_x += alien4_speed
                    alien4_4_y += alien4_speed_y
                    if alien4_4_x >= 1145:
                        alien4_4_moving_right = False
                else:
                    alien4_4_x -= alien4_speed
                    alien4_4_y += alien4_speed_y
                    if alien4_4_x < 0:
                        alien4_4_moving_right = True
                screen.blit(alien4_4, (alien4_4_x, alien4_4_y))
            if ship_rect.colliderect(alien4_4_rect):
                gameplay = False
                alien4_1_alive = False
                alien4_2_alive = False
                alien4_3_alive = False
                alien4_4_alive = False
                alien4_5_alive = False

            if alien4_5_alive and alien3_all_dead:
                if alien4_5_moving_right:
                    alien4_5_x += alien4_speed
                    alien4_5_y += alien4_speed_y
                    if alien4_5_x >= 1145:
                        alien4_5_moving_right = False
                else:
                    alien4_5_x -= alien4_speed
                    alien4_5_y += alien4_speed_y
                    if alien4_5_x < 0:
                        alien4_5_moving_right = True
                screen.blit(alien4_5, (alien4_5_x, alien4_5_y))
            if ship_rect.colliderect(alien4_5_rect):
                gameplay = False
                alien4_1_alive = False
                alien4_2_alive = False
                alien4_3_alive = False
                alien4_4_alive = False
                alien4_5_alive = False



            if bullets and bullets_count > 0:
                for i in range(len(bullets) - 1, -1, -1): 
                    el = bullets[i]
                    screen.blit(bullet, (el.x, el.y))
                    el.y -= bullet_speed

                    if el.y < 0:
                        bullets.pop(i)
                        continue

                    #if alien1_in_game:
                        #for (index, alien1_die) in enumerate(alien1_in_game):
                            #if el.colliderect(alien1_die):
                               # alien1_in_game.pop(index)
                                #bullets.pop(i)
                                

                    if alien1_1_alive and el.colliderect(pygame.Rect(alien1_1_x, alien1_1_y, 100, 100)):
                        alien1_1_alive = False 
                        if bullets:
                            bullets.pop(i)
                        explosion_active = True
                        explosion_pos = (alien1_1_x + 50, alien1_1_y + 50)
                        boom_anim_count = 0  
                        boom_anim_time = pygame.time.get_ticks() 

                    if alien1_2_alive and el.colliderect(pygame.Rect(alien1_2_x, alien1_2_y, 100, 100)):
                        alien1_2_alive = False 
                        if bullets:
                            bullets.pop(i)
                        explosion_active = True
                        explosion_pos = (alien1_2_x + 50, alien1_2_y + 50)
                        boom_anim_count = 0  
                        boom_anim_time = pygame.time.get_ticks() 
                            
                    if alien1_3_alive and el.colliderect(pygame.Rect(alien1_3_x, alien1_3_y, 100, 100)):
                        alien1_3_alive = False 
                        if bullets:
                            bullets.pop(i)
                        explosion_active = True
                        explosion_pos = (alien1_3_x + 50, alien1_3_y + 50)
                        boom_anim_count = 0  
                        boom_anim_time = pygame.time.get_ticks() 

                    if alien1_4_alive and el.colliderect(pygame.Rect(alien1_4_x, alien1_4_y, 100, 100)):
                        alien1_4_alive = False 
                        if bullets:
                            bullets.pop(i)
                        explosion_active = True
                        explosion_pos = (alien1_4_x + 50, alien1_4_y + 50)
                        boom_anim_count = 0  
                        boom_anim_time = pygame.time.get_ticks()

                    if alien1_5_alive and el.colliderect(pygame.Rect(alien1_5_x, alien1_5_y, 100, 100)):
                        alien1_5_alive = False 
                        if bullets:
                            bullets.pop(i)
                        explosion_active = True
                        explosion_pos = (alien1_5_x + 50, alien1_5_y + 50)
                        boom_anim_count = 0  
                        boom_anim_time = pygame.time.get_ticks() 


                    if (alien1_1_alive == False) and (alien1_2_alive == False) and (alien1_3_alive == False) and (alien1_4_alive == False) and (alien1_5_alive == False):
                        alien1_all_dead = True


                    if alien2_1_alive and alien1_all_dead and el.colliderect(pygame.Rect(alien2_1_x, alien2_1_y, 100, 100)):
                        if bullets:
                            bullets.pop(i)
                        alien2_1_count += 1
                        if alien2_1_count == 2:
                            alien2_1_alive = False
                            explosion_active = True
                            explosion_pos = (alien2_1_x + 50, alien2_1_y + 50)
                            boom_anim_count = 0  
                            boom_anim_time = pygame.time.get_ticks()

                    if alien2_2_alive and alien1_all_dead and el.colliderect(pygame.Rect(alien2_2_x, alien2_2_y, 100, 100)):
                        if bullets:
                            bullets.pop(i)
                        alien2_2_count += 1
                        if alien2_2_count == 2:
                            alien2_2_alive = False
                            explosion_active = True
                            explosion_pos = (alien2_2_x + 50, alien2_2_y + 50)
                            boom_anim_count = 0  
                            boom_anim_time = pygame.time.get_ticks()

                    if alien2_3_alive and alien1_all_dead and el.colliderect(pygame.Rect(alien2_3_x, alien2_3_y, 100, 100)):
                        if bullets:
                            bullets.pop(i)
                        alien2_3_count += 1
                        if alien2_3_count == 2:
                            alien2_3_alive = False
                            explosion_active = True
                            explosion_pos = (alien2_3_x + 50, alien2_3_y + 50)
                            boom_anim_count = 0  
                            boom_anim_time = pygame.time.get_ticks()

                    if alien2_4_alive and alien1_all_dead and el.colliderect(pygame.Rect(alien2_4_x, alien2_4_y, 100, 100)):
                        if bullets:    
                            bullets.pop(i)
                        alien2_4_count += 1
                        if alien2_4_count == 2:
                            alien2_4_alive = False
                            explosion_active = True
                            explosion_pos = (alien2_4_x + 50, alien2_4_y + 50)
                            boom_anim_count = 0  
                            boom_anim_time = pygame.time.get_ticks()

                    if alien2_5_alive and alien1_all_dead and el.colliderect(pygame.Rect(alien2_5_x, alien2_5_y, 100, 100)):
                        if bullets:    
                            bullets.pop(i)
                        alien2_5_count += 1
                        if alien2_5_count == 2:
                            alien2_5_alive = False
                            explosion_active = True
                            explosion_pos = (alien2_5_x + 50, alien2_5_y + 50)
                            boom_anim_count = 0  
                            boom_anim_time = pygame.time.get_ticks()

                    
                    if (alien2_1_alive == False) and (alien2_2_alive == False) and (alien2_3_alive == False) and (alien2_4_alive == False) and (alien2_5_alive == False):
                        alien2_all_dead = True

                    
                    if alien3_1_alive and alien2_all_dead and el.colliderect(pygame.Rect(alien3_1_x, alien3_1_y, 100, 100)):
                        if bullets:    
                            bullets.pop(i)
                        alien3_1_count += 1
                        if alien3_1_count == 3:
                            alien3_1_alive = False
                            explosion_active = True
                            explosion_pos = (alien3_1_x + 50, alien3_1_y + 50)
                            boom_anim_count = 0  
                            boom_anim_time = pygame.time.get_ticks()

                    if alien3_2_alive and alien2_all_dead and el.colliderect(pygame.Rect(alien3_2_x, alien3_2_y, 100, 100)):
                        if bullets:    
                            bullets.pop(i)
                        alien3_2_count += 1
                        if alien3_2_count == 3:
                            alien3_2_alive = False
                            explosion_active = True
                            explosion_pos = (alien3_2_x + 50, alien3_2_y + 50)
                            boom_anim_count = 0  
                            boom_anim_time = pygame.time.get_ticks()

                    if alien3_3_alive and alien2_all_dead and el.colliderect(pygame.Rect(alien3_3_x, alien3_3_y, 100, 100)):
                        if bullets:    
                            bullets.pop(i)
                        alien3_3_count += 1
                        if alien3_3_count == 3:
                            alien3_3_alive = False
                            explosion_active = True
                            explosion_pos = (alien3_3_x + 50, alien3_3_y + 50)
                            boom_anim_count = 0  
                            boom_anim_time = pygame.time.get_ticks()

                    if alien3_4_alive and alien2_all_dead and el.colliderect(pygame.Rect(alien3_4_x, alien3_4_y, 100, 100)):
                        if bullets:    
                            bullets.pop(i)
                        alien3_4_count += 1
                        if alien3_4_count == 3:
                            alien3_4_alive = False
                            explosion_active = True
                            explosion_pos = (alien3_4_x + 50, alien3_4_y + 50)
                            boom_anim_count = 0  
                            boom_anim_time = pygame.time.get_ticks()

                    if alien3_5_alive and alien2_all_dead and el.colliderect(pygame.Rect(alien3_5_x, alien3_5_y, 100, 100)):
                        if bullets:    
                            bullets.pop(i)
                        alien3_5_count += 1
                        if alien3_5_count == 3:
                            alien3_5_alive = False
                            explosion_active = True
                            explosion_pos = (alien3_5_x + 50, alien3_5_y + 50)
                            boom_anim_count = 0  
                            boom_anim_time = pygame.time.get_ticks()

                    
                    if (alien3_1_alive == False) and (alien3_2_alive == False) and (alien3_3_alive == False) and (alien3_4_alive == False) and (alien3_5_alive == False):
                        alien3_all_dead = True

                    
                    if alien4_1_alive and alien3_all_dead and el.colliderect(pygame.Rect(alien4_1_x, alien4_1_y, 100, 100)):
                        if bullets:    
                            bullets.pop(i)
                        alien4_1_count += 1
                        if alien4_1_count == 4:
                            alien4_1_alive = False
                            explosion_active = True
                            explosion_pos = (alien4_1_x + 50, alien4_1_y + 50)
                            boom_anim_count = 0  
                            boom_anim_time = pygame.time.get_ticks()

                    if alien4_2_alive and alien3_all_dead and el.colliderect(pygame.Rect(alien4_2_x, alien4_2_y, 100, 100)):
                        if bullets:    
                            bullets.pop(i)
                        alien4_2_count += 1
                        if alien4_2_count == 4:
                            alien4_2_alive = False
                            explosion_active = True
                            explosion_pos = (alien4_2_x + 50, alien4_2_y + 50)
                            boom_anim_count = 0  
                            boom_anim_time = pygame.time.get_ticks()

                    if alien4_3_alive and alien3_all_dead and el.colliderect(pygame.Rect(alien4_3_x, alien4_3_y, 100, 100)):
                        if bullets:    
                            bullets.pop(i)
                        alien4_3_count += 1
                        if alien4_3_count == 4:
                            alien4_3_alive = False
                            explosion_active = True
                            explosion_pos = (alien4_3_x + 50, alien4_3_y + 50)
                            boom_anim_count = 0  
                            boom_anim_time = pygame.time.get_ticks()

                    if alien4_4_alive and alien3_all_dead and el.colliderect(pygame.Rect(alien4_4_x, alien4_4_y, 100, 100)):
                        if bullets:    
                            bullets.pop(i)
                        alien4_4_count += 1
                        if alien4_4_count == 4:
                            alien4_4_alive = False
                            explosion_active = True
                            explosion_pos = (alien4_4_x + 50, alien4_4_y + 50)
                            boom_anim_count = 0  
                            boom_anim_time = pygame.time.get_ticks()

                    if alien4_5_alive and alien3_all_dead and el.colliderect(pygame.Rect(alien4_5_x, alien4_5_y, 100, 100)):
                        if bullets:    
                            bullets.pop(i)
                        alien4_5_count += 1
                        if alien4_5_count == 4:
                            alien4_5_alive = False
                            explosion_active = True
                            explosion_pos = (alien4_5_x + 50, alien4_5_y + 50)
                            boom_anim_count = 0  
                            boom_anim_time = pygame.time.get_ticks()


                    if (alien4_1_alive == False) and (alien4_2_alive == False) and (alien4_3_alive == False) and (alien4_4_alive == False) and (alien4_5_alive == False):
                        alien4_all_dead = True



                
            if explosion_active:
                current_time = pygame.time.get_ticks()
                if current_time - boom_anim_time > boom_anim_delay:
                    boom_anim_time = current_time
                    boom_anim_count += 1
                    if boom_anim_count >= len(boom_animation):
                        explosion_active = False  
                        boom_anim_count = 0
                if boom_anim_count < len(boom_animation):
                    explosion_frame = boom_animation[boom_anim_count]
                    explosion_rect = explosion_frame.get_rect(center=explosion_pos)  
                    screen.blit(explosion_frame, explosion_rect.topleft)
                if gameplay == False:
                    explosion_active = False



            if alien1_all_dead and alien2_all_dead and alien3_all_dead and alien4_all_dead:
                win = True
                
                

            if win:
                screen.blit(bg, (0, bg_y))
                screen.blit(bg, (0, bg_y + 720))
                bg_y -= 10
                if bg_y <= -720:
                    bg_y = 0  
            
                screen.blit(win_label, (400, 50))
                screen.blit(win_restart_label, (win_restart_label_rect))
                screen.blit(exit_label, (exit_label_rect))
                mouse = pygame.mouse.get_pos()
                
                if win_restart_label_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
                    
                    win = False


                    alien1_1_alive = True
                    alien1_2_alive = True
                    alien1_3_alive = True
                    alien1_4_alive = True
                    alien1_5_alive = True
                    alien1_all_dead = False
                    
                    alien1_1_x = 50
                    alien1_1_y = 50
                    alien1_2_x = 1000
                    alien1_2_y = 50
                    alien1_3_x = 500
                    alien1_3_y = 50
                    alien1_4_x = 750
                    alien1_4_y = 50
                    alien1_5_x = 250
                    alien1_5_y = 50

                    alien2_1_alive = True
                    alien2_2_alive = True
                    alien2_3_alive = True
                    alien2_4_alive = True
                    alien2_5_alive = True
                    alien2_all_dead = False

                    alien2_1_x = 50
                    alien2_1_y = 50
                    alien2_1_count = 0
                    alien2_2_x = 250
                    alien2_2_y = 50
                    alien2_2_count = 0
                    alien2_3_x = 500
                    alien2_3_y = 50
                    alien2_3_count = 0
                    alien2_4_x = 750
                    alien2_4_y = 50
                    alien2_4_count = 0
                    alien2_5_x = 1000
                    alien2_5_y = 50
                    alien2_5_count = 0

                    alien3_1_alive = True
                    alien3_2_alive = True
                    alien3_3_alive = True
                    alien3_4_alive = True
                    alien3_5_alive = True
                    alien3_all_dead = False

                    alien3_1_x = 50
                    alien3_1_y = 50
                    alien3_1_count = 0
                    alien3_2_x = 250
                    alien3_2_y = 50
                    alien3_2_count = 0
                    alien3_3_x = 500
                    alien3_3_y = 50
                    alien3_3_count = 0
                    alien3_4_x = 750
                    alien3_4_y = 50
                    alien3_4_count = 0
                    alien3_5_x = 1000
                    alien3_5_y = 50
                    alien3_5_count = 0

                    alien4_1_alive = True
                    alien4_2_alive = True
                    alien4_3_alive = True
                    alien4_4_alive = True
                    alien4_5_alive = True
                    alien4_all_dead = False

                    alien4_1_x = 50
                    alien4_1_y = 50
                    alien4_1_count = 0
                    alien4_2_x = 250
                    alien4_2_y = 50
                    alien4_2_count = 0
                    alien4_3_x = 500
                    alien4_3_y = 50
                    alien4_3_count = 0
                    alien4_4_x = 750
                    alien4_4_y = 50
                    alien4_4_count = 0
                    alien4_5_x = 1000
                    alien4_5_y = 50
                    alien4_5_count = 0

                    gameplay = True
                    ship_x = 550
                    bullets.clear()

                elif exit_label_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
                    running = False
                    pygame.quit()


        if not gameplay and not win:
            screen.blit(bg, (0, bg_y))
            screen.blit(bg, (0, bg_y + 720))
            bg_y -= 10
            if bg_y <= -720:
                bg_y = 0  
            screen.blit(lose_label, (425, 50))           
            screen.blit(restart_label, (restart_label_rect))  
            screen.blit(exit_label, (exit_label_rect))
            

            mouse = pygame.mouse.get_pos()
            if restart_label_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
                gameplay = True
                ship_x = 550
                bullets.clear()
                
                alien1_1_alive = True
                alien1_2_alive = True
                alien1_3_alive = True
                alien1_4_alive = True
                alien1_5_alive = True
                alien1_all_dead = False
                
                alien1_1_x = 50
                alien1_1_y = 50
                alien1_2_x = 1000
                alien1_2_y = 50
                alien1_3_x = 500
                alien1_3_y = 50
                alien1_4_x = 750
                alien1_4_y = 50
                alien1_5_x = 250
                alien1_5_y = 50

                alien2_1_alive = True
                alien2_2_alive = True
                alien2_3_alive = True
                alien2_4_alive = True
                alien2_5_alive = True
                alien2_all_dead = False

                alien2_1_x = 50
                alien2_1_y = 50
                alien2_1_count = 0
                alien2_2_x = 250
                alien2_2_y = 50
                alien2_2_count = 0
                alien2_3_x = 500
                alien2_3_y = 50
                alien2_3_count = 0
                alien2_4_x = 750
                alien2_4_y = 50
                alien2_4_count = 0
                alien2_5_x = 1000
                alien2_5_y = 50
                alien2_5_count = 0

                alien3_1_alive = True
                alien3_2_alive = True
                alien3_3_alive = True
                alien3_4_alive = True
                alien3_5_alive = True
                alien3_all_dead = False

                alien3_1_x = 50
                alien3_1_y = 50
                alien3_1_count = 0
                alien3_2_x = 250
                alien3_2_y = 50
                alien3_2_count = 0
                alien3_3_x = 500
                alien3_3_y = 50
                alien3_3_count = 0
                alien3_4_x = 750
                alien3_4_y = 50
                alien3_4_count = 0
                alien3_5_x = 1000
                alien3_5_y = 50
                alien3_5_count = 0

                alien4_1_alive = True
                alien4_2_alive = True
                alien4_3_alive = True
                alien4_4_alive = True
                alien4_5_alive = True
                alien4_all_dead = False

                alien4_1_x = 50
                alien4_1_y = 50
                alien4_1_count = 0
                alien4_2_x = 250
                alien4_2_y = 50
                alien4_2_count = 0
                alien4_3_x = 500
                alien4_3_y = 50
                alien4_3_count = 0
                alien4_4_x = 750
                alien4_4_y = 50
                alien4_4_count = 0
                alien4_5_x = 1000
                alien4_5_y = 50
                alien4_5_count = 0

            elif exit_label_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
                running = False
                pygame.quit()    

    pygame.display.update() 