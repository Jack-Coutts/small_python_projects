import pyglet
from pyglet import shapes
from pyglet.window import key
import random

window = pyglet.window.Window(600, 600)  # Initiate window
batch = pyglet.graphics.Batch()  # Create batch

circle = shapes.Circle(299, 299, 3, color=(50, 225, 30), batch=batch)
square = shapes.Rectangle(295, 580, 10, 10, color=(55, 55, 255), batch=batch)

score_label = pyglet.text.Label(text="Score: 0", x=10, y=460, batch=batch)


cs = [shapes.Circle(299, 299, 3, color=(50, 225, 30), batch=b) for i in range(10)]

@window.event
def on_draw():
    window.clear()
    batch.draw()

@window.event
def update(dt):

    window.clear()

    global circle

    slow = 0.01

    movements = [(10, 10), (10, -10), (-10, -10), (-10, 10)]
    coords = [random.choice(movements) for item in range(10)]

    for item in coords:

        circle.x += item[0]
        circle.y += item[1]



pyglet.clock.schedule_interval(update, 0.1)

pyglet.app.run()