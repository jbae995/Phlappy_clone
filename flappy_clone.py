import pygame

black = (0,0,0)
white = (255,255,255)

pygame.init()
surface = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Phlappy Bird')
clock = pygame.time.Clock()
game_over = False

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    pygame.display.update()
    #specific areas updated
    #can use flip instead
    clock.tick(60)
    #means we run the game code 60times persec
    #game will be 60frames per sec fps
    #games like flappy bird is a lot dependent on this. most games actually

pygame.quit()
quit()






