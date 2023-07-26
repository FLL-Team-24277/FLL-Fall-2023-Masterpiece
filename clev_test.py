from cleveland_base_robot import *

def Run(br: BaseRobot):

    # br.GyroTurn(-60)
    # br.GyroDrive(-150,50)
    # br.GyroTurn(180)
    # br.GyroDrive(150,50)
    # br.rightAttachmentMotor(500,180)
    # br.leftDriveMotor(50,180)
    # br.MoveRightAttachmentMotorSec(500, 1)
    # print("done")
    # br.rightAttachmentMotor.run_angle(500, 180)
    br.leftAttachmentMotor.run_angle(500, 1000)
    br.WaitForMillis(1000)
    br.leftAttachmentMotor.run_time(500, 1000)




if __name__ == '__main__':
    br = BaseRobot()
    Run(br)
