
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
    all_circle_vectors = []

    for item in range(circle_num):

        circle_vectors = []
        x_start = start_position[0]
        y_start = start_position[1]

        for i in range(step_num):

            x_start += random.choice(moves)
            y_start += random.choice(moves)

            circle_vectors.append((x_start, y_start))

        all_circle_vectors.append(circle_vectors)

    return all_circle_vectors


def calc_fitness(all_circle_vectors, target_coordinates, window_height):

    distances = []

    for item in all_circle_vectors:

        steps = len(item)
        destination = item[steps-1]
        distances.append(math.dist((int(destination[0]), int(destination[1])), list(target_coordinates)))

    n_dists = [1 - (item / window_height) for item in distances]  # Normalise (divide by constant & subtract from 1)

    return n_dists


def natural_selection(n_dists):

    mating_pool = []

    for index, item in enumerate(n_dists):  # Index represents circle names

        mating_pool.extend([index for i in range(int(item * 100))])  # Occur 100 * normalised distance

    return mating_pool  # Return mating pool array


def random_mutation(mutation_rate):  # Output true or false based on input probability

    mut_num = 1/mutation_rate  # Range to guess from
    num = random.randint(1, mut_num)  # Number to guess
    guess = random.randint(1, mut_num)  # Guess

    if num == guess:  # If guessed output True
        return True
    else:  # Not guessed output False
        return False


def crossing_over(mother, father, vectors, circle_start_pos):  # Mothers list of circles from mating pool

    gene_length = len(vectors[0])

    all_genes = []

    for x, y in zip(mother, father):

        new_gene = [(vectors[x][item], vectors[y][item]) for item in range(gene_length)]

        for index, item in enumerate(new_gene):

            if random_mutation(0.05):

                ax = random.choice(['x','y'])
                if ax == 'x':

                    mutate = (random.randint(-index-1, index+1)*10) + circle_start_pos[0]
                    l = list(item)
                    l[0] = mutate
                    l = tuple(l)
                    item = l
                else:
                    mutate = (random.randint(1, index + 1) * 10) + circle_start_pos[1]
                    l = list(item)
                    l[1] = mutate
                    l = tuple(l)
                    item = l

            else:
                pass

        all_genes.append(new_gene)

    return all_genes


def reproduction(mating_pool, genes, circle_start_pos):  # Reproduction and crossing over

    mothers = random.sample(mating_pool, len(genes))  # Random sample from mating_pool
    fathers = random.sample(mating_pool, len(genes))  # Random sample from mating_pool

    new_genes = crossing_over(mothers, fathers, genes, circle_start_pos)

    return new_genes


def run_gen_algo(step_num, circle_num, gen_num, start_pos, target_pos, window_height):

    gen_dict = {}
    gen_0 = first_gen_vectors(step_num, circle_num, start_pos)
    gen_dict[0] = gen_0

    for item in range(gen_num):

        if item == 0:

            pass

        else:

            genes = gen_dict[item-1]
            fit = calc_fitness(genes, target_pos, window_height)
            mp = natural_selection(fit)
            new_gen = reproduction(mp, genes, start_pos)
            gen_dict[item] = new_gen

    return gen_dict

circle_start_position = (297.5, 580)
square_position = (20, 20)
target_position = (25, 25)
window_size=[600, 600]

generations = run_gen_algo(100, 10, 20, circle_start_position, target_position, window_size[0])




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