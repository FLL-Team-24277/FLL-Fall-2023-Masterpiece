from base_robot import *


def Run(br: BaseRobot):
    # Reset Gyro
    br.robot.reset()
    br.rightAttachmentMotor.run_time(-500, 1000, wait=False)
    # br.GyroDrive(1000, 500)
    br.GyroDrive(280, 977, then=Stop.NONE)
    br.Curve(radius=370, angle=-70, speed=977, then=Stop.NONE)
    # br.robot.reset()
    br.GyroDrive(200, speed=977, then=Stop.NONE)
    br.Curve(radius=200, angle=45, speed=977, then=Stop.HOLD)
    br.GyroDrive(-100, 750)
    # # br.robot.use_gyro(True)
    br.GyroTurn(-50)
    br.GyroDrive(100, speed=977, then=Stop.NONE)
    br.rightAttachmentMotor.run_time(500, 1000, wait=False)
    br.Curve(radius=750, angle=38, speed=977)
    br.GyroDrive(distance=20)
    br.GyroDrive(distance=-200)
    # br.GyroDrive(100, speed=977, then=Stop.HOLD)
    # br.GyroDrive(-300, 700)
    # br.GyroDrive(-395, 977)
    # br.GyroTurn(-45)
    # br.rightAttachmentMotor.run_time(500, 1000, wait=False)
    # br.Curve(radius=400, angle=45, speed=977, then=Stop.NONE)

    # br.GyroDrive(225)
    # br.GyroDrive(-225, 977)
    br.WaitForButton(Button.LEFT)
    br.GyroDrive(400, 977, then=Stop.NONE)  # drive 340 mm
    br.GyroDrive(-400, 977, then=Stop.HOLD)


if __name__ == "__main__":
    br = BaseRobot()
    Run(br)
