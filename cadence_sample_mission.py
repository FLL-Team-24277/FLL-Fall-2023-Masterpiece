from base_robot import *

# Add good comments, such as what the mission is supposed to do,
# how to align the robot in home, any initial starting instructions,
# such as how it should be loaded with anything, arm positions, etc.


# When we run this program from the master program, we will call this
# "Run(br)" method.
def Run(br: BaseRobot):
    br.GyroDrive(450)  # drive 450 mm
    br.GyroTurn(-35)  # turn -35 degrees
    br.GyroDrive(600)  # drive 600 mm
    # br.GyroTurn(40)  # turn 40 degrees
    # br.GyroDrive()
    # br.GyroDrive()
    # br.GyroTurn(-90)  # turn -90 degrees
    # br.GyroDrive(200)  # drive 200 mm
    # br.GyroTurn(-70)  # turn -70 degrees
    # br.GyroDrive(30)  # drive 30 mm
    # # br.GyroTurn(-345)  # turn -345 degrees
    # br.GyroTurn(100)  # turn 100 degrees
    # br.


# If running this program directly (not from the master program), this is
# how we know it is running directly. In which case, this method will
# create a BaseRobot and run the Run(br) method above.
# In other words, keep these three lines at the bottom of your code and
# everything will be fine.
if __name__ == "__main__":
    br = BaseRobot()
    Run(br)
