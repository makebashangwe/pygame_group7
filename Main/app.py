import pygame, sys

class Game:
    def __init__(self):
        pygame.init()

        pygame.display.set_caption("Simple Game")
        self.screen = pygame.display.set_mode((952, 704))

        self.clock = pygame.time.Clock()

        self.img = pygame.image.load("data/images/avatar.png") #avatar
        self.img_pos = [220,500]
        self.bg = pygame.image.load("data/images/bg.png")
        self.bg_pos = [0, 0]

        self.movement = [False,False] #movement variable (upkey, down key)

    def run(self):
        while True:
            self.screen.blit(self.bg, self.bg_pos) #blits the screen with background

            self.img_pos[1] += self.movement[1] - self.movement[0] #updates the vertical position and addss/subtracts from y
                                                                    #based on input.
            self.screen.blit(self.img, self.img_pos) #BLIT's the updated position onto the screen based on if self.movement is true or false.

            for event in pygame.event.get(): #Event Loop
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN: #checks if a key is being pressed (key is down)
                    if event.key == pygame.K_UP: #checks if key is the up arrow
                        self.movement[0] = True #it says its true we're pressing the up key down
                    if event.key == pygame.K_DOWN:
                        self.movement[1] = True #it sets self.movement to true, pressing down key down
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP: #checks if a key was released (key is up)
                        self.movement[0] = False #it sets  up self.movement to false because the key was released.
                    if event.key == pygame.K_DOWN:
                        self.movement[1] = False #it sets self.movement to false since the key was released.
            pygame.display.update()
            self.clock.tick(60)
Game().run()