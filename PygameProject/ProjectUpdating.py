#-------All imports here --------
import pygame 
import random 
import math 
import sys
from pygame.locals import *
#Initialise PyGame
pygame.init() 

#----Constant Areas----------
#screen Size 
WIDTH = 640
HEIGHT = 480

#Platforms 
platforms = []

#Colours 
BLACK = (0,0,0) 
WHITE = (255,255,255) 
BLUE = (50,50,255) 
YELLOW = (255,255,0)

#Times
START_TIME = pygame.time.get_ticks()
DURATION = 10000

#points and lives
points_inc= pygame.USEREVENT+1
pygame.time.set_timer(points_inc, 1000)
font= pygame.font.Font(None, 26)

#---------Make the player---------
PLAYER_WIDTH = 25
PLAYER_HEIGHT = 25
PLAYER_SIZE = 25
PLAYER_SPEED = 5
PLAYER_HEIGHT = 15
IS_JUMPING = False
JUMP_HEIGHT = 15
JUMP_COUNT = 10
direction = 1
GRAVITY = 9
points = 0
collisionI = False
wait = False
onIsland = False
OnPlat = False
Time = 1500
#----------Making the screen with other aspects------------
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jump Jump Mania")
BGIMAGE= pygame.image.load("BG2.png")
PLAYER_IMAGE = pygame.Surface((PLAYER_WIDTH, PLAYER_HEIGHT))
PLAYER_IMAGE.fill(YELLOW)

ISLAND_WIDTH = 100
ISLAND_HEIGHT = 30
ISLAND_X = 260
ISLAND_Y = 420
island = Rect(ISLAND_X, ISLAND_Y, ISLAND_WIDTH, ISLAND_HEIGHT)

#add on to player location
PLAYER_X = ISLAND_X 
PLAYER_Y = ISLAND_Y - 25

#add on to platforms 
overlayPlatform = pygame.image.load("Platform.png")

#add on the lava 
lavaTexture = pygame.image.load("LVT.jpg")
lava = Rect(-20, 460 , 800, 20)
#-----------Platform classes and falling---------------
class Platform(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.Surface((100,10))
        self.image.fill((0,255,0))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(100, 640 - self.rect.width)
        self.rect.y = 0
    
def add_platform():
    rand = random.randint(1, 3)
    while rand != 0:
        platform = Platform()
        platforms.append(platform)
        rand -= 1
    #endwhile
    
fall_plat = pygame.time.get_ticks() + Time 
SpeedV = pygame.time.get_ticks() + 3000
FallSpeed = 1
jump_delay = pygame.time.get_ticks() + 500
delay = False
#------------------Points and lives function-------------------
def update(self):
    #Lives
    msg = "Lives: " + str(self.lives)
    self.font1 = pygame.font.SysFont('freesanbold.ttf', 24)
    self.text1 = self.font1.render(msg , True, WHITE)
    self.textRect1 = self.text1.get_rect()

    #Score
    score = "Score: " + str(self.score)
    self.font2 = pygame.font.SysFont('freesanbold.ttf', 24)
    self.text2 = self.font2.render(score , True, WHITE)
    self.textRect2 = self.text2.get_rect()

#-------------------Bullet class------------------
class Bullet(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.Surface((10,15))
        self.image.fill((0,255,0))
        self.rect = self.image.get_rect()
        self.rand = random.randint(0, 1)
        self.rect.x = self.rand * WIDTH
        self.rect.y = random.randint(0, HEIGHT)

#--------maingame loop redifined here-----

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == points_inc:
            points += 1
    #---------falling platforms------
    CURRENT_TIME = pygame.time.get_ticks()
    
    #The time which each 1-3 platform is put onto the screen
    if CURRENT_TIME >= fall_plat:
        add_platform()
        fall_plat = CURRENT_TIME + Time
    
    #Platform speed up over time 
    if CURRENT_TIME >= SpeedV:
        FallSpeed += 0.05
        SpeedV = CURRENT_TIME + 3000   

    #set gravity to platform fall speed 
    if FallSpeed >= GRAVITY:  
        GRAVITY = FallSpeed + 3
        if Time >= 500:
            Time = Time - 300
    #endif 


    #speed of platform being set
    for platform in platforms:
        platform.rect.y += FallSpeed
        #remove platform once it reaches the end 
        if platform.rect.y > 480:
            platforms.remove(platform)

    #-------variables to be updated--------



    #----- kEYBOARD CONTROLS --------
    KEYS = pygame.key.get_pressed()

    #ARROWS 
    if KEYS[pygame.K_LEFT] and PLAYER_X > 0:
        PLAYER_X -= PLAYER_SPEED

    if KEYS[pygame.K_RIGHT] and PLAYER_X < WIDTH - PLAYER_WIDTH:
        PLAYER_X += PLAYER_SPEED

    if KEYS[pygame.K_SPACE]:
        IS_JUMPING = True

    if IS_JUMPING:
        if JUMP_COUNT >= 0:
            FALLING = False
            direction = -1


            PLAYER_Y -= (JUMP_COUNT ** 2) * 0.5 * -(direction)
            JUMP_COUNT -= 1

            if PLAYER_Y == 0:
                JUMP_COUNT = 0
        
        else:
            IS_JUMPING = False
            direction = 1

        
    #---------Gravity function--------
    if not OnPlat:
        if PLAYER_Y < HEIGHT - PLAYER_SIZE:
            PLAYER_Y += GRAVITY * direction

        else:
            PLAYER_Y = HEIGHT - PLAYER_SIZE 

    if OnPlat:
        if PLAYER_Y < HEIGHT - PLAYER_SIZE:
            PLAYER_Y += FallSpeed
    
    #Player position and lava collision 
    PLAYER_RECT = pygame.Rect(PLAYER_X, PLAYER_Y, PLAYER_WIDTH, PLAYER_HEIGHT)

    if PLAYER_RECT.colliderect(lava):
        pygame.time.set_timer(points_inc, 0)
        # GAME OVER

    #landing on platforms
    for platform in platforms:
        if PLAYER_RECT.colliderect(platform.rect) and (direction == 1):
            OnPlat = True

        else:
            OnPlat = False


        if OnPlat:
            PLAYER_Y = platform.rect.top
            IS_JUMPING = False
            JUMP_COUNT = 10

    
    
    
    # -----------Sprites appearing on screen-------
    SCREEN.fill(BLACK)
    SCREEN.blit(BGIMAGE, (0,0))
    SCREEN.blit(PLAYER_IMAGE, (PLAYER_X, PLAYER_Y))
    pygame.draw.rect(SCREEN, (247, 104, 6), lava)
    SCREEN.blit(lavaTexture, (-20, 460))

    #-------Make and island and make it dissapear after some time----------
    if CURRENT_TIME - START_TIME < DURATION:
        pygame.draw.rect(SCREEN, (17,144,163), island)
        if PLAYER_RECT.bottom >= (island.top -3) and PLAYER_RECT.colliderect(island) and (direction == 1):
            collisionI = True
        else:
            collisionI = False
    
        if collisionI ==True:
            IS_JUMPING = False
            JUMP_COUNT = 10
            PLAYER_Y = 405
            onIsland = True
            FALLING = True 
            
    if collisionI == True:
        FALLING = True
        onIsland = False  
        collisionI == False     
        
        

    
    #----------Display points and lives-----------
    text = font.render(f'Points: {points}', True, (255, 255, 255))
    SCREEN.blit(text, (0,15))

    #----make the platforms on the screen
    for platform in platforms:
        SCREEN.blit(overlayPlatform, platform.rect)
    


    pygame.display.flip()

    pygame.time.Clock().tick(120)