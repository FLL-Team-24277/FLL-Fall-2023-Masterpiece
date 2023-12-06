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
    ACCEL = 250
    br.robot.settings(
        straight_speed=400,
        straight_acceleration=ACCEL,
        turn_rate=150,
        turn_acceleration=360,
    )
    br.leftAttachmentMotor.run_angle(1500, 5000, wait=False)
    br.GyroDrive(320, 990)
    ACCEL = 600
    br.robot.settings(
        straight_speed=400,
        straight_acceleration=ACCEL,
        turn_rate=150,
        turn_acceleration=360,
    )
    br.rightAttachmentMotor.run_angle(1500, 250, wait=True)
    br.GyroDrive(700, 990)
    br.WaitForMillis(70)
    br.GyroDrive(-600, 200)


# If running this program directly (not from the master program), this is
# how we know it is running directly. In which case, this method will
# create a BaseRobot and run the Run(br) method above.
# In other words, keep these three lines at the bottom of your code and
# everything will be fine.
if __name__ == "__main__":
    br = BaseRobot()
    Run(br)
