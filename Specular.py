import pygame, sys
import pyganim, PyIgnition
import sprites
import math, random
from pygame.locals import *

pygame.init()

# colors
BACKGROUND = (30,0,0)
# maximum speed of player
MAXSPEED = 10
# how fast player gains speed, must be dividable with friction
ACCELERATION = 0.4
# how fast objects stop
FRICTION = 0.1
# how fast projectiles fly
PROJSPEED = 20
# how long projectiles exist
PROJTIME = 180
# how often a projectile can be fired
PROJDELAY = 8
# the speed that enemies move at
ENEMYSPEED = 2

#,pygame.FULLSCREEN


screen = pygame.display.set_mode((0,0))
pygame.display.set_icon(pygame.image.load('./Textures/Icon.png'))
pygame.display.set_caption('Specular')
pygame.key.set_repeat(10, 10)
clock = pygame.time.Clock()

# load files
cursor = pygame.image.load('./Textures/Cursor2.png').convert_alpha()

distance = pygame.image.load('./Textures/Background.png').convert_alpha()

title = pygame.image.load('./Textures/Title.png').convert_alpha()
playbutton = pygame.image.load('./Textures/PlayButton.png').convert_alpha()
playpressed = pygame.image.load('./Textures/PlayPressed.png').convert_alpha()
optionbutton = pygame.image.load('./Textures/OptionsButton.png').convert_alpha()
optionpressed = pygame.image.load('./Textures/OptionsPressed.png').convert_alpha()
exitbutton = pygame.image.load('./Textures/ExitButton.png').convert_alpha()
exitpressed = pygame.image.load('./Textures/ExitPressed.png').convert_alpha()

speedmeter = pygame.image.load('./Textures/OptionsMeter.png').convert_alpha()
accelerationmeter = pygame.image.load('./Textures/OptionsMeter.png').convert_alpha()
frictionmeter = pygame.image.load('./Textures/OptionsMeter.png').convert_alpha()
speedslider = pygame.image.load('./Textures/Slider.png').convert_alpha()
speed = pygame.image.load('./Textures/Maxspeed.png').convert_alpha()
accelerationslider = pygame.image.load('./Textures/Slider.png').convert_alpha()
acceleration = pygame.image.load('./Textures/Acceleration.png').convert_alpha()
frictionslider = pygame.image.load('./Textures/Slider.png').convert_alpha()
friction = pygame.image.load('./Textures/Friction.png').convert_alpha()
backbutton = pygame.image.load('./Textures/BackButton.png').convert_alpha()
backpressed = pygame.image.load('./Textures/BackPressed.png').convert_alpha()

scorehud = pygame.image.load('./Textures/ScoreHUD.png').convert_alpha()

lose = pygame.image.load('./Textures/Lose.png').convert_alpha()

# menumusic = pygame.mixer.Sound('./Audio/04.ogg')
# gamemusic = [pygame.mixer.Sound('./Audio/02.ogg'),
#			 pygame.mixer.Sound('./Audio/03.ogg'),
#			 pygame.mixer.Sound('./Audio/06.ogg'),
#			 pygame.mixer.Sound('./Audio/08.ogg')]

# get screen dimensions
width = screen.get_width()
height = screen.get_height()
screencenterx = screen.get_width() / 2
screencentery = screen.get_height() / 2

# pixel array
pixArray = pygame.PixelArray(screen)
pixArray[width - 20][height - 20] = (0,0,0)
del pixArray

# enable audio
#pygame.mixer.init(frequency=22050, size=-16, channels=8, buffer=4096)
#pygame.mixer.volume = 0.5
#menumusic.play()

# create cursor
cursorrect = cursor.get_rect()
pygame.mouse.set_visible(False)

# create menu buttons
titlerect = title.get_rect()
playbuttonrect = playbutton.get_rect()
optionbuttonrect = optionbutton.get_rect()
exitbuttonrect = exitbutton.get_rect()

titlerect.center = (screencenterx, screencentery)
playbuttonrect.center = (screencenterx, screencentery + 60)
optionbuttonrect.center = (screencenterx, screencentery + 230)
exitbuttonrect.center = (screencenterx, screencentery + 290)

