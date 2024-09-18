import pygame
import sys
from Scripts.entities import PhysicsEntity

class Game:
    def __init__(self):
        pygame.init()

        pygame.display.set_caption("Simple Game")
        self.screen = pygame.display.set_mode((952, 704))

        self.clock = pygame.time.Clock()

        self.img = pygame.image.load("data/images/entities/player.png") #avatar
        self.img_pos = [220,500]
        self.bg = pygame.image.load("data/images/bg.png")
        self.bg_pos = [0, 0]

        self.movement = [False,False, False, False] #movement variable (up key, down key, right key, left key)

        self. collision_area = pygame.Rect(50,50,300,50)
        self.player =  PhysicsEntity(self, 'player', (50,50), (8,15))

    def run(self):
        while True:
            self.screen.blit(self.bg, self.bg_pos) #blits the screen with background
            self.img_pos[1] += self.movement[1] - self.movement[
                0]  # updates the vertical position and addss/subtracts from y
            # based on input.
            self.screen.blit(self.img, self.img_pos)  # BLIT's the updated position onto the screen based on if self.movement is true or false.

            '''To test if Collisions working, use:
            img_r = pygame.Rect(self.img_pos[0], self.img_pos[1], self.img.get_width(), self.img.get_height()) #creates a rect (x, y width, height) with same dimentions of the img we dew.

            pygame.Rect(*self.img_pos, *self.img.get_size())
            if img_r.colliderect(self.collision_area):
                pygame.draw.rect(self.screen, (0,100,255), self.collision_area)
            else:
                pygame.draw.rect(self.screen, (0,50,155), self.collision_area)
            '''
            #updade avatar position based on movement flags
            if self.movement[0]: #up
                self.img_pos[1] -=5 #moves y up
            if self.movement[1]:  # down
                self.img_pos[1] +=5 #moves y down
            if self.movement[2]:  # left
                self.img_pos[0] +=5 # moves x left
            if self.movement[3]:  # right
                self.img_pos[0] -=5 #moves x right


            for event in pygame.event.get(): #Event Loop
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN: #checks if a key is being pressed (key is down)/ Character movement
                    if event.key == pygame.K_w or event.key == pygame.K_UP: #checks if key is the up arrow
                        self.movement[0] = True #it says its true we're pressing the up key down
                    if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                        self.movement[1] = True #it sets self.movement to true, pressing down key down
                    if event.key == pygame.K_a or event.key == pygame.K_RIGHT:
                        self.movement[2] = True
                    if event.key == pygame.K_d or event.key == pygame.K_LEFT:
                        self.movement[3] = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_w or event.key ==pygame.K_UP: #checks if a key was released (key is up)
                        self.movement[0] = False #it sets  up self.movement to false because the key was released.
                    if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                        self.movement[1] = False #it sets self.movement to false since the key was released.
                    if event.key == pygame.K_a or event.key == pygame.K_RIGHT:
                        self.movement[2] = False
                    if event.key == pygame.K_d or event.key == pygame.K_LEFT:
                        self.movement[3] = False

            pygame.display.update()
            self.clock.tick(60)
Game().run()