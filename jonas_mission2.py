from base_robot import *


def Run(br: BaseRobot):
    br.rightAttachmentMotor.run_until_stalled(speed=-400, duty_limit=50)
    br.rightAttachmentMotor.run_time(-500, 200)
    br.GyroDrive(800, speed=977, then=Stop.BRAKE)
    br.leftAttachmentMotor.run_time(-500, 1500, wait=False)
    br.rightAttachmentMotor.run_time(1000, 1500)
    br.GyroDrive(-200, then=Stop.BRAKE)
    br.GyroTurn(-30)
    br.GyroDrive(-600, then=Stop.BRAKE)


if __name__ == "__main__":
    br = BaseRobot()
    Run(br)
