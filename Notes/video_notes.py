import sys
import pygame

#surface = image, screen is a special type of surface.

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Hello World")  # Game Name/Window Name
        self.screen = pygame.display.set_mode((640, 480))  # creates the window , resolution in pixels
        self.clock = pygame.time.Clock() #clock oject

        self.img = pygame.image.load('data/images/clouds/cloud_1.png') #will create the background
        self.img_pos = [160,200] #makes it easier to change the position code without editing the blit function
    def run(self):
        while True:  #gameloop
            self.screen.blit(self.img, self.img_pos) #blit places self.img on the screen
            for event in pygame.event.get():  ###pygame.event.get() gets user input so the window doens't freeze, and event is any sort of input from the mouse, keyboard, etc.
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            pygame.display.update()  # will continuously update the screen so it's not black
            self.clock.tick(60)  # framerate, will maintain 60fps


Game().run()