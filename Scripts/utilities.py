import pygame

BASE_IMG_PATH = 'data/images/'

def load_image(path): #LOAD IMAGE FUNCTION
    img = pygame.image.load(BASE_IMG_PATH + path).convert()
    return img