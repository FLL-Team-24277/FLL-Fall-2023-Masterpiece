from base_robot import *

# Add good comments, such as what the mission is supposed to do,
# how to align the robot in home, any initial starting instructions,
# such as how it should be loaded with anything, arm positions, etc.


# When we run this program from the master program, we will call this
# "Run(br)" method.
def Run(br: BaseRobot):
    br.GyroDrive(120, 977)  # drive 60 mm
    br.GyroTurn(-17)  # turn -12 degrees
    br.GyroDrive(425, 977)  # drive 420 mm
    br.GyroTurn(-49.5)  # turn -50 degrees
    br.GyroDrive(700, 977)  # drive 700 mm

    # enter the museum
    br.GyroTurn(20)  # turn 15 degrees
    br.GyroDrive(68, 977)  # drive 65 mm
    br.GyroDrive(-255, 977)  # drive -255 mm

    # drive to skateboard
    br.GyroTurn(-37)  # turn -37 degrees
    br.GyroDrive(600, 977)  # drive 490 mm
    br.GyroTurn(30)  # turn 60 degrees

    # enter base from skateboard
    br.GyroDrive(130, 977)  # drive 170 mm
    br.rightAttachmentMotor.run_time(977, 800)
    br.GyroDrive(-250, 977)  # drive -230 mm
    br.GyroTurn(55)  # turn 55 degrees
    br.Curve(radius=-330, angle=-60, speed=800)
    br.GyroDrive(-800, -977)

    # base to popcorn
    br.WaitForButton(Button.LEFT)
    br.GyroDrive(290, 977)  # drive 340 mm
    # br.GyroTurn(23)
    br.GyroDrive(85, 977)
    br.GyroDriveForMillis(1000, -990)


# If running this program directly (not from the master program), this is
# how we know it is running directly. In which case, this method will
# create a BaseRobot and run the Run(br) method above.
# In other words, keep these three lines at the bottom of your code and
# everything will be fine.
if __name__ == "__main__":
    br = BaseRobot()
    Run(br)
