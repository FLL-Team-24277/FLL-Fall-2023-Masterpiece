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
    # br.leftAttachmentMotor.run_until_stalled(-990, Stop.COAST, 40)

    br.GyroDrive(600, 990)
    br.leftAttachmentMotor.run_time(-500, 1000)
    br.WaitForMillis(300)
    br.GyroDrive(-750, 400)

    br.WaitForButton(Button.LEFT)

    br.leftAttachmentMotor.run_until_stalled(-990, duty_limit=75)
    br.rightAttachmentMotor.run_until_stalled(990, duty_limit=35)
    br.GyroDrive(400, 990)
    br.WaitForMillis(100)
    br.leftAttachmentMotor.run_angle(990, 90, wait=True)
    br.rightAttachmentMotor.run_angle(990, -120)
    br.WaitForMillis(100)
    br.robot.use_gyro(False)
    br.robot.drive(speed=-977, turn_rate=0)
    br.WaitForMillis(1000)
    br.robot.drive(speed=0, turn_rate=0)
    br.robot.use_gyro(True)
    # br.GyroDrive(-400, 900)

    # br.GyroDrive(-80, 990)
    # br.GyroTurn(-60)
    # br.GyroDrive(-370, 990)
    # br.WaitForMillis(300)
    # br.robot.curve(radius=750, angle=-60)
    # # br.GyroDrive(800, 990)


# If running this program directly (not from the master program), this is
# how we know it is running directly. In which case, this method will
# create a BaseRobot and run the Run(br) method above.
# In other words, keep these three lines at the bottom of your code and
# everything will be fine.
if __name__ == "__main__":
    br = BaseRobot()
    Run(br)
