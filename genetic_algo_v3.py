import random
import math


# Create individuals
class Individual:

    # Initiate constructor
    def __init__(self, xy, diameter):  # Input xy coordinates [x, y] and diameter
        self.xy = xy  # [x, y] coordinates
        self.x = xy[0]  # Can call x or y individually
        self.y = xy[1]
        self.size = diameter  # Diameter of circle
        self.move_history = []  # Each previous move made by circle
        self.generation = 0  # Which generation

    # Move circle
    def move(self, move_size):  # Input size of possible moves

        possible_moves = list(range(-move_size, move_size))  # Positive and negative moves
        new_position = [self.x + random.choice(possible_moves), self.y + random.choice(possible_moves)]
        self.move_history.append(self.xy)  # Keep record of old positions
        self.xy = new_position  # Update xy with new positions
        self.x = new_position[0]  # Update x with new position
        self.y = new_position[1]  # Update y with new position

    def check_square(self, square):  # Check whether individual in square

        if self.y in square.y_range and self.x in square.x_range:  # Square class has these attributes
            return True
        else:
            return False


# Children - all individuals after first generation
class Child(Individual):

    def __init__(self, xy, diameter, generation):  # Must input generation number here
        Individual.__init__(self, xy, diameter)
        self.generation = generation
        self.move_history = []  # Also has move history
        self.future = []  # Future moves created from parents

    def crossing_over(self, father, mother, move_size, mutation_rate):  # Reproduction from parents

        future_moves = []  # Moves inherited from parents

        for item in range(len(father.move_history)):  # Iterate over each step/move

            coin_toss = random.choice(list(range(int(1/mutation_rate))))  # Determine whether mutation

            if item % 2 == 0:  # Even move indexes from father
                if coin_toss != 1:
                    future_moves.append(father.move_history[item])  # No mutation
                else:  # Mutation
                    future_moves.append([item * random.choice(list(range(-move_size, move_size))),
                                         item * random.choice(list(range(-move_size, move_size)))])  # Mutation

            else:  # Odd move indexes from mother
                if coin_toss != 1:  # No mutation
                    future_moves.append(mother.move_history[item])
                else:  # Mutation
                    future_moves.append([item * random.choice(list(range(-move_size, move_size))),
                                         item * random.choice(list(range(-move_size, move_size)))])  # Mutation

        self.future = future_moves  # Add inherited future moves to circle attributes

    def next_move(self, prev_moves):  # Move along list of future moves

        new_position = self.future[prev_moves]  # Select which move to make
        self.xy = new_position  # Update xy with new positions
        self.x = new_position[0]  # Update x with new position
        self.y = new_position[1]  # Update y with new position
        self.move_history.append(self.xy)  # Update move history


# Target box
class TargetSquare:

    def __init__(self, center_xy, side_len):

        self.center_xy = center_xy  # Center coordinates of the ssquare
        self.side_len = side_len  # Length of square sides
        self.x = center_xy[0]  # x center
        self.y = center_xy[1]  # y center
        self.x_range = list(range(math.floor((self.x - (side_len/2))), math.floor((self.x + (side_len/2)))))  # x side
        self.y_range = list(range(math.floor((self.y - (side_len/2))), math.floor((self.y + (side_len/2)))))  # y side


def move_first_gen(num_of_circles, num_of_moves, start_pos, move_size):  # Move first generation of circles

    circle_lst = []  # Create each circle

    for index in range(num_of_circles):  # Iterate of num of circles

        circle = Individual(start_pos, 5)  # Create a circle

        for move in range(num_of_moves):  # Iterate over move num

            circle.move(move_size)  # Make all moves

        circle_lst.append(circle)  # Add created circles to list

    return circle_lst  # Return list of moves circles


def calc_fitness(circle, square, window_height):  # Determine fitness of moved circle

    distance = math.dist(circle.xy, square.center_xy)  # Euclidean distance
    normalised_dist = 1-(distance / window_height)  # Normalise distance measures
    return normalised_dist


