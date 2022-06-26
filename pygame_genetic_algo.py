
# Simple pygame program

# Import and initialize the pygame library
import pygame
import random

pygame.init()

fpsClock = pygame.time.Clock()  # Initiate frames per second

# Set up the drawing window
screen = pygame.display.set_mode([600, 600])

# set the pygame window name
pygame.display.set_caption('Genetic Algorithm: Circles to Square')

# Create font object
font_obj = pygame.font.Font('freesansbold.ttf', 16)
text_surface = font_obj.render('Generation: 0', True, (0, 0, 0))  # Render the text/font

# Run until the user asks to quit
running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with light blue
    screen.fill((173, 216, 230))

    # Draw solid red square
    sq_col = (220, 20, 60)  # Crimson red
    square = pygame.draw.rect(screen, sq_col, pygame.Rect((20, 20), (10, 10)))

    # Circle start coordinates
    cx = 247.5
    cy = 550

    # Draw a solid blue circle in the center
    circles = [pygame.draw.circle(screen, (60, 179, 113), (cx+random.randint(-40, 40), cy+random.randint(-40, 40)), 5) for i in range(10)]

    # Add the already created text
    screen.blit(text_surface, (450, 50))

    fpsClock.tick(10)  # 10 frames per second

    # Flip the display
    pygame.display.flip()  # Update the contents of the entire display

# Done! Time to quit.
pygame.quit()