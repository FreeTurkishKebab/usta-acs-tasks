import pygame 
import random 
import math 
import sys
from pygame.locals import *
# -- Global Constants 
x = 0 
y = 0 
loop = 0
is_jump = False

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
dt = pygame.display.set_caption("Space") 
# -- Exit game flag set to false 
done = False
# Create a list of the snow blocks 
Platform_group = pygame.sprite.Group() 
# Create a list of all sprites 
all_sprites_group = pygame.sprite.Group()  
#create a background
bg = pygame.image.load("BG2.png")
# -- Manages how fast screen refreshes 
clock = pygame.time.Clock()
#cadd variable incase of collision with lava 
collision_tolerance = 10
#add platform spawn time 
spawnTime = 1000
#make the lava and spawn island
lava = Rect(-300, 460, 1000, 20)
lavaTexture = pygame.image.load("LVT.jpg")
island = Rect(400, 350, 100, 100)
#make a variable for current state of jump 


## -- Define the class snow which is a sprite 
class Platform(pygame.sprite.Sprite): 
 # Define the constructor for snow 
 def __init__(self, color, width, height,speed): 
 # Call the sprite constructor 
   super().__init__() 
 # Create a sprite and fill it with colour 
   self.image = pygame.image.load('Platform.png').convert_alpha()
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
 # Define the constructor for snow 
    def __init__(self, color, width, height, player): 
    # Call the sprite constructor 
        super().__init__()

        # Create a sprite and fill it with colour 
        self.image = pygame.Surface([width,height]) 
        self.image.fill(color) 
        
        # Set the position of the sprite 
        self.rect = self.image.get_rect() 
        self.rect.x = 300 
        self.rect.y =  size[0] - height
        self.vel_x = 0
        self.vel_y = 10

        self.lives = 1

        self.m = 1 

        self.is_jump = False       

    def update(self):
        if self.rect.y >= size[1]:
            self.rect.y = 470

            # making isjump equal to false 
            self.is_jump = False

            # setting original values to v and m
            self.vel_y = 10
            self.m = 1
        
        self.rect.x -= self.vel_x
        # end if
        msg = "Lives: " + str(self.lives)
        self.font1 = pygame.font.SysFont('freesanbold.ttf', 24)
        self.text1 = self.font1.render(msg , True, WHITE)
        self.textRect1 = self.text1.get_rect()

        if self.is_jump:
            self.jump()

    def jump(self):

        # calculate force (F). F = 1 / 2 * mass * velocity ^ 2.
        F = 0.5 * self.m * self.vel_y ** 2

        # change in the y co-ordinate
        player.rect.y -= F
          
        # decreasing velocity while going up and become negative while coming down
        self.vel_y -= 1
        # object reached its maximum height
        if self.vel_y < 0:
            # negative sign is added to counter negative velocity
            self.m = -1
        else:
           self.m = 1

        

        

class bullet(pygame.sprite.Sprite):
    def __init__(self, color, height, width):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        # Set the position of the sprite
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x
        self.rect.y = 480 - 20

    def update(self):
        # Move bullet up 
        self.rect.y = self.rect.y - 5
        # -- bullet hitting the platform
        pygame.sprite.groupcollide(bulletlist, Platform_group, True, True)
    

bulletlist = pygame.sprite.Group()

          
   # -- User inputs here 
 #End Procedure
#End Class

# Create the platforms
number_of_Platforms = 10 # we are creating 10 Platforms
for x in range (number_of_Platforms): 
  Platforms = Platform(BLUE, 10, 10,1) # Platforms are blue with size 10 by 10 px
  Platform_group.add (Platforms) # adds the new Platform to the group of Platforms
  all_sprites_group.add (Platforms) # adds it to the group of all Sprites
 
#Next x


#create the player 
player = Player(YELLOW, 10, 10,1)
all_sprites_group.add (player)

#make a hit 
hit = pygame.sprite.spritecollide(player, Platform_group, True)

while not done: 
 # -- User input and controls

 for event in pygame.event.get():
    if event.type == pygame.QUIT:
        done = True

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT:
            player.vel_x = -3
        
        elif event.key == pygame.K_LEFT:
            player.vel_x = 3
        
        elif event.key == pygame.K_SPACE:
            player.is_jump = True
            

    if event.type == pygame.KEYUP:
        if event.key == pygame.K_RIGHT:
            player.vel_x = 0
        if event.key == pygame.K_LEFT:
            player.vel_x = 0

    if hit and is_jump:
       player.vel_y = 1
       player.bottom = Platforms.top
       

#End If
 screen.blit(bg,(0,0))
 #Next event

 # -- Game logic goes after this comment
 all_sprites_group.update()
  
    
    
    

 #draw the lava and island 
 screen.blit(lavaTexture, (lava))
 pygame.draw.rect(screen, (17, 144, 163), island)

 #game over means touching lava 
 


  
 all_sprites_group.draw (screen) 

       
    
 
 screen.blit(player.text1, player.textRect1)
 # -- flip display to reveal new position of objects 
 pygame.display.flip()
 # - The clock ticks over 
 clock.tick(60) 
#End While - End of game loop 
pygame.quit()