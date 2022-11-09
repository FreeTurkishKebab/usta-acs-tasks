import pygame 
import math
pygame.init()
# -- Global Constants 
x = 0 
y = 0 
# -- Colours 
BLACK = (0,0,0) 
WHITE = (255,255,255) 
BLUE = (50,50,255) 
YELLOW = (255,255,0) 
# -- Initialise PyGame
pygame.init() 
# -- Blank Screen
size = (640,480) 
screen = pygame.display.set_mode(size) 
# -- Title of new window/screen 
dt = pygame.display.set_caption("House") 
# -- Exit game flag set to false 
done = False
sun_x = 40
sun_y = 100
# -- Manages how fast screen refreshes 
clock = pygame.time.Clock()

while not done: 
 # -- User input and controls
 for event in pygame.event.get(): 
   if event.type == pygame.QUIT: 
     done = True 
#End If
 #Next event
 # -- Game logic goes after this comment


 if sun_x >= 640 :
    sun_x = 0
 if sun_y >= 480 :
    sun_y = 0
 # -- Screen background is BLACK 
 screen.fill (BLACK) 
 # -- Draw here 
 pygame.draw.rect(screen, BLUE, (220,165,200,150))
 pygame.draw.circle(screen, YELLOW, ((sun_x), (sun_y)), 40, 0)
 angle = 20
 angle = 0.0174532925 * angle
 sun_x = (sun_x * math.cos(angle)) + (sun_y * math.sin(angle))
 sun_y = (sun_x * math.sin(angle)) - (sun_y * math.cos(angle))
 # -- flip display to reveal new position of objects 
 pygame.display.flip()
 # - The clock ticks over 
 clock.tick(60) 
#End While - End of game loop 
pygame.quit()