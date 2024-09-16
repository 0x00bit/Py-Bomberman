import pygame, sys
from level import *

# Configurations
WINDOW_NAME = 'Rhythm '
WIDTH, HEIGHT = 1280, 720

def run():
    pygame.init()
    # Resolution
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    # Title 
    title = pygame.display.set_caption(WINDOW_NAME)
    # FPS
    clock = pygame.time.Clock()

    teste = pygame.image.load('assets/characters/Char_001.png').convert_alpha()

    while True:
        screen.fill((50,50,50))  # Remember to remove
        character_01 = load_sprites(teste, 72, 72)
        screen.blit(character_01, (0,0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()  # Update the display
        clock.tick(60)  # FPS control, limit to 60 FPS

run() 
