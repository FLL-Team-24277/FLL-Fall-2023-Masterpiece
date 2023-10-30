from base_robot import *

# Add good comments, such as what the mission is supposed to do,
# how to align the robot in home, any initial starting instructions,
# such as how it should be loaded with anything, arm positions, etc.

# Weird spacing is intentional. Should be auto-corrected by Black formatter after saving


# When we run this program from the master program, we will call this
# "Run(br)" method.
def Run(br: BaseRobot):
    #   Your mission code goes here, step-by-step
    # It MUST be indented just like the lines below
    br.leftAttachmentMotor.run_until_stalled(-990, Stop.COAST, 40)
    br.GyroDrive(325, 990)
    br.WaitForMillis(100)
    br.leftAttachmentMotor.run_angle(990, 90, wait=True)
    br.rightAttachmentMotor.run_angle(990, -120)
    br.WaitForMillis(100)
    br.GyroDrive(-330, 900)

    br.WaitForButton(Button.LEFT)
    br.GyroDrive(-100, 990)
    br.GyroTurn(-55)
    br.GyroDrive(-360, 990)
    br.WaitForMillis(300)
    br.GyroDrive(800, 990)


# If running this program directly (not from the master program), this is
# how we know it is running directly. In which case, this method will
# create a BaseRobot and run the Run(br) method above.
# In other words, keep these three lines at the bottom of your code and
# everything will be fine.
if __name__ == "__main__":
    br = BaseRobot()
    Run(br)
