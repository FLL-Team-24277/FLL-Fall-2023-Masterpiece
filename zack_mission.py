from base_robot import *


def Run(br: BaseRobot):
    # Positive numbers lower the arm; negative raises
    # Positive makes the robot go forward/ Negative makes the robot go backward
    # 3D Cinema

    br.GyroDrive(325, 950)
    br.leftAttachmentMotor.run_until_stalled(700)
    br.GyroDrive(-225, 950)

    # Sound Mixer

    while True:
        pressed = br.hub.buttons.pressed()
        if Button.LEFT in pressed:
            pushes = 1
            break
        if Button.RIGHT in pressed:
            pushes = 2
            break
        wait(50)

    br.GyroDrive(415, 950)
    br.WaitForMillis(300)
    br.GyroDrive(-30, 75)
    br.leftAttachmentMotor.run_angle(175, -300, wait=False)
    br.GyroDrive(75, 60)

    # Theater Scene Change

    br.GyroDrive(-150, 900)
    br.GyroTurn(-40)
    br.GyroDrive(500, 900)
    br.GyroTurn(-40)
    br.GyroDrive(-130, 900)
    br.GyroDrive(170, 900)
    for i in range(pushes):
        br.GyroDrive(100, 200)
        br.GyroDrive(-60, 200)
        br.WaitForMillis(775)
    # Wall Squaring

    br.GyroDrive(-33, 900)
    br.GyroTurn(-135)
    br.DriveAndSteer(-215, 0, 1750)

    # Immersive Experience

    br.GyroDrive(269, 900)
    br.GyroTurn(-90)
    br.GyroDrive(428, 900)
    br.GyroTurn(-90)
    br.GyroDrive(58, 900)
    br.leftAttachmentMotor.run_angle(900, 350)
    br.leftAttachmentMotor.run_time(-900, 1000)
    br.GyroDrive(-75, 900)

    # Augmented Reality

    br.GyroTurn(35)
    br.GyroDrive(375, 900)
    br.GyroDrive(-25, 500)
    # br.Curve(40,50)
    # br.leftAttachmentMotor.run_until_stalled(900)

    # # Back To Base

    # br.GyroDrive(100, 900)
    # br.GyroTurn(-45)
    # br.GyroDrive(400, 900)
    # br.Curve(275, 60)
    # br.GyroDrive(300, 900)


if __name__ == "__main__":
    br = BaseRobot()
    Run(br)
