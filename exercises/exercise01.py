import sys
sys.path.append('../mobilerobot')

# import necessary classes
from world import SimpleWorld
from vehicle import Vehicle

# initialize three vehicles
v1 = Vehicle(radius=3)
v1.setState(x=50, y=70, theta=90)

v2 = Vehicle(radius=3)
v2.setState(x=20, y=20, theta=180)

v3 = Vehicle(radius=3)
v3.setState(x=20, y=70, theta=0)


# The functions below will be called in every step of the animation. The first argument is used
# to access the rotate and move command of the robot
def move1(vehicle):
    # The first robot rotates ro the left
    vehicle.rotateLeft(angle=0.2)
    
def move2(vehicle):
    # ------------- Modify this part --------------------------------------
    # Modify this function, such that the second robot rotates the whole time to the right
    pass
    # ---------------------------------------------------------------------- 


def move3(vehicle):
    # ------------- Modify this part --------------------------------------
    # Modify this function, such that the third robot moves forwards
    pass
    # ---------------------------------------------------------------------- 


# pass move function to vehicles
v1.controller = move1
v2.controller = move2
v3.controller = move3

# initialize world and animation
sworld = SimpleWorld(x=100, y=100, vehicles=[v1, v2, v3])
sworld.initAnimation()

# show plot
sworld.showScene()
