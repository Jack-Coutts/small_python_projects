import pygame
import random
import math


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

            circle_vectors.append([x_start, y_start])

        all_circle_vectors.append(circle_vectors)

    return all_circle_vectors


def calc_fitness(all_circle_vectors, target_coordinates, window_height):

    distances = []

    for item in all_circle_vectors:

        steps = len(item)
        destination = item[steps-1]
        distances.append(math.dist(destination, target_coordinates))

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

        new_gene = [[vectors[x][item][0], vectors[y][item][1]] for item in range(gene_length)]

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


v = first_gen_vectors(100, 10, [250, 250])

f = calc_fitness(v, [500, 500], 600)

m = natural_selection(f)

r = reproduction(m, v, [250, 250])

print(r)