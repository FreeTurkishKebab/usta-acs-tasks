import pygame 

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
size = (400,600) 
screen = pygame.display.set_mode(size) 

# -- Title of new window/screen 
dt = pygame.display.set_caption("The game") 
# -- Exit game flag set to false 
done = False 

#creating the main character 
class player(pygame.sprite.Sprite): 
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
    
    def MoveChar(self, mousePosition):
        self.rect.x = mousePosition[0]
        self.rect.y = mousePosition[1]


pygame.init()
pygame.mixer.init() 

#creating the background 
pygame.display.set_caption("Jump-Jump Mania")
background_image=pygame.image.load("Background.png").convert()
pygame.mouse.set_visible(False)        

# -- Manages how fast screen refreshes 
clock = pygame.time.Clock()

#setting the background loop
while done == False:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done = True 

        elif event.type == pygame.KEYDOWN: # - a key is down 
           if event.key == pygame.K_LEFT: # - if the left key pressed
               player.speed = 3 # speed set to -3
           elif event.key == pygame.K_RIGHT: # - if the right key pressed
               player.speed = -3 # speed set to -3

        elif event.type == pygame.KEYUP: # - a key released 
           if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT: 
               player.speed = 0 # speed set to 0

    screen.blit(background_image, [0,0])
    pygame.display.flip()
    clock.tick()
pygame.quit()
