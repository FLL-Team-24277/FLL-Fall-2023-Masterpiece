from base_robot import *


def Run(br: BaseRobot):
    br.GyroDrive(430, 977, then=Stop.NONE)
    br.Curve(radius=400, angle=-50, speed=977)
    br.leftAttachmentMotor.run_time(-1000, 3300)
    br.GyroDrive(-110, 750)
    # br.Curve(radius=200, angle=70, speed=977)
    br.GyroTurn(90)
    br.GyroDrive(40)


if __name__ == "__main__":
    br = BaseRobot()
    Run(br)
