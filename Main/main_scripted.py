import pygame
import sys
from Scripts.entities import PhysicsEntity
from Scripts.utilities import load_image

class Game:
    def __init__(self):
        pygame.init()

        pygame.display.set_caption("Simple Game")
        self.screen = pygame.display.set_mode((952, 704))
        self.bg = pygame.image.load("data/images/bg.png")
        self.bg_pos = [0, 0]
        self.clock = pygame.time.Clock()
        self.assets = {
            'player': load_image('entities/player.png')
        }
        self.player = PhysicsEntity(self, 'player', (50,50), (8,15))
        self.movement = [False, False, False, False]  # movement variable (up key, down key, right key, left key)

    def run(self):
        while True:
            self.screen.blit(self.bg, self.bg_pos)  # blits the screen with background
            self.player.update((self.movement[0] - self.movement[0], 0))
            self.player.render(self.screen)

            for event in pygame.event.get():  # Event Loop
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:  # checks if a key is being pressed (key is down)/ Character movement
                    if event.key == pygame.K_w or event.key == pygame.K_UP:  # checks if key is the up arrow
                        self.movement[0] = True  # it says its true we're pressing the up key down
                    if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                        self.movement[1] = True  # it sets self.movement to true, pressing down key down
                    if event.key == pygame.K_a or event.key == pygame.K_RIGHT:
                        self.movement[2] = True
                    if event.key == pygame.K_d or event.key == pygame.K_LEFT:
                        self.movement[3] = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_w or event.key == pygame.K_UP:  # checks if a key was released (key is up)
                        self.movement[0] = False  # it sets  up self.movement to false because the key was released.
                    if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                        self.movement[1] = False  # it sets self.movement to false since the key was released.
                    if event.key == pygame.K_a or event.key == pygame.K_RIGHT:
                        self.movement[2] = False
                    if event.key == pygame.K_d or event.key == pygame.K_LEFT:
                        self.movement[3] = False

            pygame.display.update()
            self.clock.tick(60)


Game().run()