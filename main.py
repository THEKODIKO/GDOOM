import pygame as pp
import math



#initialising pygame module
pp.init()


#defining window and its properties
screen = pp.display.set_mode((1300,750))
pp.display.set_caption("GDOOM")
gameIcon = pp.image.load('./imgSource/medal.png')
pp.display.set_icon(gameIcon)
over_font = pp.font.Font('freesansbold.ttf', 59)


def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX - bulletX, 2) + (math.pow(enemyY - bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False

    



player1 = pp.image.load('./imgSource/Player1.png')
player1_x = 400
player1_y = 300
player1_xc = 0
player1_yc = 0


health1 = 100
health2 = 100

player2 = pp.image.load('./imgSource/Player2.png')
player2_x = 800
player2_y = 300
player2_xc = 0
player2_yc = 0

bulletRig = pp.image.load('./imgSource/bullRig.png')
bull_x = player2_x
bull_y = player2_y
bull_xc = 0
bulletLef = pp.image.load('./imgSource/bullLef.png')
bull_xl = player2_x
bull_yl = player2_y
bull_xcl = 0

bullet2Rig = pp.image.load('./imgSource/bullRig.png')
bull2_x = player1_x
bull2_y = player1_y
bull2_xc = 0

shoot = False
shoot2 = False

running = True

while running:
    screen.fill((0, 0, 0,0))
    screen.blit(player1,(player1_x,player1_y))
    screen.blit(player2,(player2_x,player2_y))
    screen.blit(bulletLef,(int(bull_x),int(player2_y)))
    screen.blit(bulletRig,(int(bull2_x),int(player1_y)))
    for event in pp.event.get():
        if event.type == pp.QUIT:
            running = False
        if event.type == pp.KEYDOWN:
            if event.key == pp.K_RIGHT:
                player2_xc += 5
            if event.key == pp.K_LEFT:
                player2_xc -= 5
            if event.key == pp.K_d:
                player1_xc += 5
            if event.key == pp.K_a:
                player1_xc -= 5
            if event.key == pp.K_w:
                player1_yc -= 5
            if event.key == pp.K_s:
                player1_yc += 5
            if event.key == pp.K_UP:
                player2_yc -= 5
            if event.key == pp.K_DOWN:
                player2_yc +=5
            if event.key == pp.K_k:
                shoot = True
            if event.key == pp.K_c:
                shoot2 = True
                

        if event.type == pp.KEYUP:
            if event.key == pp.K_w:
                player1_yc = 0
            if event.key == pp.K_s:
                player1_yc =0
            if event.key == pp.K_UP:
                player2_yc = 0
            if event.key == pp.K_DOWN:
                player2_yc =0
            if event.key == pp.K_RIGHT:
                player2_xc = 0
            if event.key == pp.K_LEFT:
                player2_xc = 0
            if event.key == pp.K_d:
                player1_xc = 0
            if event.key == pp.K_a:
                player1_xc = 0
            if event.key == pp.K_k:
                pass
            if event.key == pp.K_c:     
                pass

    if shoot == True:
        bull_xc-=0.1
        bull_x += bull_xc
    if shoot == False:
        bull_x = player2_x
    
    if shoot2 == True:
        bull2_xc+=0.1
        bull2_x += bull2_xc
    if shoot2 == False:
        bull2_x = player1_x

    player1_x+=player1_xc
    player2_x+=player2_xc
    player1_y+=player1_yc
    player2_y+=player2_yc

    if bull_x<=0:
        bull_x = player2_x
        shoot=False 
    if bull_x>=1300:
        bull_x = player2_x
        shoot=False

    if bull2_x<=0:
        bull2_x = player1_x
        shoot2=False 
    if bull2_x>=1300:
        bull2_x = player1_x
        shoot2=False

    if player1_x >= 1300:player1_x =0
    elif player1_x <= 0:player1_x =1300
    elif player1_y >=700:player1_y = 0
    elif player1_y <=0:player1_y = 700
    
    
    if player2_x >= 1300:player2_x =0
    elif player2_x <= 0:player2_x =1300
    elif player2_y >=700:player2_y = 0
    elif player2_y <=0:player2_y = 700

    collision = isCollision(player2_x ,player2_y,bull2_x ,player1_y )
    if collision:
        health1-=4

    collision = isCollision(player1_x ,player1_y,bull_x ,player2_y )
    if collision:
        health2 -=4

    if health1 <=0:
        print("player 1")
        break
    elif health2 <=0:
        print("player 2")
        break

    clock = pp.time.Clock() 

    healthPla1 = over_font.render(str(health2), True, (255, 255, 255))
    screen.blit(healthPla1, (10, 10))

    healthPla2 = over_font.render(str(health1), True, (255, 255, 255))
    screen.blit(healthPla2, (1190, 10))

    pp.display.update()
    clock.tick(60)