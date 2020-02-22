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
o1 = Obstacle(20, 40, 60, 10)
o2 = Obstacle(20, 40, 10, 30)
o3 = Obstacle(70, 40, 10, 30)

# Modify the move function, such that the robot moves to the goal (the light source) and stops there.
# This exercise is identical to exercise03, but the obstacle is now more complex
def move(robot, rightMeasurement, leftMeasurement):
    # ------------- Modify this part --------------------------------------
    free = robot.moveForward(0.01)
    # ---------------------------------------------------------------------- 
    

# pass move function to robots
r.controller = move

# initialize world and animation
world = LightObstacleWorld(x=100, y=100, robots=[r], light=l, obstacles=[o1, o2, o3])
world.initAnimation()

# show plot
world.showScene()
