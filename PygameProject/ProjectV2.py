#-------All imports here --------
import pygame 
import random 
import math 
import sys
from pygame.locals import *
#Initialise PyGame
pygame.init() 
# -------- Global Constants ---------
x = 0 
y = 0 
loop = 0
points = 0
platforms = []
rand = 0
# -- Colours 
BLACK = (0,0,0) 
WHITE = (255,255,255) 
BLUE = (50,50,255) 
YELLOW = (255,255,0) 
# --------- Making the screen with images defined --------
size = (640,480) 
screen = pygame.display.set_mode(size) 
#Title of new window/screen 
dt = pygame.display.set_caption("Jump-Jump-Mania") 
#Exit game flag set to false 
done = False
# Create a list of the platforms
Platform_group = pygame.sprite.Group() 
# Create a list of all sprites 
all_sprites_group = pygame.sprite.Group()  
#create a background
bg = pygame.image.load("BG2.png")
# -- Manages how fast screen refreshes 
clock = pygame.time.Clock()
points_inc = pygame.USEREVENT+1
pygame.time.set_timer(points_inc, 1000)
font = pygame.font.Font(None, 26)
#cadd variable incase of collision with lava 
collision_tolerance = 10
#add platform spawn time 
spawnTime = 1000
#make the lava and spawn island
lava = Rect(-275, 450, 800, 50)
lavaTexture = pygame.image.load("LVT.jpg")
island = Rect(400, 350, 100, 100)
overlay = pygame.image.load("Platform.png")
#----------------------------------------------------


## -- Define the class snow which is a sprite 
class Platform(pygame.sprite.Sprite): 
 # Define the constructor for snow 
 def __init__(self): 
 # Call the sprite constructor 
   super().__init__() 
 # Create a sprite and fill it with colour 
   self.image =  pygame.image.load('Platform.png').convert_alpha()
    # Set the position of the sprite 
   self.rect = self.image.get_rect() 
   self.rect.x = random.randint(0, 480 - self.rect.width)
   self.rect.y = 0

def add_platform():
    rand = random.randint(1, 3)
    while rand != 0:
        platform = Platform()
        platforms.append(platform)
        rand -= 1
    #endwhile
   
#-------------------------------------------------------------------------

class Player(pygame.sprite.Sprite): 
 # Define the constructor for snow 
    def __init__(self, color, width, height, speed): 
    # Call the sprite constructor 
        super().__init__()

        # Create a sprite and fill it with colour 
        self.image = pygame.Surface([width,height]) 
        self.image.fill(color) 
        
        # Set the position of the sprite 
        self.rect = self.image.get_rect() 
        self.rect.x = 450
        self.rect.y =  340
        
        self.vel_x = 0
        self.vel_y = 10

        self.lives = 3
        self.score = 0

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
        if self.vel_y == -1:
           self.rect.y -= self.vel_y
        # end if
        msg = "Lives: " + str(self.lives)
        self.font1 = pygame.font.SysFont('freesanbold.ttf', 24)
        self.text1 = self.font1.render(msg , True, WHITE)
        self.textRect1 = self.text1.get_rect()

        score = "Score: " + str(self.score)
        self.font2 = pygame.font.SysFont('freesanbold.ttf', 24)
        self.text2 = self.font2.render(score , True, WHITE)
        self.textRect2 = self.text2.get_rect()

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
 
#Next x


#create the player 
player = Player(YELLOW, 10, 10,1)
all_sprites_group.add (player)

#make sure the platforms will fall in increments 
fall_plat = pygame.time.get_ticks() + 5000

while not done: 
 # -- User input and controls

 for event in pygame.event.get():
    if event.type == pygame.QUIT:
        done = True
    
    if event.type == points_inc:
        points += 1

    time_now = pygame.time.get_ticks()

    if time_now >= fall_plat:
       add_platform()
       fall_plat= time_now + 5000
    
    for platform in platforms:
       platform.rect.y += 5
       if platform.rect.y > 640:
          platforms.remove(platform)

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT:
            player.vel_x = -3
        
        elif event.key == pygame.K_LEFT:
            player.vel_x = 3
        
        elif event.key == pygame.K_SPACE:
            player.vel_y = 10
            player.is_jump = True


    if event.type == pygame.KEYUP:
        if event.key == pygame.K_RIGHT:
            player.vel_x = 0
        if event.key == pygame.K_LEFT:
            player.vel_x = 0

 hit = pygame.sprite.spritecollide(player, Platform_group, False) 
 if player.is_jump and player.m == -1 and hit:
    player.vel_y = -1
    player.is_jump = False 

 for platform in platforms:
    screen.blit(overlay, platform.rect)
 pygame.display.flip()

 if player.rect.colliderect(lava):
    pygame.time.set_timer(points_inc, 0)
    if player.lives > 0:
        player.lives -= player.lives


 text = font.render(f'Score: {points}', True, (255, 255, 255))
    
    

#End If
 screen.blit(bg,(0,0))
 screen.blit(text, (0, 15))
 #Next event

 # -- Game logic goes after this comment
 all_sprites_group.update()
  
    
    
    

 #draw the lava and island 
 pygame.draw.rect(screen, (247, 104, 6), lava)
 screen.blit(lavaTexture, (-275, 450))
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