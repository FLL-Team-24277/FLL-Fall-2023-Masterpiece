from base_robot import *


def GyroTurn(angle):
    angle = -angle
    angle = (-angle) + br.hub.imu.heading()
    delta = angle - br.hub.imu.heading()
    while round(delta) not in range(-1, 1):
        br.robot.turn(delta)
        delta = angle - br.hub.imu.heading()


def Run(br: BaseRobot):
    br.rightAttachmentMotor.run_time(-500, 1000)
    br.robot.use_gyro(True)
    br.GyroDrive(500, 700)
    br.GyroTurn(-38)
    br.GyroDrive(100, 700)
    br.GyroTurn(-32)
    br.GyroDrive(600, 700)
    br.GyroDrive(-100, 700)
    br.GyroTurn(-42)
    br.GyroDrive(450, 700)
    br.robot.settings(600, 500, 50, 360)
    br.robot.turn(50)
    br.robot.settings(600, 500, 150, 360)
    br.GyroDrive(200, 700)
    br.rightAttachmentMotor.run_time(500, 500, wait=False)
    br.GyroDrive(-200, 700)
    br.robot.use_gyro(True)
    GyroTurn(-50)
    br.GyroDrive(-200, 700)
    br.GyroTurn(-40)
    br.GyroDrive(750, 700)

    # br.GyroDrive(-100, 700)
    # br.GyroTurn(-50)
    # br.rightAttachmentMotor.run_time1(speed=900, time=500, wait=False)
    # br.GyroDrive(400)


if __name__ == "__main__":
    br = BaseRobot()
    Run(br)
