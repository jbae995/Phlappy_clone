import pygame
import time
from random import *

#adding colors and difficulty levels 7:20
black = (0,0,0)
white = (255,255,255)
pink = (255,223,229)
yellow = (248,207,106)
purple = (42,3,104)

colorChoice = [pink, yellow, purple]

pygame.init()

surfaceWidth = 800
surfaceHeight = 500

imageHeight = 26
imageWidth = 36

surface = pygame.display.set_mode((surfaceWidth, surfaceHeight))
pygame.display.set_caption('Phlappy Bird')
clock = pygame.time.Clock()

img = pygame.image.load('/Users/jsbae/Desktop/Phlappy_clone/bird_1.png')

def score(count):
    font = pygame.font.Font('freesansbold.ttf', 20)
    text = font.render('Score: '+ str(count), True, white)
    surface.blit(text,[0, 0])
    
def blocks(x_block, y_block, block_width, block_height, gap, colorChoice):#blockpipes in game
    pygame.draw.rect(surface, colorChoice, [x_block, y_block, block_width, block_height])
    pygame.draw.rect(surface, colorChoice, [x_block, y_block + block_height + gap, block_width, surfaceHeight])
    
def replay_or_quit():
    for event in pygame.event.get([pygame.KEYDOWN, pygame.KEYUP, pygame.QUIT]):
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            continue
        
        return event.key
    return None

def makeTextObjs(text, font):#creating text
    textSurface = font.render(text, True, yellow)
    return textSurface, textSurface.get_rect()

def msgSurface(text):#message when gameover
    smallText = pygame.font.Font('freesansbold.ttf', 20)
    largeText = pygame.font.Font('freesansbold.ttf', 45)

    titleTextSurf, titleTextRect = makeTextObjs(text, largeText)
    titleTextRect.center = surfaceWidth / 2, surfaceHeight / 2
    surface.blit(titleTextSurf, titleTextRect)#text

    typTextSurf, typTextRect = makeTextObjs('Press any KEY to continue, gamer', smallText)
    typTextRect.center = surfaceWidth / 2, ((surfaceHeight / 2) + 100)
    surface.blit(typTextSurf, typTextRect)#textandrectangle

    pygame.display.update() #actually displaying output on screen.if this code is not here, display does not update and when crash, bird will go into own loop and won't show anything
    time.sleep(1)
    #sleep time

    while replay_or_quit() == None:
        clock.tick()

    main()
    
def gameOver():
    msgSurface('YOU FUCKING KILLED THE BIRD!')
  
def phlappy(x, y, image):#image
    surface.blit(img, (x, y))
    
def main():
    x = 150
    y = 200
    #where the img starts
    y_move = 0
    #moves up 5px; if changed, can control the amount of movement
    
    x_block = surfaceWidth
    y_block = 0

    block_width = 75
    block_height = randint(0, (surfaceHeight/2))
    gap = imageHeight * 3
    block_move = 6

    current_score = 0 #scoreboard
    
    game_over = False
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    y_move = -5 #means up
                    
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    y_move = 5 #moves bird up

        y += y_move
        
        surface.fill(black)
        phlappy(x, y, img)
        score(current_score)

        blocks(x_block, y_block, block_width, block_height, gap)
        x_block -= block_move

        if y > surfaceHeight - 40 or y < 0:
            gameOver()

        if x_block < (-1 * block_width):
            x_block = surfaceWidth
            #immediately creates new block after old block disappears off screen
            block_height = randint(0, (surfaceHeight/2))

        if x  + imageWidth > x_block:#upper block crash
            if x < x_block + block_width:
                #print('possibly within boundaries of x upper')
                if y < block_height:
                    #print('Y crossover UPPER')
                    if x - imageWidth < block_width + x_block:
                        #print('game over, hit upper')
                        gameOver()

        if x + imageWidth > x_block:#lower block crash
            #print('x crossover')
            if y + imageHeight > block_height + gap:
                #print('Y crossover lower')
                if x < block_width + x_block:
                    #print('game over lower')
                    gameOver()

        if x < x_block and x > x_block - block_move:
            current_score += 1
                

        pygame.display.update()
        #specific areas updated
        #can use flip instead
        clock.tick(60)
        #means we run the game code 60times persec
        #game will be 60frames per sec fps
        #games like flappy bird is a lot dependent on this. most games actually

main()
pygame.quit()
quit()














