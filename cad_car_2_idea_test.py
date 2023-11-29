from base_robot import *


def Run(br: BaseRobot):
    ACCEL = 350
    br.robot.settings(
        straight_speed=400,
        straight_acceleration=ACCEL,
        turn_rate=150,
        turn_acceleration=360,
    )
    br.rightAttachmentMotor.run_time(-500, 1000)
    br.robot.use_gyro(True)
    br.GyroDrive(500, 700)
    br.GyroTurn2(-38)
    br.GyroDrive(100, 700)
    br.GyroTurn(-25)
    br.GyroDrive(600, 700)
    br.GyroTurn(25)
    br.GyroDrive(-100, 700)
    br.robot.settings(600, ACCEL, 50, 360)
    br.GyroTurn(-56)
    br.GyroDrive(400, 700)
    br.robot.turn(40)
    br.robot.settings(600, ACCEL, 150, 360)
    br.GyroDrive(225, 700)
    br.rightAttachmentMotor.run_time(500, 500, wait=False)
    br.WaitForButton(Button.LEFT)
    br.GyroDrive(515, 977)  # drive 340 mm
    br.GyroDrive(-600, 977)

    # br.GyroDrive(-100, 700)
    # br.GyroTurn(-50)
    # br.rightAttachmentMotor.run_time1(speed=900, time=500, wait=False)
    # br.GyroDrive(400)


if __name__ == "__main__":
    br = BaseRobot()
    Run(br)
