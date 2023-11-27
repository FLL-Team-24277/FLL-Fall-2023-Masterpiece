from base_robot import *


def Run(br: BaseRobot):
    br.rightAttachmentMotor.run_time(
        speed=-1500, time=1000, wait=False, then=Stop.HOLD
    )
    br.GyroDrive(500, 700)
    br.GyroTurn(-30)
    br.GyroDrive(100, 700)
    br.GyroTurn(-32)
    br.GyroDrive(600, 700)
    # br.GyroTurn(-30)
    # br.GyroDrive(300, 700)

    # br.GyroDrive(-100, 700)
    # br.GyroTurn(-50)
    # br.rightAttachmentMotor.run_time1(speed=900, time=500, wait=False)
    # br.GyroDrive(400)


if __name__ == "__main__":
    br = BaseRobot()
    Run(br)
