from base_robot import *

# Add good comments, such as what the mission is supposed to do,
# how to align the robot in home, any initial starting instructions,
# such as how it should be loaded with anything, arm positions, etc.

# Weird spacing is intentional. Should be auto-corrected by Black formatter after saving


# When we run this program from the master program, we will call this
# "Run(br)" method.
def Run(br: BaseRobot):
    #   Your mission code goes here, step-by-step
    # It MUST be indented just like the lines belowL

    br.GyroDrive(600, 300)
    br.GyroTurn(40)
    br.GyroDrive(200,300)
    br.GyroTurn(-100)


    br.GyroDrive(80,550)
    br.leftAttachmentMotor.run_angle (300,-450)  # speed 500, 180 degrees
    br.WaitForMillis(3000)
    br.GyroDrive(-60,550)
    br.WaitForMillis(2000)
    br.leftAttachmentMotor.run_angle(300,450)
    br.GyroDrive(80,550)
    br.leftAttachmentMotor.run_angle (300,-450)  # speed 500, 180 degrees
    br.WaitForMillis(3000)
    br.GyroDrive(-80,550)
    br.WaitForMillis(2000)
    br.leftAttachmentMotor.run_angle(300,450)
    br.GyroTurn(-95)
    br.GyroDrive(200,300)
    br.GyroTurn(-40)
    br.GyroDrive(500, 300)

# If running this program directly (not from the master program), this is
# how we know it is running directly. In which case, this method will
# create a BaseRobot and run the Run(br) method above.
# In other words, keep these three lines at the bottom of your code and
# everything will be fine.
if __name__ == "__main__":
    br = BaseRobot()
    Run(br)