def natural_selection(circle_lst, square, window_height):  # Select best circles for reproduction

    reached_square = 0  # Number of circles hitting the square
    mating_pool = []  # Pool of circles to select from for mating
    n_dists = []  # Normalised distance for each circle

    for circle in circle_lst:  # Iterate over circles

        if circle.check_square(square):  # Check whether circle in square
            reached_square += 1  # Count of circles reaching square
            fit = calc_fitness(circle, square, window_height)  # Calc fitness
            n_dists.append(fit)  # Add fitness
        else:  # Circle not reaches square
            fit = calc_fitness(circle, square, window_height)  # Calc fitness
            n_dists.append(fit)  # Add fitness

    for index, item in enumerate(n_dists):  # Index represents circle names

        mating_pool.extend([index for i in range(int(item * 1000))])  # Occur 100 * normalised distance

    mothers = random.sample(mating_pool, len(circle_lst))  # Random sample of mating pool for mothers
    fathers = random.sample(mating_pool, len(circle_lst))  # Random sample of mating pool for fathers

    av_n_dist = sum(n_dists)/len(n_dists)  # Average normalised distance for this generation

    return mothers, fathers, reached_square, av_n_dist  # Return selected mothers & fathers, num successful & n_dists


def next_generation(mothers, fathers, circle_lst, generation, mutation_rate, start_pos):  # Create next gen

    children = []  # List of child circles

    for mother, father in zip(mothers, fathers):  # Iterate over parents

        child = Child(start_pos, 5, generation)  # create child
        child.crossing_over(circle_lst[father], circle_lst[mother], move_size, mutation_rate)  # Inherit moves
        children.append(child)  # Add child to list

    return children  # List of child generation


def move_children(children):  # Move child generations

    move_num = len(children[0].future)  # Num of moves

    for child in children:  # Iterate over children

        for move in range(move_num):  # Iterate over moves

            child.next_move(move)  # Move child

    return children  # Return children


def generations(gen_number, square, circle_num, move_num,
                start_pos, move_size, window_height, mutation_rate ):  # Run the program

    n_dists = []
    made_it = []
    generation = []

    for number in range(gen_number):  # Iterate over generations

        if number == 0:  # First generation

            circles = move_first_gen(circle_num, move_num, start_pos, move_size)  # Create/move circles
            mothers, fathers, reached_square, av_n_dist = natural_selection(circles, square, window_height)  # Select

            n_dists.append(round(av_n_dist, 2))  # Add average distance for generation
            made_it.append(reached_square)  # Add number reaching square

            children = next_generation(mothers, fathers, circles, 1, mutation_rate, start_pos)  # Create children

            move_children(children)  # Move children

            generation.append(children)  # Add generation to llist of generations

        else:  # Child generations

            cir = generation[number-1]  # Select circles
            mothers, fathers, reached_square, av_n_dist = natural_selection(cir, square, window_height)  # Select

            n_dists.append(round(av_n_dist, 2))  # Add average distance for generation
            made_it.append(reached_square)  # Add number reaching square

            children = next_generation(mothers, fathers, cir, 1, mutation_rate, start_pos)  # Create children

            move_children(children)  # Move children

            generation.append(children)  # Add generation to llist of generations

    return n_dists, made_it  # Output ave dist per generation and number of circles hitting the square


# Parameters
move_size = 50
mutation_rate = 0.05
start_pos = [400, 400]
square_center = [25, 25]
sq_side_len = 10
move_num = int(input('Number of steps: '))
circle_num = int(input('Number of circles: '))
window_height = 600
gen_number = int(input('Number of generations: '))

# Run program
square = TargetSquare(square_center, sq_side_len)

nd, mi = generations(gen_number, square, circle_num, move_num, start_pos, move_size, window_height, mutation_rate)

# Output information
print()
print(f'Number of circles that reached the square each generation: \n{mi}')
print()
print(f'Average normalised distance for each generation (Higher = Closer): \n{nd}')
