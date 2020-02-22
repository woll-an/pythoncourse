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

# Modify the move function, such that the robot moves to the goal (the light source) and stops there
# The 
def move(robot, rightMeasurement, leftMeasurement):
    # ------------- Modify this part --------------------------------------
    pass
    # ---------------------------------------------------------------------- 
    

# pass move function to robots
r.controller = move

# initialize world and animation
sworld = LightObstacleWorld(x=100, y=100, robots=[r], light=l, obstacles=[o])
sworld.initAnimation()

# show plot
sworld.showScene()
