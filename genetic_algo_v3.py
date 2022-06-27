import random
import math


# Create individuals
class Individual:

    # Initiate constructor
    def __init__(self, xy, diameter):  # Input xy coordinates [x, y] and diameter
        self.xy = xy
        self.x = xy[0]  # Can call x or y individually
        self.y = xy[1]
        self.size = diameter
        self.move_history = []
        self.generation = 0

    # Move circle
    def move(self, move_size):  # Input size of possible moves

        possible_moves = list(range(-move_size, move_size))  # Positive and negative moves
        new_position = [self.x + random.choice(possible_moves), self.y + random.choice(possible_moves)]
        self.move_history.append(self.xy)  # Keep record of old positions
        self.xy = new_position  # Update xy with new positions
        self.x = new_position[0]  # Update x with new position
        self.y = new_position[1]  # Update y with new position

    def check_square(self, square):  # Check whether individual in square

        if self.y in square.y_range and self.x in square.x_range:
            return True
        else:
            return False


# Children - all individuals after first generation
class Child(Individual):

    def __init__(self, xy, diameter, generation):
        Individual.__init__(self, xy, diameter)
        self.generation = generation
        self.future = []

    def crossing_over(self, father, mother, move_size, mutation_rate):

        future_moves = []

        for item in range(len(father.move_history)):

            coin_toss = random.choice(random.choice(list(range(1/mutation_rate))))  # Determine whether mutation

            if item % 2 == 0:
                if coin_toss == 1:
                    future_moves.append(father.move_history[item])
                else:
                    future_moves.append([item * random.choice(list(range(-move_size, move_size))),
                                         item * random.choice(list(range(-move_size, move_size)))])  # Mutation

            else:
                if coin_toss == 1:
                    future_moves.append(mother.move_history[item])
                else:
                    future_moves.append([item * random.choice(list(range(-move_size, move_size))),
                                         item * random.choice(list(range(-move_size, move_size)))])  # Mutation

        self.future = future_moves

    def next_move(self, prev_moves):

        new_position = self.future[prev_moves]
        self.xy = new_position  # Update xy with new positions
        self.x = new_position[0]  # Update x with new position
        self.y = new_position[1]  # Update y with new position
        self.move_history.append[self.xy]  # Update move history


# Target box
class TargetSquare:

    def __init__(self, center_xy, side_len):

        self.center_xy = center_xy
        self.side_len = side_len
        self.x = center_xy[0]
        self.y = center_xy[1]
        self.x_range = list(range(math.floor((self.x - (side_len/2))), math.floor((self.x + (side_len/2)))))
        self.y_range = list(range(math.floor((self.y - (side_len/2))), math.floor((self.y + (side_len/2)))))


def move_first_gen(num_of_circles, num_of_moves, start_pos):

    circle_lst = []

    for index in range(num_of_circles):

        circle = Individual(start_pos, 5)

        for move in range(num_of_moves):

            circle.move(10)

        circle_lst.append(circle)

    return circle_lst


def calc_fitness(circle, square, window_height):

    distance = math.dist(circle.xy, square.center_xy)  # Euclidean distance
    normalised_dist = 1-(distance - window_height)
    return normalised_dist


def natural_selection(circle_lst, square, window_height):

    reached_square = []
    mating_pool = []
    n_dists = []

    for circle in circle_lst:

        if circle.check_square(square):
            reached_square += 1
            fit = calc_fitness(circle, square, window_height)
            n_dists.append(fit)
        else:
            fit = calc_fitness(circle, square, window_height)
            n_dists.append(fit)

    for index, item in enumerate(n_dists):  # Index represents circle names

        mating_pool.extend([index for i in range(int(item * 100))])  # Occur 100 * normalised distance

    mothers = random.sample(mating_pool, len(circle_lst))  # Random sample of mating pool for mothers
    fathers = random.sample(mating_pool, len(circle_lst))  # Random sample of mating pool for fathers

    return mothers, fathers


def next_generation():

    pass




def move_child_gen():

    pass





square = TargetSquare([25, 25], 10)



circles = move_first_gen(10, 10, [10, 10])

for item in circles:

    print(item.move_history)

print(circles[0].check_square(square))




