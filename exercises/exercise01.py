import sys
sys.path.append('mobilerobot')

# import necessary classes
from world import RobotWorld
from robot import Robot

# initialize three robots
r1 = Robot()
r1.setState(x=50, y=70, theta=90)

r2 = Robot()
r2.setState(x=20, y=20, theta=180)

r3 = Robot()
r3.setState(x=20, y=70, theta=0)


# The functions below will be called in every step of the animation. The first argument is used
# to access the rotate and move command of the robot
def move1(robot):
    # The first robot rotates ro the left
    robot.rotateLeft(angle=0.2)
    
def move2(robot):
    # ------------- Modify this part --------------------------------------
    # Modify this function, such that the second robot rotates the whole time to the right
    pass
    # ---------------------------------------------------------------------- 


def move3(robot):
    # ------------- Modify this part --------------------------------------
    # Modify this function, such that the third robot moves forwards
    pass
    # ---------------------------------------------------------------------- 


# pass move function to robots
r1.controller = move1
r2.controller = move2
r3.controller = move3

# initialize world and animation
world = RobotWorld(x=100, y=100, robots=[r1, r2, r3])
world.initAnimation()

# show plot
world.showScene()
