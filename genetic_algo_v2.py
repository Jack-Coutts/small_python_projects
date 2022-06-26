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

print(first_gen_vectors(100, 10, (250, 250)))