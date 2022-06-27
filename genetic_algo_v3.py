import random


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

        possible_moves = [move_size, -move_size]  # Positive and negative moves
        new_position = [self.x + random.choice(possible_moves), self.y + random.choice(possible_moves)]
        self.move_history.append(self.xy)  # Keep record of old positions
        self.xy = new_position  # Update xy with new positions
        self.x = new_position[0]  # Update x with new position
        self.y = new_position[1]  # Update y with new position


# Children - all individuals after first generation
class Child(Individual):

    def __init__(self, xy, diameter, generation):
        Individual.__init__(self, xy, diameter)
        self.generation = generation
        self.future = []

    def crossing_over(self, father, mother):

        future_moves = []

        for item in range(len(father.move_history)):

            if item % 2 == 0:
                future_moves.append(father.move_history[item])
            else:
                future_moves.append(mother.move_history[item])

        self.future = future_moves

    def next_move(self, prev_moves):

        new_position = self.future[prev_moves]
        self.xy = new_position  # Update xy with new positions
        self.x = new_position[0]  # Update x with new position
        self.y = new_position[1]  # Update y with new position


# Target box
class TargetSquare:

    def __init__(self, center_xy, side_len):

        self.center_xy = center_xy
        self.side_len = side_len
        self.x_range = list(range(center_xy[0] - (side_len/2), center_xy[0] + (side_len/2)))
        self.y_range = list(range(center_xy[1] - (side_len/2), center_xy[1] + (side_len/2)))


def move_first_gen(num_of_circles, num_of_moves, start_pos):

    circle_lst = []

    for index in range(num_of_circles):

        circle = Individual(start_pos, 5)

        for move in range(num_of_moves):

            circle.move(10)

        circle_lst.append(circle)

    return circle_lst


def move_child_gen():

    pass


circles = move_first_gen(10, 10, [10, 10])

for item in circles:

    print(item.move_history)





