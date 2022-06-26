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



v = first_gen_vectors(100, 10, (250, 250))

f = calc_fitness(v, [500, 500], 600)

m = natural_selection(f)

print(m)