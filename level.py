import pygame

def load_sprites(sheet, width, height):
    image = pygame.Surface((width, height)).convert_alpha()
    image.blit(sheet, (0, 0), (0, 0, width, height))
    return image

