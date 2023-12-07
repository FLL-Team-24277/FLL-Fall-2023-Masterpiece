from base_robot import *


def Run(br: BaseRobot):
    # ACCEL = 350
    # br.robot.settings(
    # straight_speed=400,
    # straight_acceleration=ACCEL,
    # turn_rate=150,
    # turn_acceleration=360,
    # )
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
    br.GyroTurn(-45)
    br.GyroDrive(100, speed=977, then=Stop.NONE)
    br.rightAttachmentMotor.run_time(500, 1000, wait=False)
    br.Curve(radius=750, angle=20, speed=977, then=Stop.NONE)
    br.GyroDrive(100, speed=977, then=Stop.HOLD)
    br.GyroDrive(-300, 700)
    # br.GyroDrive(-395, 977)
    # br.GyroTurn(-45)
    # br.rightAttachmentMotor.run_time(500, 1000, wait=False)
    # br.Curve(radius=400, angle=45, speed=977, then=Stop.NONE)

    # br.GyroDrive(225)
    # br.GyroDrive(-225, 977)
    # br.WaitForButton(Button.LEFT)
    # br.GyroDrive(400, 977, then=Stop.NONE)  # drive 340 mm
    # br.GyroDrive(-500, 977, then=Stop.NONE)


if __name__ == "__main__":
    br = BaseRobot()
    Run(br)
