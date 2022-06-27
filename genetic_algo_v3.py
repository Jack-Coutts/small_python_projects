
import random

# Define function for optimisation
def sum_listed_vectors(initial_position, list_of_coordinate):  # Finds final position given after list of moves


    pass


def create_individual(move_num, max_move):  # Create individual with all moves they will make

    moves = [[random.randint(1, max_move + 1), random.randint(1, max_move + 1)] for item in range(move_num)]

    return moves  # Return list of [x_move, y_move] for number of moves. Moves size randint from max_move.


def create_population(pop_number, move_num, max_move):  # Create multiple individuals.

    population = [create_individual(move_num, max_move) for i in range(pop_number)]

    return population  # List of lists. Each sublist is an individual.


def target_square(square_centre, side_length):  # Define the x & y coordinates that the square covers

    x_range = list(range(square_centre[0]-(side_length/2)))  # Square coordinates on x axis
    y_range = list(range(square_centre[1]-(side_length/2)))  # Square coordinates on y axis

    return x_range, y_range  # Return two lists, one per axis, containing possible target coordinates



# Testing

ind = create_individual(20, 10)

pop = create_population(10, 10, 10)

print(pop)