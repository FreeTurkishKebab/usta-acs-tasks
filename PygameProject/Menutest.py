import pygame
from pygame.locals import *

pygame.init()


width = 640
height = 480
screen = pygame.display.set_mode([width, height])
pygame.display.set_caption("jump jump mania")

fps = 60
timer = pygame.time.Clock()
mainMenu = True #so the menu opens instantly 
bg = pygame.image.load("MenuBG.png")
font = pygame.font.Font('freesansbold.ttf', 24)



class button:
    def __init__(self, txt, pos, exitButton):
        self.text = txt
        self.pos=pos
        self.button = pygame.rect.Rect((self.pos[0], self.pos[1], (260, 40)))
        self.exitButton = exitButton
    
    def drawExit():
        exitButton = pygame.draw.rect(screen, 'black', [220, 390, 200, 60], 0, 5)
        pygame.draw.rect(screen, 'ghostwhite', [220, 390, 200, 60], 5, 5)
        exittxt = font.render('Exit', True, 'ghostwhite')
        screen.blit(exittxt,(290, 410))
        if exitButton.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
            run = False

    def drawMenu():
        menuButton = pygame.draw.rect(screen, 'black', [220, 20, 200, 60], 0, 5)
        pygame.draw.rect(screen, 'ghostwhite', [220, 20, 200, 60], 5, 5)
        mainMenutxt = font.render('Start', True, 'ghostwhite')
        screen.blit(mainMenutxt,(290, 40))
        if menuButton.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
            menu = True 
        else:
            menu = False
        return menu

run = True

while run:
    screen.blit(bg,(0,0))
    timer.tick(fps)
    if mainMenu:
        button.drawMenu()
        button.drawExit()

    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            run = False
    pygame.display.flip()

pygame.quit()