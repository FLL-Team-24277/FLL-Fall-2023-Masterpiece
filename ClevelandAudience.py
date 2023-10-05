from base_robot import *


def Run(br: BaseRobot):
    #   Your mission code goes here, step-by-step
    # It MUST be indented just like the lines below

    br.GyroDrive(750)
    br.GyroTurn(35)
    br.GyroDrive(100)
    br.GyroDrive(-100)
    br.GyroTurn(-90)
    br.GyroDrive(25)
    br.GyroDrive(-55)
    br.GyroTurn(-45)
    br.GyroDrive(150)


# If running this program directly (not from the master program), this is
# how we know it is running directly. In which case, this method will
# create a BaseRobot and run the Run(br) method above.
# In other words, keep these three lines at the bottom of your code and
# everything will be fine.
if __name__ == "__main__":
    br = BaseRobot()
    Run(br)