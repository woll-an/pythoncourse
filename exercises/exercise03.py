import sys
sys.path.append('mobilerobot')

# import necessary classes
from world import LightObstacleWorld
from robot import Robot
from light import Light
from obstacle import Obstacle

# initialize two robots
r = Robot(radius=3)
r.setState(x=50, y=80, theta=180)

# initialize a light source
l = Light(x=50, y=20)

# initiallize the obstacle
o = Obstacle(20, 40, 60, 20)

# Modify the move function, such that the robot moves to the goal (the light source) and stops there.
# The robot will stop, when it hits the obstacle. The moveForward command of the robot will return
# False if it cannot move and True otherwise. Use this information to circumnavigate the obstacle.
# Step (1): use the code from Exercise01 to navigate in the direction of the light.
# Step (2): define a behavior if the robot cannot move forward, which is activated when
# moveForward returns False
def move(robot, rightMeasurement, leftMeasurement):
    # ------------- Modify this part --------------------------------------
    free = robot.moveForward(0.01)
    # ---------------------------------------------------------------------- 
    

# pass move function to robots
r.controller = move

# initialize world and animation
world = LightObstacleWorld(x=100, y=100, robots=[r], light=l, obstacles=[o])
world.initAnimation()

# show plot
world.showScene()
