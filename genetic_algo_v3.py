
import random

# Define function for optimisation
def sum_listed_vectors(initial_position, list_of_coordinate):  # Finds final position given after list of moves




    pass


def create_individual(move_num, max_move):

    moves = [[random.randint(1, max_move + 1), random.randint(1, max_move + 1)] for item in range(move_num)]

    return moves

print(create_individual(20, 10))