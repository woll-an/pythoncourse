import sys
sys.path.append('../mobilerobot')

# import necessary classes
from world import LightWorld
from vehicle import Vehicle
from light import Light

# initialize two vehicles
v = Vehicle(radius=3)
v.setState(x=50, y=70, theta=90)

# initialize a light source
l = Light(x=20, y=30)

# Modify the move function, such that the vehicle moves to the goal (the light source) and stops there
# The move function has now three arguments:
# - the vehicle itself (and therefore access to its move and rotate commands)
# - the measurement of two sensors, which are located to the left and to the right of the robot
# If the robot's right sensor faces the light source, its measurement is higher than the measurement
# of the left sensor. If the robot is at the position of the light source, both sensors will show 
# a measurement of 0.5
# Step (1): implement a function using only the rotate commands of the robot, such that the
# robot will point in the direction of the light source.
# Step (2): move the robot forward based on the sum of the measurement of the sensors. You know
# you reached the goal if the sum is 1.0 
def move(vehicle, rightMeasurement, leftMeasurement):
    # ------------- Modify this part --------------------------------------
    pass
    # ---------------------------------------------------------------------- 
    

# pass move function to vehicles
v.controller = move

# initialize world and animation
sworld = LightWorld(x=100, y=100, vehicles=[v], light=l)
sworld.initAnimation()

# show plot
sworld.showScene()
