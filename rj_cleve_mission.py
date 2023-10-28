from base_robot import *


def Run(br: BaseRobot):
    #   Your mission code goes here, step-by-step
    # It MUST be indented just like the lines below
    # for our testing
    # br.WaitForButton(Button.LEFT)
    #  for master program
    br.GyroDrive(295.5, 800)
    br.GyroTurn(92)
    br.GyroDrive(725 - 180, 800)
    br.GyroTurn(35)
    br.GyroDrive(120, 800)
    br.GyroDrive(-110, 800)
    br.GyroTurn(-85)
    # drive farther
    br.GyroDriveForMillis(500, 800)
    br.leftAttachmentMotor.run_angle(977, -2400)
    br.GyroDrive(-68, 800)
    br.GyroTurn(-30)

    br.Curve(radius=420, angle=-80)
    # br.GyroTurn(50)
    # br.GyroDrive(100, 800)
    # br.GyroTurn(20)
    # br.GyroDrive(-100, 800)
    # # br.GyroDrive(125)
    # br.GyroDrive(-125)


# Design Three
# br.GyroTurn(-50)
# br.GyroDrive(200)
# br.GyroTurn(-35)
# br.GyroDrive(400)
# br.GyroTurn(-105)
# br.GyroDrive(200)
# br.GyroTurn(30)

# br.GyroDrive(50)
# br.GyroTurn(27)
# br.GyroDrive(75)
# br.GyroDrive(-75)
# br.GyroTurn(-27)
# br.GyroDrive(-50)
# br.GyroTurn(-40)
# # br.GyroDrive(500)

# design two
# turn 45 at hot dog
# br.GyroTurn(-75)
# br.GyroDrive(350)
# br.GyroTurn(-90)
# # br.GyroDrive(50)
# br.GyroTurn(115)
# br.GyroDrive(50)
# br.GyroDrive(-50)
# br.GyroTurn(-90)
# br.GyroDrive(500)

# design one
# br.GyroTurn(-78)
# br.GyroDrive(325)
# br.GyroTurn(-19)
# br.GyroDrive(50)
# br.GyroTurn(30)


# If running this program directly (not from the master program), this is
# how we know it is running directly. In which case, this method will
# create a BaseRobot and run the Run(br) method above.
# In other words, keep these three lines at the bottom of your code and
# everything will be fine.
if __name__ == "__main__":
    br = BaseRobot()
    Run(br)
