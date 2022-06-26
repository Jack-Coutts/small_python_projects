
# Simple pygame program

# Import and initialize the pygame library
import pygame
import random
import math


def draw_rect(location):

    sq_col = (220, 20, 60)  # Crimson red
    square = pygame.draw.rect(screen, sq_col, pygame.Rect(location, (10, 10)))

    return square


def draw_circle(location):

    green = (60, 179, 113)
    circle = pygame.draw.circle(screen, green, (location), 5)

    return circle


def first_gen_vectors(step_num, circle_num, start_position):

    moves = [10, -10]
    av = []

    for item in circle_num:

        v = []
        x_start = start_position[0]
        y_start = start_position[1]

        for i in step_num:

            x_start += random.choice(moves)
            y_start += random.choice(moves)

            v.append((x_start, y_start))

        av.append(v)

    return av





# Initiate pygame
pygame.init()

fpsClock = pygame.time.Clock()  # Initiate frames per second

# Set up the drawing window
screen = pygame.display.set_mode([600, 600])

# set the pygame window name
pygame.display.set_caption('Genetic Algorithm: Circles to Square')

# Create font object
font_obj = pygame.font.Font('freesansbold.ttf', 16)
text_surface = font_obj.render('Generation: 0', True, (0, 0, 0))  # Render the text/font


vectors = [(20, 20), (40, 40), (60, 60), (80, 80), (90, 90)]
count = 0

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
    square = draw_rect((20, 20))


    c = draw_circle(vectors[count])
    count += 1



    # Add the already created text
    screen.blit(text_surface, (450, 50))



    fpsClock.tick(10)  # 10 frames per second

    # Flip the display
    pygame.display.flip()  # Update the contents of the entire display



# Done! Time to quit.
pygame.quit()