from base_robot import *


def Run(br: BaseRobot):
    # br.GyroTurn(180)
    # br.GyroDrive(150,50)
    # br.rightAttachmentMotor(500,180)
    # br.leftDriveMotor(50,180)
    # br.MoveRightAttachmentMotorSec(500, 1)
    # print("done")
    br.GyroDrive(500, 100)
    br.WaitForMillis(1000)
    br.GyroDrive(500, then=Stop.BRAKE)
    # br.WaitForMillis()
    # br.leftAttachmentMotor.run_time(500, 1000)
    # br.GyroDrive(1000000,5000)


if __name__ == "__main__":
    br = BaseRobot()
    Run(br)
