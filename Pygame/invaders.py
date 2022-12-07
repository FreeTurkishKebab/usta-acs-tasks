import pygame 
import random 
import math 
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
dt = pygame.display.set_caption("Snow") 
# -- Exit game flag set to false 
done = False
# Create a list of the snow blocks 
invader_group = pygame.sprite.Group() 
# Create a list of all sprites 
all_sprites_group = pygame.sprite.Group()  
# -- Manages how fast screen refreshes 
clock = pygame.time.Clock()

## -- Define the class snow which is a sprite 
class Snow(pygame.sprite.Sprite): 
 # Define the constructor for snow 
 def __init__(self, color, width, height,speed): 
 # Call the sprite constructor 
   super().__init__() 
 # Create a sprite and fill it with colour 
   self.image = pygame.Surface([width,height]) 
   self.image.fill(color) 
    # Set the position of the sprite 
   self.rect = self.image.get_rect() 
   self.rect.x = random.randrange(0, 600) 
   self.rect.y = random.randrange(-50, 0)
   self.speed = 1
 def update(self):
   if self.rect.y >= 480:
    self.rect.y = 0
    self.rect.x = random.randrange(0, 600)
   self.rect.x = random.randrange(-1,2) + self.rect.x
   self.rect.y = self.rect.y + self.speed
#-------------------------------------------------------------------------
class Player(pygame.sprite.Sprite):
    def __init__(self, speed, size, height):
       self.speed = 0
       self.posx = 300
       self.posy = (size[0] - self.height)
 #End Procedure
#End Class

# Create the enemies
number_of_enemies = 10 # we are creating 10 invaders
for x in range (number_of_enemies): 
  enemies = Snow(BLUE, 10, 10,1) # invaders are blue with size 10 by 10 px
  invader_group.add (enemies) # adds the new invader to the group of invaders
  all_sprites_group.add (enemies) # adds it to the group of all Sprites
  # - Screen background is BLACK 
  
#create the player 
z = 0
for z in range(0,0):
    pygame.draw.rect(YELLOW, 10, 10,1)





#Next x

# -- Game logic goes after this comment
while not done: 
 # -- User input and controls
 for event in pygame.event.get(): 
   if event.type == pygame.QUIT: 
     done = True 
#End If
 #Next event
 all_sprites_group.update()
 screen.fill (BLACK) 
  # -- Draw here 
 all_sprites_group.draw (screen) 
 # -- Draw here 
 # -- flip display to reveal new position of objects 
 pygame.display.flip()
 # - The clock ticks over 
 clock.tick(60) 
#End While - End of game loop 
pygame.quit()