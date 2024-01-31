import sys 
import pygame 
pygame.init()

font = pygame.font.Font(None, 26)
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
BUTTON_HEIGHT = 82
BUTTON_WIDTH = 200
FPS = 60

#create the background
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Settings")

CLOCK = pygame.time.Clock()

ST = pygame.image.load("LB2.jpg")

image = pygame.image.load('ARROW.png').convert_alpha()
    # Set the position of the sprite 
MENU_BUTTON = image.get_rect() 
MENU_BUTTON.center=(BUTTON_WIDTH//2, BUTTON_HEIGHT//2)
BUTTON_TEXT= font.render("Back to Menu", True, (255,255,255))

#create a dictionary
MY_SETTINGS = [
    {"Command": "Press < to", "Outcome": "Make the player move left"},
    {"Command": "press > to", "Outcome": "Make the player move right"},
    {"Command": "press SPACE BAR to", "Outcome": "Make the player jump"},
    ]

def settings():

    y_offset = 200
    for i in MY_SETTINGS:
        TEXT = f"{i['Command']}: {i['Outcome']}"
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
    
    SCREEN.blit(ST, (0,0))
    SCREEN.blit(image, (0,0))
    SCREEN.blit(BUTTON_TEXT, (MENU_BUTTON.x + 30, MENU_BUTTON.y + 30))
    settings()

    pygame.display.flip()
    CLOCK.tick(FPS)
pygame.quit()
sys.exit()