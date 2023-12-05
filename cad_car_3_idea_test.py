from base_robot import *


def Run(br: BaseRobot):
    # ACCEL = 350
    # br.robot.settings(
    # straight_speed=400,
    # straight_acceleration=ACCEL,
    # turn_rate=150,
    # turn_acceleration=360,
    # )
    br.rightAttachmentMotor.run_time(-500, 1000, wait=False)
    br.GyroDrive(280, 977, then=Stop.NONE)
    br.Curve(radius=370, angle=-70, speed=977, then=Stop.NONE)
    br.GyroDrive(375, 750, then=Stop.NONE)
    br.GyroTurn(35)
    br.GyroDrive(-100, 700, then=Stop.NONE)
    br.GyroTurn(-45)
    br.GyroDrive(400, 977, then=Stop.NONE)
    br.GyroTurn(45)
    br.GyroDrive(150)
    br.rightAttachmentMotor.run_time(500, 1000)
    br.GyroDrive(-400, 977, then=Stop.NONE)
    # br.WaitForButton(Button.LEFT, then=Stop.NONE)
    # br.GyroDrive(515, 977, then=Stop.NONE)  # drive 340 mm
    # br.GyroDrive(-600, 977, then=Stop.NONE)


if __name__ == "__main__":
    br = BaseRobot()
    Run(br)
