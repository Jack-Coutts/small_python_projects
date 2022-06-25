import pyglet
from pyglet import shapes

window = pyglet.window.Window(600, 600)  # Initiate window
batch = pyglet.graphics.Batch()  # Create batch

circle = shapes.Circle(299, 299, 3, color=(50, 225, 30), batch=batch)
square = shapes.Rectangle(295, 580, 10, 10, color=(55, 55, 255), batch=batch)


@window.event
def on_draw():
    window.clear()
    batch.draw()

pyglet.app.run()