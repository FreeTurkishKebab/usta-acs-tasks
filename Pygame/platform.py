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
size = (600,400) 
screen = pygame.display.set_mode(size) 
# -- Title of new window/screen 
dt = pygame.display.set_caption("Fun") 
# -- Exit game flag set to false 
done = False
# Create a list of all sprites 
all_sprites_group = pygame.sprite.Group()  
# -- Manages how fast screen refreshes 
clock = pygame.time.Clock()
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
        self.speed = 0
        self.lives = 3
        

    def update(self):
        if self.rect.y >= 400:
            self.rect.x = 0
            self.rect.x = random.randrange(0, 600)
            self.rect.x = 320
            self.rect.y = 390
        self.rect.x = self.rect.x - self.speed
        if y < 400:
            y = y + 1
        # end if

def jump():
    Player.rect.y = Player.rect.y - 3

#create the player 
player = Player(YELLOW, 10, 10, 1)
all_sprites_group.add (player)

while not done: 
 # -- User input and controls
 for event in pygame.event.get(): 
    if event.type == pygame.QUIT:
     done = True 
    elif event.type == pygame.KEYDOWN: # - a key is down 
        if event.key == pygame.K_LEFT: # - if the left key pressed
            player.speed = 3 # speed set to -3
        elif event.key == pygame.K_RIGHT: # - if the right key pressed
            player.speed = -3 # speed set to -3
        elif event.key == pygame.K_UP:
            jump()

    elif event.type == pygame.KEYUP: # - a key released 
        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT: 
            player.speed = 0 # speed set to 0
    


#End If
 #Next event

 # -- Game logic goes after this comment

  # -- Draw here 
 screen.fill (BLACK)
 all_sprites_group.draw (screen)  
 # -- flip display to reveal new position of objects 
 pygame.display.flip()
 # - The clock ticks over 
 clock.tick(60) 
#End While - End of game loop
pygame.quit()