def detect_mouseover(buttonrect, buttonpressed):
    if buttonrect.collidepoint(pygame.mouse.get_pos()):
        screen.blit(buttonpressed, buttonrect)

def detect_button_press(button, mode, newmode):
    if button.collidepoint(pygame.mouse.get_pos()) and event.type == MOUSEBUTTONDOWN:
        return newmode
    else:
        return mode

# create option buttons
backbuttonrect = backbutton.get_rect()
speedmeterrect = speedmeter.get_rect()
accelerationmeterrect = accelerationmeter.get_rect()
frictionmeterrect = frictionmeter.get_rect()
speedsliderrect = speedslider.get_rect()
accelerationsliderrect = accelerationslider.get_rect()
frictionsliderrect = frictionslider.get_rect()
speedrect = speed.get_rect()
frictionrect = friction.get_rect()
accelerationrect = acceleration.get_rect()

backbuttonrect.center = (screencenterx, screencentery + 330)
speedmeterrect.center = (screencenterx, screencentery - 100)
speedsliderrect.center = (screencenterx, screencentery - 100)
accelerationmeterrect.center = (screencenterx, screencentery)
accelerationsliderrect.center = (screencenterx, screencentery)
frictionmeterrect.center = (screencenterx, screencentery + 100)
frictionsliderrect.center = (screencenterx, screencentery + 100)
speedrect.center = (screencenterx, screencentery - 130)
accelerationrect.center = (screencenterx, screencentery - 30)
frictionrect.center = (screencenterx, screencentery + 70)

def slider_movement(slider, screencenterx, location):
    (X,Y) = slider.center
    (mouse_X, mouse_Y) = pygame.mouse.get_pos()
    (button1, button2, button3) = pygame.mouse.get_pressed()
    if slider.collidepoint(pygame.mouse.get_pos()) and button1 == True:
        slider.center = (mouse_X, location)
    if X < screencenterx - 227:
        slider.center = (screencenterx - 227, location)
    if X > screencenterx + 227:
        slider.center = (screencenterx + 227, location)

def get_slider_value(slider, screencenterx):
    (X,Y) = slider.center
    return X - screencenterx

# create lose screen
loserect = lose.get_rect()
loserect.center = (screencenterx, screencentery)

# create player entity
player = sprites.Player((screencenterx, screencentery))
player.shadowrect.center = (screencenterx,screencentery)
nospawn = pygame.Rect(screencenterx - 300, screencentery - 300, 600, 600)
shockwaverect = pygame.Rect(screencenterx - 750, screencentery - 750, 1500, 1500)
playerspeed_X = 0
playerspeed_Y = 0
playermovement_X = 0
playermovement_Y = 0

def destroy_player():
    X, Y = screencenterx, screencentery
    source3.CreateKeyframe(source3.curframe + 1, pos = (X, Y), particlesperframe = 320)
    source4.CreateKeyframe(source4.curframe + 1, pos = (X, Y), particlesperframe = 160)
    source3.CreateKeyframe(source3.curframe + 2, pos = (X, Y), particlesperframe = 0)
    source4.CreateKeyframe(source4.curframe + 2, pos = (X, Y), particlesperframe = 0)

# create enemy entities
enemies = pygame.sprite.Group()
enemyincrease = 2
enemyamount = 0

def create_enemy(rect, offset, lives, enemytype):
    X = random.randint(rect.left, rect.right)
    Y = random.randint(rect.top, rect.bottom)
    enemy = sprites.Enemy((X, Y), lives, enemytype, random.randint(-offset, offset))
    if nospawn.colliderect(enemy.rect) == False:
        enemies.add(enemy)

def destroy_enemy(enemy, offset_X, offset_Y):
    enemy.kill()
    X, Y = enemy.rect.center
    X -= offset_X
    Y -= offset_Y
    source1.CreateKeyframe(source1.curframe + 1, pos = (X, Y), particlesperframe = 10)
    source2.CreateKeyframe(source2.curframe + 1, pos = (X, Y), particlesperframe = 5)
    source1.CreateKeyframe(source1.curframe + 2, pos = (X, Y), particlesperframe = 0)
    source2.CreateKeyframe(source2.curframe + 2, pos = (X, Y), particlesperframe = 0)
    source1.CreateParticleKeyframe(60, colour = (0,0,0,0))
    source2.CreateParticleKeyframe(60, colour = (0,0,0,0))

