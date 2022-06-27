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
        self.move_history = []
        self.future = []

    def crossing_over(self, father, mother, move_size, mutation_rate):

        future_moves = []

        for item in range(len(father.move_history)):

            coin_toss = random.choice(list(range(int(1/mutation_rate))))  # Determine whether mutation

            if item % 2 == 0:
                if coin_toss != 1:
                    future_moves.append(father.move_history[item])
                else:
                    future_moves.append([item * random.choice(list(range(-move_size, move_size))),
                                         item * random.choice(list(range(-move_size, move_size)))])  # Mutation

            else:
                if coin_toss != 1:
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
        self.move_history.append(self.xy)  # Update move history


# Target box
class TargetSquare:

    def __init__(self, center_xy, side_len):

        self.center_xy = center_xy
        self.side_len = side_len
        self.x = center_xy[0]
        self.y = center_xy[1]
        self.x_range = list(range(math.floor((self.x - (side_len/2))), math.floor((self.x + (side_len/2)))))
        self.y_range = list(range(math.floor((self.y - (side_len/2))), math.floor((self.y + (side_len/2)))))


def move_first_gen(num_of_circles, num_of_moves, start_pos, move_size):

    circle_lst = []

    for index in range(num_of_circles):

        circle = Individual(start_pos, 5)

        for move in range(num_of_moves):

            circle.move(move_size)

        circle_lst.append(circle)

    return circle_lst


def calc_fitness(circle, square, window_height):

    distance = math.dist(circle.xy, square.center_xy)  # Euclidean distance
    normalised_dist = 1-(distance / window_height)
    return normalised_dist


def natural_selection(circle_lst, square, window_height):

    reached_square = 0
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

        mating_pool.extend([index for i in range(int(item * 1000))])  # Occur 100 * normalised distance

    mothers = random.sample(mating_pool, len(circle_lst))  # Random sample of mating pool for mothers
    fathers = random.sample(mating_pool, len(circle_lst))  # Random sample of mating pool for fathers

    av_n_dist = sum(n_dists)/len(n_dists)

    return mothers, fathers, reached_square, av_n_dist


def next_generation(mothers, fathers, circle_lst, generation, mutation_rate, start_pos):

    children = []

    for mother, father in zip(mothers, fathers):

        child = Child(start_pos, 5, generation)
        child.crossing_over(circle_lst[father], circle_lst[mother], move_size, mutation_rate)
        children.append(child)

    return children


def move_children(children):

    move_num = len(children[0].future)

    for child in children:

        for move in range(move_num):

            child.next_move(move)

    return children


def generations(gen_number, square, circle_num, move_num,
                start_pos, move_size, window_height, mutation_rate ):

    n_dists = []
    made_it = []
    generation = []

    for number in range(gen_number):

        if number == 0:

            circles = move_first_gen(circle_num, move_num, start_pos, move_size)
            mothers, fathers, reached_square, av_n_dist = natural_selection(circles, square, window_height)

            n_dists.append(av_n_dist)
            made_it.append(reached_square)

            children = next_generation(mothers, fathers, circles, 1, mutation_rate, start_pos)

            move_children(children)

            generation.append(children)

        else:

            cir = generation[number-1]
            mothers, fathers, reached_square, av_n_dist = natural_selection(cir, square, window_height)
            n_dists.append(av_n_dist)
            made_it.append(reached_square)

            children = next_generation(mothers, fathers, cir, 1, mutation_rate, start_pos)
            move_children(children)

            generation.append(children)

    return n_dists, made_it


move_size = 50
mutation_rate = 0.05
start_pos = [400, 400]
square_center = [25, 25]
sq_side_len = 10
move_num = 500
circle_num = 100
window_height = 600
gen_number = 1000


# Test
square = TargetSquare(square_center, sq_side_len)

nd, mi = generations(gen_number, square, circle_num, move_num, start_pos, move_size, window_height, mutation_rate)


print(mi)