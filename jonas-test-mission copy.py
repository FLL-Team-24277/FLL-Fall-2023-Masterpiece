from base_robot import *


def Run(br: BaseRobot):
    br.Curve(2000, 15)


if __name__ == "__main__":
    br = BaseRobot()
    Run(br)
