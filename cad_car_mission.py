from base_robot import *

# Add good comments, such as what the mission is supposed to do,
# how to align the robot in home, any initial starting instructions,
# such as how it should be loaded with anything, arm positions, etc.


# When we run this program from the master program, we will call this
# "Run(br)" method.
def Run(br: BaseRobot):
    br.GyroDrive(420)  # drive 420 mm
    br.GyroTurn(-50)  # turn -50 degrees
    br.GyroDrive(700)  # drive 700 mm
    br.GyroTurn(20)  # turn 20 degrees

    # enter the museum
    br.GyroDrive(65)  # drive 65 mm
    br.GyroDrive(-255)  # drive -255 mm

    # drive to skateboard
    br.GyroTurn(-37)  # turn -37 degrees
    br.GyroDrive(490)  # drive 490 mm
    br.GyroTurn(40)  # turn 40 degrees

    # enter the skateboard
    br.GyroDrive(170)  # drive 170 mm
    br.rightAttachmentMotor.run_angle(1000, 300)
    br.GyroDrive(-230)  # drive -230 mm
    br.GyroTurn(55)  # turn 55 degrees
    br.Curve(radius=-360, angle=-60)
    br.GyroDrive(-600, -977)

    # base to popcorn
    br.WaitForButton(Button.LEFT)
    br.GyroDrive(340)  # drive 340 mm
    br.GyroTurn(10)
    br.GyroDrive(55)
    br.leftAttachmentMotor.run_angle(-1000, 300)
    br.GyroDrive(-200)  # drive -200 mm


# If running this program directly (not from the master program), this is
# how we know it is running directly. In which case, this method will
# create a BaseRobot and run the Run(br) method above.
# In other words, keep these three lines at the bottom of your code and
# everything will be fine.
if __name__ == "__main__":
    br = BaseRobot()
    Run(br)
