from turtle import Turtle, Screen
import random
import math


def create_window_and_square():

    # Set up canvas
    canvas.bgcolor("light blue")  # Colour
    canvas.setup(width=600, height=600)  # Size
    canvas.title("Genetic Algorithm: Race to square")  # Title

    # Create target square
    target_square = Turtle('square', visible=False)  # Square is a turtle
    target_square.turtlesize(0.6)  # Square size

    # Set square position
    target_square.speed(0)  # Fastest so appears at top
    target_square.penup()  # Do not draw line
    target_square.setposition(-280, 280)  # Square location
    target_square.showturtle()


def rand_direction():  # Select random coordinates/direction from list

    movements = [(10, 10), (10, -10), (-10, -10), (-10, 10)]  # List of possible directions
    move = random.choice(movements)  # Random selection from list
    return move


def make_turtle(turtle_num, move_num):  # Create all turtle instances and their genes

    ts = [Turtle('circle', visible=False) for _ in range(turtle_num)]  # Create list of turtle instances
    gs = [[rand_direction() for move in range(move_num)] for num in range(turtle_num)]  # Create list of moves/genes
    return ts, gs  # Return genes and moves/genes


def move_turtles(turtles, genes):  # Move all turtles based on their genes & record end location

    final_positions = []  # List of end locations

    for index, item in enumerate(turtles):  # Iterate over turtles

        for dire in genes[index]:  # Iterate over movements for each turtle

            item.speed(0)  # Fastest speed
            item.penup()  # No line
            item.turtlesize(0.3)  # Turtle size
            item.color('green')  # Colour
            item.showturtle()  # Make turtle visible
            item.goto(item.pos() + dire)  # Complete each movement in genes for this turtle

        final_positions.append(item.pos())  # Add final location of each turtle to lise

    return final_positions


def calc_fitness(final_positions, target_coordinates):  # Calculates fitness of each individual

    distances = [math.dist(item, target_coordinates) for item in final_positions]  # Euclidean distance turtle/target

    n_dists = [1-(item/height) for item in distances]  # Normalise dists (divide by constant & subtract from 1)

    return n_dists  # Return a list of normalised distances - these fall between 1 & 0 - higher the better


def natural_selection(fitness):  # Create a mating pool proportional to fitness

    mating_pool = []

    for index, item in enumerate(fitness):  # Index represents turtle names

        mating_pool.extend([index for i in range(int(item*float(100)))])  # Occur 1000 times normalised distance

    return mating_pool  # Return mating pool array


def random_mutation(mutation_rate):  # Output true or false based on input probability

    mut_num = 1/mutation_rate  # Range to guess from
    num = random.randint(1, mut_num)  # Number to guess
    guess = random.randint(1, mut_num)  # Guess

    if num == guess:  # If guessed output True
        return True
    else:  # Not guessed output False
        return False


def reproduction(mating_pool, genes, turtles):  # Reproduction and crossing over

    mothers = random.sample(mating_pool, len(turtles))  # Random sample from mating_pool
    fathers = random.sample(mating_pool, len(turtles))  # Random sample from mating_pool

    new_genes = []  # List of new genes for each turtle (nested list)

    for index, item in enumerate(turtles):  # Iterate over turtles

        child_genes = []  # Sublist for new_genes

        for i, m in enumerate(genes[0]):  # Iterate over each move

            if random_mutation(0.1):  # If true
                move = rand_direction()  # Move is random rather than inherited

            else:  # Mutation false then move inherited
                move = (genes[fathers[index]][i][0], genes[mothers[index]][i][1])  # Select x from father & y mother

            child_genes.append(move)   # Add move to child_genes

        new_genes.append(child_genes)  # Add genes of each child to new_genes as a sublist

    new_turtles = [Turtle('circle', visible=False) for _ in range(len(new_genes))]  # Create new turtle instances

    return new_turtles, new_genes  # Return nested list


def write_label(gen, average):

    # Pen for writing title
    pen = Turtle('square', visible=False)
    pen.speed(0)
    pen.shape("square")
    pen.color("black")
    pen.penup()
    pen.goto(250, 250)
    pen.write(f'Generation: {gen+1} \nAverage Distance for Gen {gen}: {average} ', align="right",
              font=("candara", 12, "bold"))


def final_message(message):

    pen = Turtle('square', visible=False)
    pen.speed(0)
    pen.shape("square")
    pen.color("black")
    pen.penup()
    pen.goto(0, 0)
    pen.write(f'Total distance improvement: {message}', align="right", font=("candara", 12, "bold"))


def run_circles_to_squares(circle_num, move_num, gen_num):  # Run the program

    count = 0
    create_window_and_square()  # Create first window
    turtles, genes = make_turtle(circle_num, move_num)  # Create initial turtle/genes

    initial_dist = 0  # Initiate variable - will be changed
    final_dist = 0  # Initiate variable - will be changed

    for item in range(gen_num):  # Iterate over each generation

        create_window_and_square()  # Create new window

        positions = move_turtles(turtles, genes)  # Move turtles

        fitness = calc_fitness(positions, target)  # Calculate fitness

        av_fit = sum([1-item for item in fitness])/len([1-item for item in fitness])  # Distance for text display

        mating_pool = natural_selection(fitness)  # Create mating pool

        canvas.clearscreen()  # Clear window

        write_label(count, '{0:.2f}'.format(av_fit * 600))  # Text showing gen num and dist

        turtles, genes = reproduction(mating_pool, genes, turtles)  # Produce next generation

        if count == 0:
            initial_dist = '{0:.2f}'.format(av_fit * 600)
        if count == gen_num-1:
            final_dist = '{0:.2f}'.format(av_fit * 600)

        count += 1

    final_message(round(float(initial_dist)-float(final_dist), 2))

    canvas.mainloop()  # End turtle


# Add user inputs for parameters
num_of_circles = int(input('Number of circles: '))
num_of_steps = int(input('Number of steps: '))
num_of_generations = int(input('Number of generations: '))

# Creating a window screen
canvas = Screen()  # Initiate screen
target = (-280, 280)  # Target coordinates
height = 600  # Height of screen

run_circles_to_squares(num_of_circles, num_of_steps, num_of_generations)  # Run the algorithm

