## Light up vPython
from vpython import *


# Set up the vPython scene
scene.title = "Projectile Motion"
scene.width = 900
scene.height = 500
scene.background = color.black

# Create ground
'''
the y-value of -51 moves the 'ground' down in the scene
'''
ground = box(pos=vector(0, -51, 0), size=vector(400, 0.5, 5), color=color.green)

# Create the projectile
'''
The ball.v vector provides both velocity and launch angle. Here x and y values
are equal so the math works out to a 45' launch angle. An x-value > the y-value
is a shallower angle and x-value < the y-value is a steeper angle
'''
ball = sphere(pos=vector(-100, -48, 0), radius=2, color=color.blue, make_trail=True)
ball.mass = 10
ball.v = vector(35, 35, 0) # initial velocity
g = vector(0, -9.81, 0) # gravity


# Flight information
flight_info = label(
    #pos=vector(50, -48, 0),  # Slightly above the ground level
    pos=vector(100, -48, 0),  # Slightly above the ground level
    text="Flight Time: 0 s\nDistance: 0 m",
    height=20,
    color=color.white
)


# Simulation variables
t = 0
dt = 0.01

# Simulation loop
while ball.pos.y >= -50:
    rate(100)

    Fnet = ball.mass * g
    ball.v += (Fnet / ball.mass) * dt
    ball.pos += ball.v * dt

    t += dt

    #Update flight info
    flight_info.text=f"Flight time: {t:.2f} s\nDistance: {ball.pos.x + 100:.2f} m"

