from base_robot import *

# Add good comments, such as what the mission is supposed to do,
# how to align the robot in home, any initial starting instructions,
# such as how it should be loaded with anything, arm positions, etc.

# Weird spacing is intentional. Should be auto-corrected by Black formatter after saving


# When we run this program from the master program, we will call this
# "Run(br)" method.

# For the new attachment that should grab Izzy and do the printer


def Run(br: BaseRobot):
    br.GyroDrive(600, 990)
    br.leftAttachmentMotor.run_time(-500, 1000)
    br.WaitForMillis(300)
    br.GyroDrive(-750, 400)


# If running this program directly (not from the master program), this is
# how we know it is running directly. In which case, this method will
# create a BaseRobot and run the Run(br) method above.
# In other words, keep these three lines at the bottom of your code and
# everything will be fine.
if __name__ == "__main__":
    br = BaseRobot()
    Run(br)
