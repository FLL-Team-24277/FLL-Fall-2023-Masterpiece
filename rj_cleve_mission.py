from base_robot import *


def Run(br: BaseRobot):
    #   Your mission code goes here, step-by-step
    # It MUST be indented just like the lines below
    # for our testing
    # br.WaitForButton(Button.LEFT)
    #  for master program
    br.GyroDrive(295.5, 800)
    br.GyroTurn(90)
    br.GyroDrive(725 - 180, 800)
    br.GyroTurn(40)
    br.GyroDrive(130, 800)
    br.rightAttachmentMotor.run_angle(1000, 360)
    br.rightAttachmentMotor.run_angle(1000, -360)
    br.GyroDrive(-100, 800)
    br.GyroTurn(-45, speed=100)
    br.GyroDrive(40)
    br.GyroTurn(-45, speed=100)

    # drive farther
    br.GyroDriveForMillis(300, 800)
    # br.GyroDrive(-1, 800)
    br.leftAttachmentMotor.run_angle(977, -2235)  # -2325

    # br.GyroTurn(-30)

    # br.Curve(radius=420, angle=-80)
    # br.GyroTurn(-60)
    # # Drive farther after testing
    # br.GyroDrive(150, 800)
    # br.GyroTurn(60)
    # # br.GyroDrive(150, 800)
    # br.GyroDrive(-150, 800)


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
