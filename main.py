import pygame as pp

#initialising pygame module
pp.init()

#defining window and its properties
screen = pp.display.set_mode((1300,750))
pp.display.set_caption("GDOOM")

player1 = pp.image.load('Player1.png')
player1_x = 400
player1_y = 300
player1_xc = 0
player1_yc = 0

player2 = pp.image.load('Player2.png')
player2_x = 800
player2_y = 300
player2_xc = 0
player2_yc = 0


running = True

while running:
    screen.fill((0, 0, 0,0))
    screen.blit(player1,(player1_x,player1_y))
    screen.blit(player2,(player2_x,player2_y))
    for event in pp.event.get():
        if event.type == pp.QUIT:
            running = False
        if event.type == pp.KEYDOWN:
            if event.key == pp.K_RIGHT:
                player2_xc += 2
            if event.key == pp.K_LEFT:
                player2_xc -= 2
            if event.key == pp.K_d:
                player1_xc += 2
            if event.key == pp.K_a:
                player1_xc -= 2
            if event.key == pp.K_w:
                player1_yc -= 2
            if event.key == pp.K_s:
                player1_yc += 2
            if event.key == pp.K_UP:
                player2_yc -= 2
            if event.key == pp.K_DOWN:
                player2_yc +=2

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
    player1_x+=player1_xc
    player2_x+=player2_xc
    player1_y+=player1_yc
    player2_y+=player2_yc

    if player1_x >= 1300:player1_x =0
    elif player1_x <= 0:player1_x =1300
    elif player1_y >=700:player1_y = 0
    elif player1_y <=0:player1_y = 700
    
    
    if player2_x >= 1300:player2_x =0
    elif player2_x <= 0:player2_x =1300
    elif player2_y >=700:player2_y = 0
    elif player2_y <=0:player2_y = 700

    pp.display.update()