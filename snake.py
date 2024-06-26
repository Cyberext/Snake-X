import pyglet
from pyglet.gl import *
import random

# Window configuration
window = pyglet.window.Window(width=800, height=600, caption="3D Snake Game")
window.set_location(100, 100)

# Game configuration
snake_positions = [(0, 0, 0)]
snake_direction = (1, 0, 0)
snake_length = 5
current_level = 1
selected_snake = 'snake_texture.png'  # Default snake texture

# Load textures
textures = {
    'snake': pyglet.image.load('textures/snake_texture.png').get_texture(),
    'jungle': pyglet.image.load('textures/jungle_texture.png').get_texture(),
    'food': pyglet.image.load('textures/food_texture.png').get_texture(),
    'custom_snake_1': pyglet.image.load('textures/snake_texture_1.png').get_texture(),
    'custom_snake_2': pyglet.image.load('textures/snake_texture_2.png').get_texture()
}

# Food configuration
food_position = (random.randint(-10, 10), random.randint(-10, 10), random.randint(-10, 10))

def update(dt):
    global snake_positions, food_position, snake_length
    
    # Update snake position
    new_head = tuple(map(sum, zip(snake_positions[0], snake_direction)))
    snake_positions = [new_head] + snake_positions[:-1]
    
    # Check for food collision
    if new_head == food_position:
        snake_length += 1
        snake_positions.append(snake_positions[-1])
        food_position = (random.randint(-10, 10), random.randint(-10, 10), random.randint(-10, 10))
    
    # Check for level completion
    if snake_length > 10 * current_level:  # Arbitrary level progression condition
        next_level()

def next_level():
    global current_level, snake_length, snake_positions
    current_level += 1
    snake_length = 5
    snake_positions = [(0, 0, 0)]
    # Load next level's configuration or increase difficulty
    print(f"Level {current_level}")

@window.event
def on_draw():
    window.clear()
    glLoadIdentity()
    gluLookAt(0, 0, 20, 0, 0, 0, 0, 1, 0)

    # Draw jungle background
    draw_cube((0, 0, -5), textures['jungle'])

    # Draw snake
    for pos in snake_positions:
        draw_cube(pos, textures[selected_snake])

    # Draw food
    draw_cube(food_position, textures['food'])

def draw_cube(position, texture):
    x, y, z = position
    glPushMatrix()
    glTranslatef(x, y, z)
    glBindTexture(GL_TEXTURE_2D, texture.id)
    glBegin(GL_QUADS)
    # Define the vertices and texture coordinates for each face of the cube
    # Front Face
    glTexCoord2f(0.0, 0.0)
    glVertex3f(-0.5, -0.5, 0.5)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(0.5, -0.5, 0.5)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(0.5, 0.5, 0.5)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(-0.5, 0.5, 0.5)
    # Add other faces similarly
    glEnd()
    glPopMatrix()

@window.event
def on_key_press(symbol, modifiers):
    global snake_direction, selected_snake
    if symbol == pyglet.window.key.UP:
        snake_direction = (0, 1, 0)
    elif symbol == pyglet.window.key.DOWN:
        snake_direction = (0, -1, 0)
    elif symbol == pyglet.window.key.LEFT:
        snake_direction = (-1, 0, 0)
    elif symbol == pyglet.window.key.RIGHT:
        snake_direction = (1, 0, 0)
    elif symbol == pyglet.window.key.W:
        snake_direction = (0, 0, 1)
    elif symbol == pyglet.window.key.S:
        snake_direction = (0, 0, -1)
    elif symbol == pyglet.window.key._1:
        selected_snake = 'custom_snake_1'
    elif symbol == pyglet.window.key._2:
        selected_snake = 'custom_snake_2'

pyglet.clock.schedule_interval(update, 1/10.0)
pyglet.app.run()