def destroy_enemy_lv2(enemy, offset_X, offset_Y):
    enemy.kill()
    X, Y = enemy.rect.center
    X -= offset_X
    Y -= offset_Y
    source5.CreateKeyframe(source5.curframe + 1, pos = (X, Y), particlesperframe = 10)
    source6.CreateKeyframe(source6.curframe + 1, pos = (X, Y), particlesperframe = 5)
    source5.CreateKeyframe(source5.curframe + 2, pos = (X, Y), particlesperframe = 0)
    source6.CreateKeyframe(source6.curframe + 2, pos = (X, Y), particlesperframe = 0)

def cripple_enemy(enemy, offset_X, offset_Y):
    X, Y = enemy.rect.center
    X -= offset_X
    Y -= offset_Y
    source5.CreateKeyframe(source5.curframe + 1, pos = (X, Y), particlesperframe = 2)
    source6.CreateKeyframe(source6.curframe + 1, pos = (X, Y), particlesperframe = 1)
    source5.CreateKeyframe(source5.curframe + 2, pos = (X, Y), particlesperframe = 0)
    source6.CreateKeyframe(source6.curframe + 2, pos = (X, Y), particlesperframe = 0)

# create powerups
powerups = pygame.sprite.Group()
multiplier = 1
multiplierexist = 0

def create_powerup(rect):
    X = random.randint(rect.left, rect.right)
    Y = random.randint(rect.top, rect.bottom)
    powerup = sprites.Powerup((X,Y), 600)
    powerups.add(powerup)

# create particle effects
smalleffect = PyIgnition.ParticleEffect(screen)
source1 = smalleffect.CreateSource(initspeed = 7.0, initspeedrandrange = 1, initdirectionrandrange = 3.3, particlelife = 60, drawtype = PyIgnition.DRAWTYPE_IMAGE, imagepath = './Enemy1/smallParticle.png')
source2 = smalleffect.CreateSource(initspeed = 5.0, initspeedrandrange = 1, initdirectionrandrange = 3.3, particlelife = 60, drawtype = PyIgnition.DRAWTYPE_IMAGE, imagepath = './Enemy1/largeParticle.png')

largeeffect = PyIgnition.ParticleEffect(screen)
source5 = largeeffect.CreateSource(initspeed = 7.0, initspeedrandrange = 1, initdirectionrandrange = 3.3, particlelife = 60, drawtype = PyIgnition.DRAWTYPE_IMAGE, imagepath = './Enemy2/smallParticle.png')
source6 = largeeffect.CreateSource(initspeed = 5.0, initspeedrandrange = 1, initdirectionrandrange = 3.3, particlelife = 60, drawtype = PyIgnition.DRAWTYPE_IMAGE, imagepath = './Enemy2/largeParticle.png')

deatheffect = PyIgnition.ParticleEffect(screen)
source3 = deatheffect.CreateSource(initspeed = 8.0, initspeedrandrange = 1, initdirectionrandrange = 3.3, particlelife = 120, drawtype = PyIgnition.DRAWTYPE_IMAGE, imagepath = './Player/PlayerParticle.png')
source4 = deatheffect.CreateSource(initspeed = 6.0, initspeedrandrange = 1, initdirectionrandrange = 3.3, particlelife = 120, drawtype = PyIgnition.DRAWTYPE_IMAGE, imagepath = './Player/PlayerParticle1.png')


# create projectile entities
projectiles = pygame.sprite.Group()
firingdelay = PROJDELAY
weapon2delay = PROJDELAY
weapon2time = 0
weapon2angle = 0

def create_projectile(offset):
    projectile = sprites.Projectile(player.rect.center)
    projectile.direction += offset
    projectile.time = PROJTIME
    projectiles.add(projectile)
    #firesound.play()

def create_wave(offset):
    projectile = sprites.Projectile(player.rect.center)
    projectile.direction = offset
    projectile.time = PROJTIME
    projectiles.add(projectile)


# create HUD
font = pygame.font.Font('./Font/Battlev2l.ttf', 60)
font2 = pygame.font.Font('./Font/Battlev2l.ttf', 20)
scorehudrect = scorehud.get_rect()

