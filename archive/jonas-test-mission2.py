from base_robot import *


def Run(br: BaseRobot):
    br.DriveAndSteer(500, 20, 5000)


if __name__ == "__main__":
    br = BaseRobot()
    Run(br)
