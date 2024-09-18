import pygame

pygame.init()  # initializes pygame
clock = pygame.time.Clock()  # initializes the game clock/frame rate
screen = pygame.display.set_mode((500, 500))  # creates the screen
rect1_speed = [5, 5]  # a variable to track the speed of the square
rect1 = pygame.Rect(0, 0, 200, 200)  # creates a rectangle with the dimensions of 200x200 at the origin
surf = pygame.Surface((rect1.w, rect1.h))  # creates the surface with the same dimensions of the rectangle
surf.fill((255, 0, 0))  # makes the surface red

running = True

while running:  # infinite loop
    for event in pygame.event.get():  # sees if the user has clicked an event
        if event.type == pygame.QUIT:  # if the event is to quit
            running = False  # end the game loop / end the game

    # Check if the rectangle is out of bounds and reverse direction if needed
    if rect1.x < 0 or rect1.x + rect1.width > 500:
        rect1_speed[0] = -rect1_speed[0]
    if rect1.y < 0 or rect1.y + rect1.height > 500:
        rect1_speed[1] = -rect1_speed[1]

    # Move the rectangle by its current speed
    rect1 = rect1.move(rect1_speed)

    screen.fill((0, 0, 0))  # "erases" the old square so a new one can be redrawn
    screen.blit(surf, rect1.topleft)  # displays red rectangle at the updated position
    pygame.display.flip()  # updates the entire screen
    clock.tick(60)  # how often the screen updates

pygame.quit()  # properly quits pygame