scorehudrect.midtop = (screencenterx,0)

# game background
distancerect = distance.get_rect()

# game mode
mode = 0

# game loop
while True:

    # clear
    screen.fill(BACKGROUND)

    # exit
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # game loop
    if mode == 1:

        # acceleration and topspeed
        key = pygame.key.get_pressed()

        if key [pygame.K_w] and playerspeed_Y > -MAXSPEED:
            playerspeed_Y -= ACCELERATION
        if key [pygame.K_s] and playerspeed_Y < MAXSPEED:
            playerspeed_Y += ACCELERATION
        if key [pygame.K_a] and playerspeed_X > -MAXSPEED:
            playerspeed_X -= ACCELERATION
        if key [pygame.K_d] and playerspeed_X < MAXSPEED:
            playerspeed_X += ACCELERATION

        # friction
        if playerspeed_X > 0:
            playerspeed_X -= FRICTION
        if playerspeed_Y > 0:
            playerspeed_Y -= FRICTION
        if playerspeed_X < -0:
            playerspeed_X += FRICTION
        if playerspeed_Y < -0:
            playerspeed_Y += FRICTION

        # boundaries
        borderleft, bordertop = distancerect.topleft
        borderright, bordeerbottom = distancerect.bottomright
        if player.rect.top < bordertop and playerspeed_Y < 0:
            playerspeed_Y = -playerspeed_Y
        if player.rect.bottom > bordeerbottom and playerspeed_Y > 0:
            playerspeed_Y = -playerspeed_Y
        if player.rect.left < borderleft and playerspeed_X < 0:
            playerspeed_X = -playerspeed_X
        if player.rect.right > borderright and playerspeed_X > 0:
            playerspeed_X = -playerspeed_X

        # update player
        if player.life == 3:
            player.anim1.play()
            player.anim2.play()
        if player.life == 2:
            player.anim1.play()
            player.anim2.pause()
        if player.life == 1:
            player.anim1.pause()
        if player.life <= 0:
            mode = -3
            sprites.shockwave.play()
            destroy_player()

        playermovement_X -= playerspeed_X
        playermovement_Y -= playerspeed_Y

        # update cursor
        cursorrect.center = (pygame.mouse.get_pos())

        # level background
        screen.blit(distance, distancerect)
        distancerect.center = (playermovement_X, playermovement_Y)

        # update particle effects
        smalleffect.pos = (playermovement_X, playermovement_Y)
        largeeffect.pos = (playermovement_X, playermovement_Y)
        smalleffect.Update()
        largeeffect.Update()
        deatheffect.Update()
        smalleffect.Redraw()
        largeeffect.Redraw()
        deatheffect.Redraw()

        # update weapons
        firingdelay -= 1
        weapon2delay -= 1
        if weapon2delay < 0: weapon2delay = 0

        (button1, button2, button3) = pygame.mouse.get_pressed()
        if button1 == True and firingdelay < 1:
            create_projectile(0)
            firingdelay = PROJDELAY

        elif button3 == True and weapon2delay < 60:
            weapon2time = 60

        if weapon2time > 0:
            create_projectile(weapon2angle + 2.1)
            create_projectile(weapon2angle + 1.1)
            create_projectile(weapon2angle + 0)
            create_projectile(weapon2angle - 1.1)
            create_projectile(weapon2angle - 2.2)
            create_projectile(weapon2angle - 3.3)
            weapon2delay = 600
            weapon2time -= 1
            weapon2angle += 0.2

        if firingdelay == PROJDELAY - 2:
            create_projectile(0.04)
            create_projectile(-0.04)

        for projectile in projectiles:
            projmove_X, projmove_Y = sprites.calculate_angular_movement(projectile.co, projectile.direction, PROJSPEED)
            projectile.co = (projmove_X - playerspeed_X, projmove_Y - playerspeed_Y)
            projectile.rect.center = projectile.co
            screen.blit(projectile.image, projectile.rect)
            projectile.time -= 1
            if projectile.time == 0:
                projectile.kill()

        # update enemies
        enemyincrease += 0.005
        if enemyamount < enemyincrease and random.randint(0,10) == 1:
            create_enemy(distancerect, 1, 2, sprites.enemy_lv1)
            enemyamount += 1

        if enemyamount < enemyincrease and enemyincrease > 8 and random.randint(0,100) == 1:
            create_enemy(distancerect, 0, 4, sprites.enemy_lv2)
            enemyamount += 1

        for enemy in enemies:
            enemymove_X, enemymove_Y = sprites.calculate_angular_movement(enemy.co, sprites.angle_to_player(enemy.rect.center, player.rect.center) + enemy.offset, ENEMYSPEED)
            enemy.co = (enemymove_X - playerspeed_X, enemymove_Y - playerspeed_Y)
            enemy.rect.center = enemy.co
            enemy.anim.blit(screen, enemy.rect)

            if distancerect.contains(enemy.rect) == False:
                enemy.offset = -enemy.offset

            if enemy.rect.colliderect(player.rect):
                player.life -= 1
                enemyamount -= 1
                if enemy.score == 4:
                    destroy_enemy_lv2(enemy, playermovement_X, playermovement_Y)
                else:
                    destroy_enemy(enemy, playermovement_X, playermovement_Y)

            for projectile in projectiles:
                if enemy.rect.collidepoint(projectile.rect.center):
                    enemy.life -= 1
                    if enemy.score == 4:
                        cripple_enemy(enemy, playermovement_X, playermovement_Y)
                    projectile.kill()
                    if enemy.life <= 0:
                        if enemy.score == 4:
                            destroy_enemy_lv2(enemy, playermovement_X, playermovement_Y)
                        else:
                            destroy_enemy(enemy, playermovement_X, playermovement_Y)
                        enemyamount -= 1
                        score += enemy.score * multiplier

            if player.life <= 0:
                if enemy.score == 4:
                    destroy_enemy_lv2(enemy, playermovement_X, playermovement_Y)
                else:
                    destroy_enemy(enemy, playermovement_X, playermovement_Y)
                enemyamount -= 1
                score += enemy.score * multiplier

        # update powerups
        multiplierexist -= 0.001
        if multiplierexist < 1:
            if random.randint(0,1) == 1:
                create_powerup(distancerect)
                multiplierexist += 1
        for powerup in powerups:
            powerup.timer -= 1
            if powerup.timer < 0:
                powerup.kill()
            powerup.rect.center = (playermovement_X - powerup.X ,playermovement_Y - powerup.Y)
            screen.blit(powerup.image,powerup.rect)
            if powerup.rect.colliderect(player.rect):
                multiplier += 1
        if multiplier > 1:
            multiplier -= 0.1


        # update screen
        screen.blit(player.shadow, player.shadowrect)
        player.anim1.blit(screen, player.rect)
        player.anim2.blit(screen, player.rect)
        screen.blit(player.image, player.rect)
        screen.blit(cursor, cursorrect)

        # update HUD
        screen.blit(scorehud, scorehudrect)
        scorestring = font.render('%s' %(score), 1, (140, 0, 0))
        scorestringrect = scorestring.get_rect()
        scorestringrect.midtop = (screencenterx, 0)
        multiplierstring = font2.render('x%s' %(multiplier), 1, (140,0,0))
        multiplierstringrect = multiplierstring.get_rect()
        multiplierstringrect.midtop = (screencenterx + 300, 60)
        screen.blit(scorestring, scorestringrect)
        screen.blit(multiplierstring, multiplierstringrect)

        # update modes
        if key [pygame.K_ESCAPE]:
            mode = -2

    # start menu loop
    elif mode == 0:

        # update screen
        screen.blit(title, titlerect)
        screen.blit(playbutton, playbuttonrect)
        screen.blit(optionbutton, optionbuttonrect)
        screen.blit(exitbutton, exitbuttonrect)

        # detect buttonpresses
        detect_mouseover(playbuttonrect, playpressed)
        mode = detect_button_press(playbuttonrect, mode, 1)
        detect_mouseover(optionbuttonrect, optionpressed)
        mode = detect_button_press(optionbuttonrect, mode, -1)
        detect_mouseover(exitbuttonrect, exitpressed)
        if exitbuttonrect.collidepoint(pygame.mouse.get_pos()) and event.type == MOUSEBUTTONDOWN:
            pygame.quit()
            sys.exit()

        # cursor
        cursorrect.center = (pygame.mouse.get_pos())
        screen.blit(cursor, cursorrect)

        # start game
        if mode == 1:
            loseshow = 120
            #pygame.mixer.fadeout(3000)
            #gamemusic[random.randint(0, 3)].play(loops = -1)
            player.life = 3
            score = 0
            firingdelay = PROJDELAY
            playerspeed_X = 0
            playerspeed_Y = 0
            playermovement_X = screencenterx
            playermovement_Y = screencentery
            enemyamount = 0
            enemyincrease = 2
            for enemy in enemies:
                enemy.kill()

    # option menu loop
    elif mode == -1:

        # update screen
        screen.blit(speed, speedrect)
        screen.blit(acceleration, accelerationrect)
        screen.blit(friction, frictionrect)
        screen.blit(backbutton, backbuttonrect)
        screen.blit(speedmeter, speedmeterrect)
        screen.blit(accelerationmeter, accelerationmeterrect)
        screen.blit(frictionmeter, frictionmeterrect)
        screen.blit(speedslider, speedsliderrect)
        screen.blit(accelerationslider, accelerationsliderrect)
        screen.blit(frictionslider, frictionsliderrect)

        # detect changes
        slider_movement(speedsliderrect, screencenterx, screencentery - 100)
        slider_movement(accelerationsliderrect, screencenterx, screencentery)
        slider_movement(frictionsliderrect, screencenterx, screencentery + 100)
        detect_mouseover(backbuttonrect, backpressed)
        mode = detect_button_press(backbuttonrect, mode, 0)

        # update settings
        MAXSPEED = (get_slider_value(speedsliderrect, screencenterx) / 22.7) + 10
        ACCELERATION = (get_slider_value(accelerationsliderrect, screencenterx) / 567.5) + 0.4
        FRICTION = (get_slider_value(frictionsliderrect, screencenterx) / 1135) + 0.2

        # cursor
        cursorrect.center = (pygame.mouse.get_pos())
        screen.blit(cursor, cursorrect)

    # pause menu
    elif mode == -2:

        # update screen
        screen.blit(playbutton, playbuttonrect)
        screen.blit(exitbutton, exitbuttonrect)

        # detect buttonpresses
        detect_mouseover(playbuttonrect, playpressed)
        mode = detect_button_press(playbuttonrect, mode, 1)
        detect_mouseover(exitbuttonrect, exitpressed)
        if exitbuttonrect.collidepoint(pygame.mouse.get_pos()) and event.type == MOUSEBUTTONDOWN:
            pygame.quit()
            sys.exit()

        # cursor
        cursorrect.center = (pygame.mouse.get_pos())
        screen.blit(cursor, cursorrect)

    # lose screen
    elif mode == -3:

        # update stuff
        loseshow -= 1

        # update cursor
        cursorrect.center = (pygame.mouse.get_pos())

        # detect changes
        (button1, button2, button3) = pygame.mouse.get_pressed()
        if button1 == True and loseshow < 0:
            mode = 0

        # level background
        screen.blit(distance, distancerect)

        # update projectiles
        for projectile in projectiles:
            projmove_X, projmove_Y = sprites.calculate_angular_movement(projectile.co, projectile.direction, PROJSPEED)
            projectile.co = (projmove_X + playermovement_X, projmove_Y + playermovement_Y)
            projectile.rect.center = projectile.co
            screen.blit(projectile.image, projectile.rect)
            projectile.time -= 1
            if projectile.time == 0:
                projectile.kill()

        # update particle effects
        smalleffect.Update()
        deatheffect.Update()
        smalleffect.Redraw()
        deatheffect.Redraw()

        # update screen
        screen.blit(cursor, cursorrect)
        for enemy in enemies:
            enemy.anim.blit(screen, enemy.rect)
        sprites.shockwave.blit(screen,shockwaverect)
        screen.blit(lose,loserect)

        scorestring = font.render('score: %s' %(score), 1, (150, 0, 0))
        scorestringrect = scorestring.get_rect()
        scorestringrect.midtop = (screencenterx, screencentery + 80)
        screen.blit(scorestring, scorestringrect)

    pygame.display.update()

    # framerate
    clock.tick(60)


