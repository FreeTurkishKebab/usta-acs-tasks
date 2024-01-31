#-------All imports here --------
import pygame 
import random 
import math 
import sys
from pygame.locals import *
import pygame.freetype

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
RED = (255,0,0)

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
lives = 3
collisionI = False
onIsland = False
OnPlat = False
Time = 1500
over = False
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
overlayBulletR = pygame.image.load("BulletRight.png")
overlayBulletL = pygame.image.load("BulletLeft.png")
overlayCoin = pygame.image.load("GCoin.png")
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
bullets = []
class MakeBullet(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((15,10))
        self.image.fill((34,134,234)) 
        self.rand = random.randint(0,1)
        self.rect = self.image.get_rect()
        self.rect.x = self.rand * WIDTH
        self.rect.y = random.randint(0, HEIGHT)

def add_bullet():
    bullet = MakeBullet()
    bullets.append(bullet)
bulletappear = pygame.time.get_ticks() + 3000


#----------------Gold coin class-----------------
coins = []
class GoldCoin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((12,12))
        self.image.fill((255,215,0)) 
        self.rand = random.randint(0,1)
        self.rect = self.image.get_rect()
        self.rect.x = self.rand * WIDTH
        self.rect.y = random.randint(0, HEIGHT)

def add_coin():
    coin = GoldCoin()
    coins.append(coin)
coinappear = pygame.time.get_ticks() + 5000

#--------maingame loop redifined here-----

while True and not over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == points_inc:
            points += 1

    #---------Making the game over screen---------
    if lives <= 0:
        over = True
        
    #---------falling platforms------
    CURRENT_TIME = pygame.time.get_ticks()
    
    #The time which each 1-3 platform is put onto the screen
    if CURRENT_TIME >= fall_plat:
        add_platform()
        fall_plat = CURRENT_TIME + Time
    
    #Gold coins come out of the wall every 5 seconds 
    if CURRENT_TIME >= coinappear:
        add_coin()
        coinappear = CURRENT_TIME + 5000
    
    #Bullets come out of the walls every 3 seconds
    if CURRENT_TIME >= bulletappear:
        add_bullet()
        bulletappear = CURRENT_TIME + 3000
        
    
    #Platform speed up over time 
    if CURRENT_TIME >= SpeedV:
        FallSpeed += 0.05
        SpeedV = CURRENT_TIME + 3000   

    #set gravity to platform fall speed 
    if FallSpeed >= GRAVITY:  
        GRAVITY = FallSpeed + 3
        if Time >= 500:
            Time = Time - 500
    #endif 


    #speed of platform being set
    for platform in platforms:
        platform.rect.y += FallSpeed
        #remove platform once it reaches the end 
        if platform.rect.y > 480:
            platforms.remove(platform)
    
    #speed of the gold coins being set 
    for coin in coins:
        if coin.rand == 0:
            coin.rect.x += 3
            if coin.rect.x > WIDTH:
                coins.remove(coin)
        
        elif coin.rand == 1:
            coin.rect.x -= 3
            if coin.rect.y < 0:
                 coins.remove(coin)

    #speed of the bullets being set
    for bullet in bullets:
        if bullet.rand == 0:
            bullet.rect.x += 3
            if bullet.rect.x > WIDTH:
                bullets.remove(bullet)
        
        elif bullet.rand == 1:
            bullet.rect.x -= 3
            if bullet.rect.y < 0:
                bullets.remove(bullet)


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
        lives -= lives
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

    #------Make the player collide with the gold coins 
    for coin in coins:
        if PLAYER_RECT.colliderect(coin.rect):
            points += 10
            coins.remove(coin)
    
    #------Make the player collide with the bullets 
    for bullet in bullets:
        if PLAYER_RECT.colliderect(bullet.rect):
            lives -= 1
            bullets.remove(bullet)


    
    
    
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
    SCREEN.blit(text, (0,4))

    text2 = font.render(f'Lives: {lives}', True, (255,255,255))
    SCREEN.blit(text2, (0,24))

    #----make the platforms on the screen
    for platform in platforms:
        SCREEN.blit(overlayPlatform, platform.rect)
    
    #-----Make the gold coins appear on the screen
    for coin in coins:
        SCREEN.blit(overlayCoin, coin.rect)
    
    #-----Make the bullets appear on the screen
    for bullet in bullets:
        if bullet.rand == 1:
            SCREEN.blit(overlayBulletL, bullet.rect)
        elif bullet.rand == 0:
            SCREEN.blit(overlayBulletR, bullet.rect)

    


    pygame.display.flip()

    pygame.time.Clock().tick(120)

#-------------------------Text file is created---------------------

current_score = points 
high_score = 0 

if current_score > high_score:  #set the values for the new bigh score 
    high_score = current_score

with open("high_score.txt", "a") as file:
    file.write(str(high_score))
#-------------Game over screen is drawn---------------------------------------------------------------

#-----------------Create the dimensions for the buttons---------------

BUTTON_WIDTH = 200
BUTTON_HEIGHT = 50
BUTTON_TEXT_COLOR = (0, 0, 0)
BFONT = pygame.font.Font('freesansbold.ttf', 36)
#--------------Add the variables for the textures in the game over screen-------

#save an image to add to the buttons  and background
wood_texture = pygame.image.load("wood_texture.png")
background_image = pygame.image.load("GameOver.png")

#--------------Create a class for the buttons--------------

class Button:
    #This is the initial definition of the button
    def __init__(self, x, y, width, height, text, action):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text 
        self.action = action 
    
    #This is where the dimensions and texture of the buttons are declared 
    def draw(self, SCREEN):
        SCREEN.blit(wood_texture, self.rect)
        pygame.draw.rect(SCREEN, (0, 0, 0), self.rect, 2) #wooden border 
        text_surface = BFONT.render(self.text, True, BUTTON_TEXT_COLOR)
        text_rect = text_surface.get_rect(center = self.rect.center)
        SCREEN.blit(text_surface, text_rect)

    #This checks whether the mouse is clicking on the button or not
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                self.action()

#Define the different texts  
              
def text_to_screen(SCREEN, text, x, y): 
    text = str(text)
    Tfont = pygame.font.Font(None, 100)
    text = Tfont.render(text, True, RED)
    SCREEN.blit(text, (x, y))

#Score
FinalScore = "Score: " + str(points)

def display_score(SCREEN, x, y): 
    text2 = FinalScore
    Tfont = pygame.font.Font(None, 70)
    text2 = Tfont.render(text2, True, RED)
    SCREEN.blit(text2, (x, y))
    
def display_inpMessage(SCREEN, x, y): 
    text3 = "Please input a name: "
    Tfont = pygame.font.Font(None, 40)
    text3 = Tfont.render(text3, True, RED)
    SCREEN.blit(text3, (x, y))

User = ""   
#---------------Define the different button types-----------------------

def Menu():
    import Menu
    open(file="Menu")

#--------------Draw the buttons------------------

Menu_Button = Button(
    WIDTH // 2 - BUTTON_WIDTH // 2, 
    HEIGHT // 2 - BUTTON_HEIGHT // 2 + 150, 
    BUTTON_WIDTH,
    BUTTON_HEIGHT, 
    "Quit" ,
    Menu
)

buttons = [Menu_Button]
#-------------Main loop for the game over screen----------
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        for button in buttons:
            button.handle_event(event)

    SCREEN.blit(background_image, (0, 0)) #draw the background image

    #-----------------draw the different texts on screen-----------------

    text_to_screen(SCREEN, 'GAME OVER', WIDTH // 2 - 200, HEIGHT // 2 - 200) #The game over text

    display_score(SCREEN, WIDTH // 2 - 100, HEIGHT // 2 - 100) #The score text
    
    display_inpMessage(SCREEN, WIDTH // 2 - 300, HEIGHT // 2 )

    
    for button in buttons:
        button.draw(SCREEN)
    
    pygame.display.flip()
    
    

    

    pygame.time.Clock().tick(120)