
# Simple pygame program

# Import and initialize the pygame library
import pygame
import random

pygame.init()

fpsClock = pygame.time.Clock()  # Initiate frames per second

# Set up the drawing window
screen = pygame.display.set_mode([500, 500])

# Run until the user asks to quit
running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with white
    screen.fill((255, 255, 255))

    x = 250
    y = 250

    # Draw a solid blue circle in the center
    circles = [pygame.draw.circle(screen, (0, 0, 255), (x+random.randint(-40, 40), y+random.randint(-40, 40)), 5) for i in range(10)]

    fpsClock.tick(10)  # 10 frames per second

    # Flip the display
    pygame.display.flip()  # Not sure what it does but is essential

# Done! Time to quit.
pygame.quit()