from base_robot import *

# Add good comments, such as what the mission is supposed to do,
# how to align the robot in home, any initial starting instructions,
# such as how it should be loaded with anything, arm positions, etc.


# When we run this program from the master program, we will call this
# "Run(br)" method.
def Run(br: BaseRobot):
    br.GyroDrive(25)
    br.rightAttachmentMotor.run_angle(200, -180)  # speed 200, 180 degrees
    br.GyroTurn(90)
    br.rightAttachmentMotor.run_angle(200, 180)  # speed 200, 180 degrees
    br.GyroDrive(-25)
    br.GyroTurn(-90)


# If running this program directly (not from the master program), this is
# how we know it is running directly. In which case, this method will
# create a BaseRobot and run the Run(br) method above.
# In other words, keep these three lines at the bottom of your code and
# everything will be fine.
if __name__ == "__main__":
    br = BaseRobot()
    Run(br)