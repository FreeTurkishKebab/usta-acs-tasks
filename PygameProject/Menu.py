import pygame 
import sys 
from pygame.locals import *
from pygame import mixer
#make a background music 
mixer.init()
mixer.music.load('MenuM.mp3')
mixer.music.play()

pygame.init()


#define and give values to the dimensions 
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
BUTTON_WIDTH = 200
BUTTON_HEIGHT = 50
BUTTON_TEXT_COLOR = (0, 0, 0)
FONT = pygame.font.Font('freesansbold.ttf', 36)


#make the a variable to display the screen using screen mode 
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Game Menu")

#save an image to add to the background 
background_image = pygame.image.load("BG.jpg")
#save an image to add to the buttons 
wood_texture = pygame.image.load("wood_texture.png")



#make the classes for the functions and the looks of the button
class Button:
    def __init__(self, x, y, width, height, text, action):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text 
        self.action = action 
    
    def draw(self, screen):
        screen.blit(wood_texture, self.rect)
        pygame.draw.rect(screen, (0, 0, 0), self.rect, 2) #wooden border 
        text_surface = FONT.render(self.text, True, BUTTON_TEXT_COLOR)
        text_rect = text_surface.get_rect(center = self.rect.center)
        screen.blit(text_surface, text_rect)
    
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                self.action()
def start_game():
    import ProjectV2
    open(file="ProjectV2.py")

def quit_game():
    pygame.quit()
    sys.exit()

def leaderboard():
    import LB
    open(file="LB.py")

#create the buttons on the screen
start_button = Button(
    SCREEN_WIDTH // 2 - BUTTON_WIDTH // 2, 
    SCREEN_HEIGHT // 2 - BUTTON_HEIGHT // 2 - 50 ,
    BUTTON_WIDTH,
    BUTTON_HEIGHT, 
    "Start",
    start_game,
)

quit_button = Button(
    SCREEN_WIDTH // 2 - BUTTON_WIDTH // 2, 
    SCREEN_HEIGHT // 2 - BUTTON_HEIGHT // 2 + 150, 
    BUTTON_WIDTH,
    BUTTON_HEIGHT, 
    "Quit" ,
    quit_game
)

LB_button = Button(
    SCREEN_WIDTH // 2 - BUTTON_WIDTH // 2, 
    SCREEN_HEIGHT // 2 - BUTTON_HEIGHT // 2 + 50, 
    BUTTON_WIDTH,
    BUTTON_HEIGHT, 
    "Scores",
    leaderboard
)

buttons = [start_button, quit_button, LB_button]

#the main game loop to make the menu 
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        for button in buttons:
            button.handle_event(event)

    screen.blit(background_image, (0, 0)) #draw the background image

    for button in buttons:
        button.draw(screen)

    pygame.display.flip()
    
