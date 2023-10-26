import pygame 
import sys
from pygame.locals import *
pygame.init()
width = 500
height = 500
vel = 10
x_plat = 100
y_plat = 400
platform_vel = 5
clock = pygame.time.Clock()
isjump = False
jumpcount = 7.5
ColTol= 10
gravity = 1
player_vy = 0 #player vertical velocity

surface = pygame.display.set_mode((width, height))
rect = Rect(x_plat, y_plat, 150, 20)
player = Rect(250, 475, 25, 25)

run = True 
while run: 

    clock.tick(60)

    if rect.left >= 355 or rect.left < 1:
        platform_vel *= -1

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.x > 0:
        player.x -= vel
    if keys[pygame.K_RIGHT] and player.x < (500 - 25):
        player.x += vel
    if not(isjump):
        if keys[pygame.K_SPACE]:
            isjump = True
            player_vy = -16
    player_vy += gravity 
    player.y += player_vy

    collide = pygame.Rect.colliderect(rect, player)
    if collide and player_vy >= 0:
        player.bottom = rect.top
        player_vy = 0
        player.left += platform_vel
        isjump = False
    
    if player.y> 475: #don't fall off the bottom of the screen
        player.y = 475
        player_vy = 0
        isjump = False
    
    rect.left += platform_vel #move platform

    pygame.draw.rect(surface, (0,0,0), rect)
    pygame.draw.rect(surface, (255,255,255), player)
    pygame.display.update()
    surface.fill((255,222,173))

    for event in pygame.event.get():
        if event.type == QUIT:
            run = False
        
        



