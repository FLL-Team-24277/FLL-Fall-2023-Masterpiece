from base_robot import *


def Run(br: BaseRobot):
    # br.rightAttachmentMotor(500,180)
    # br.leftDriveMotor(50,180)
    # br.MoveRightAttachmentMotorSec(500, 1)
    # print("done")
    # pressed = br.hub.buttons.pressed()
    # while len(pressed) == 0:
    # pressed = br.hub.buttons.pressed()
    br.WaitForButton(Button.LEFT)
    br.GyroDrive(350, 600)
    br.GyroTurn(180)
    br.GyroDrive(400, -600)
    br.WaitForButton(Button.LEFT)
    br.GyroDrive(850, speed=977, then=Stop.BRAKE)
    br.GyroDrive(-850, speed=977, then=Stop.BRAKE)
    br.WaitForButton(Button.LEFT)
    br.GyroDrive(750, then=Stop.BRAKE)
    br.GyroTurn(90, then=Stop.BRAKE)
    br.GyroDrive(250, then=Stop.BRAKE)
    br.leftAttachmentMotor.run_time(500, 500)
    br.rightAttachmentMotor.run_time(1000, 1500)
    wait(250)
    br.GyroDrive(-200, then=Stop.BRAKE)
    br.GyroTurn(-90, then=Stop.BRAKE)
    br.robot.straight(-750, Stop.BRAKE, True)
    br.WaitForButton(Button.LEFT)
    br.GyroDrive(500)  # 500 mm
    br.GyroDrive(-500)  # 500 mm


if __name__ == "__main__":
    br = BaseRobot()
    Run(br)
