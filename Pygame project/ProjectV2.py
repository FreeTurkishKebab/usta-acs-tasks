import pygame 
import random 
import math 
# -- Global Constants 
x = 0 
y = 0 
loop = 0

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
invader_group = pygame.sprite.Group() 
# Create a list of all sprites 
all_sprites_group = pygame.sprite.Group()  
#create a background
bg = pygame.image.load("BG2.png")
# -- Manages how fast screen refreshes 
clock = pygame.time.Clock()



## -- Define the class snow which is a sprite 
class Invader(pygame.sprite.Sprite): 
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
 # Define the constructor for snow 
    def __init__(self, color, width, height, speed): 
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
        # -- bullet hitting the invader
        pygame.sprite.groupcollide(bulletlist, invader_group, True, True)
    

bulletlist = pygame.sprite.Group()

          
   # -- User inputs here 
 #End Procedure
#End Class

# Create the enemies
number_of_enemies = 10 # we are creating 10 invaders
for x in range (number_of_enemies): 
  enemies = Invader(BLUE, 10, 10,1) # invaders are blue with size 10 by 10 px
  invader_group.add (enemies) # adds the new invader to the group of invaders
  all_sprites_group.add (enemies) # adds it to the group of all Sprites
  # - Screen background is BLACK 
#Next x


#create the player 
player = Player(YELLOW, 10, 10,1)
all_sprites_group.add (player)

 

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

#End If
 screen.blit(bg,(0,0))
 #Next event

 # -- Game logic goes after this comment
 all_sprites_group.update()
 # -- when invader hits the player add 5 to score. 
 player_hit_group = pygame.sprite.spritecollide(player, invader_group, True)
 for foo in player_hit_group: 
    player.lives = player.lives - 1
    print (player.lives)

  
 all_sprites_group.draw (screen) 
 screen.blit(player.text1, player.textRect1)
 # -- flip display to reveal new position of objects 
 pygame.display.flip()
 # - The clock ticks over 
 clock.tick(60) 
#End While - End of game loop 
pygame.quit()