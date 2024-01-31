import sys 
#from ProjectUpdating import current_score
import pygame 
pygame.init()

font = pygame.font.Font(None, 36)
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
BUTTON_HEIGHT = 82
BUTTON_WIDTH = 200
FPS = 60

#---------------------Grab the high scores and scores from the main game----------------
high_score = 0
with open("high_score.txt", "r") as file:
    high_score = int(file.read())

print("High Score:", high_score)

#---------------Start creating the leaderboard------------------
#create the background
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Leader Board")

CLOCK = pygame.time.Clock()

LB = pygame.image.load("LB2.jpg")

image = pygame.image.load('ARROW.png').convert_alpha()
    # Set the position of the sprite 
MENU_BUTTON = image.get_rect() 
MENU_BUTTON.center=(BUTTON_WIDTH//2, BUTTON_HEIGHT//2)
BUTTON_TEXT= font.render("Back to Menu", True, (255,255,255))
#------------------Create a def for the scores---------------
def read_high_score():
    with open("high_score.txt", "r") as file:
        high_score = int(file.read())
    return high_score

def display_high_score(SCREEN, font):
    high_score = read_high_score()
    text = font.render("High Score: {}".format(high_score), True, (255,255,255))
    SCREEN.blit(text, (200, 200))
#create a dictionary
MY_LEADER_BOARD = [
    {"Position": "1st place", "Players Name": "GC", "Players Score": 250},
    {"Position": "2nd place", "Players Name": "TP", "Players Score": 249},
    {"Position": "3rd place", "Players Name": "GC", "Players Score": 199},
    ]

def scoreboard():

    y_offset = 200
    for i in MY_LEADER_BOARD:
        TEXT = f"{i['Position']}: {i['Players Name']}: {i['Players Score']}"
        BGTEXT=font.render(TEXT, True, (255,255,255))
        SCREEN.blit(BGTEXT, (200, y_offset))
        y_offset += 50





running = True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button==1:
                if MENU_BUTTON.collidepoint(event.pos):
                    import Menu
                    open(file="Menu.py")
    
    #---------------Deal with the high scores----------
    display_high_score(SCREEN, font)

    #---------Screen blits----------
    SCREEN.blit(LB, (0,0))
    SCREEN.blit(image, (0,0))
    SCREEN.blit(BUTTON_TEXT, (MENU_BUTTON.x + 30, MENU_BUTTON.y + 30))
    scoreboard()

    pygame.display.flip()
    CLOCK.tick(FPS)
pygame.quit()
sys.exit()

