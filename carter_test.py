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
    br.GyroDrive(50)  # drive 50 mm
    br.GyroDrive(-240)  # drive -240 mm
    br.GyroTurn(-37)  # turn -37 degrees
    br.GyroDrive(440)  # drive 440 mm
    br.GyroTurn(35)  # turn 435 degrees
    br.GyroDrive(200)  # drive 200 mm
    br.GyroTurn(18)  # turn 18 degrees
    br.rightAttachmentMotor.run_angle(1000, 300)
    br.GyroDrive(-250)  # drive -250 mm
    br.GyroTurn(-15)  # turn -15 degrees
    br.GyroDrive(50)  # drive 50 mm
    # br.GyroTurn(80)  # turn 80 degrees
    # br.GyroDrive()
    br.leftAttachmentMotor.run_angle(1000, 300)
    br.GyroDrive(-50)  # drive -50 mm


# If running this program directly (not from the master program), this is
# how we know it is running directly. In which case, this method will
# create a BaseRobot and run the Run(br) method above.
# In other words, keep these three lines at the bottom of your code and
# everything will be fine.
if __name__ == "__main__":
    br = BaseRobot()
    Run(br)
