import pygame, sys

class Game:
    def __init__(self):
        pygame.init()

        pygame.display.set_caption("Simple Game")
        self.screen = pygame.display.set_mode((952, 704))

        self.clock = pygame.time.Clock()

        self.img = pygame.image.load("data/images/avatar.png") #avatar
        self.img_pos = [220,500]

        self.movement = [False,False] #movement variable

    def run(self):
        while True:
            self.screen.fill((14,219,248)) #fill the screen with blue

            self.img_pos[1] += self.movement[1] - self.movement[0] #updates the vertical position and addss/subtracts from y
                                                                    #based on input.
            self.screen.blit(self.img, self.img_pos) #BLIT's the updated position onto the screen based on if self.movement is true or false.

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN: #checks if the event is a key release
                    if event.key == pygame.K_UP: #checks if the released key is the up arrow
                        self.movement[0] = True #it sets self.movement to true, adding 0 to y
                    if event.key == pygame.K_DOWN:
                        self.movement[1] = True #it sets self.movement to true, adding 1 to y
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP:
                        self.movement[0] = False #it sets self.movement to false, adding 0 to y
                    if event.key == pygame.K_DOWN:
                        self.movement[1] = False #it sets self.movement to true, adding 1 to y
            pygame.display.update()
            self.clock.tick(60)
Game().run()