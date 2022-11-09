import pygame 
import winsound
# -- Global Constants 
ball_width = 20
x_val = 150
y_val = 200
x_direction = 1
y_direction = 1
x_edge = False
y_edge = False
padd_length = 15
padd_width = 60
x_padd = 0
y_padd = 20
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
pygame.display.set_caption("My Window") 
# -- Exit game flag set to false 
done = False
# -- Manages how fast screen refreshes 
clock = pygame.time.Clock() 

### -- Game Loop 
while not done: 
 # -- User input and controls
 for event in pygame.event.get(): 
    if event.type == pygame.QUIT: 
       done = True 
#End If
 #Next event
 # -- Game logic goes after this comment
 #This is the part of the code which makes the ball bounce
 if y_val == 460 :
    y_edge = True 
    winsound.Beep(800,20)
 elif y_val == 0 :
    y_edge = False
    winsound.Beep(800,20)

 if x_val == 620 :
    x_edge = True 
    winsound.Beep(800,20)
 elif x_val == 0 :
    x_edge = False
    winsound.Beep(800,20)

 if x_edge == False :
    x_val = x_val + x_direction
 else :
    x_val = x_val - x_direction

 if y_edge == False :
    y_val = y_val + y_direction
 else :
    y_val = y_val - y_direction
#---------------------------------------------------
 # -- Screen background is BLACK 
 screen.fill (BLACK) 
 # -- Draw here 
 pygame.draw.rect(screen, BLUE, (x_val, y_val, 20, ball_width)) 
 pygame.draw.rect(screen, WHITE, (x_padd, y_padd, padd_length, padd_width))
 # -- flip display to reveal new position of objects 
 pygame.display.flip()
 # - The clock ticks over 
 clock.tick(60) 
#End While - End of game loop 
pygame.quit()
