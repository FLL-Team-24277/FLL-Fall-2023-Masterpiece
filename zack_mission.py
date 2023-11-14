from base_robot import *


def Run(br: BaseRobot):
    # Positive numbers lower the arm; negative raises
    # Positive makes the robot go forward/ Negative makes the robot go backward
    # 3D Cinema

    print(str(br.hub.battery.voltage()))
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
        br.GyroDrive(115, 200)
        br.GyroDrive(-60, 200)
        br.WaitForMillis(775)
    # Wall Squaring

    br.GyroDrive(-33, 900)
    br.GyroTurn(-135)
    br.DriveAndSteer(-215, 0, 1750)

    # Driving to Immersive Experience-purple guy

    br.GyroDrive(240, 900)
    br.GyroTurn(-90)
    br.GyroDrive(430, 900)
    br.GyroTurn(-90)

    # Doing Immersive Expeiriance-purple guy

    br.GyroDrive(35, 900)
    br.leftAttachmentMotor.run_time(speed=1000, time=1400)
    br.leftAttachmentMotor.run_until_stalled(-900)
    br.GyroDrive(-75, 900)

    # Driving to Augmented Reality-blue flower

    br.GyroTurn(38)
    br.GyroDrive(324, 900)
    br.GyroTurn(25)
    br.WaitForMillis(250)
    br.GyroDriveForMillis(-1150, 500)
    br.GyroTurn(15)

    # Driving to next  mission

    br.leftAttachmentMotor.run_until_stalled(700)
    br.DriveAndSteer(350, -35, 665)
    br.WaitForMillis(250)
    br.GyroDrive(-65, 500)

    # Doing Augmented Reality-blue flower

    br.GyroTurn(70)
    br.GyroDrive(45, 900)
    br.WaitForMillis(250)
    br.Curve(radius=223, angle=-95)
    br.GyroDrive(-40, 900)
    br.GyroTurn(65)
    br.GyroDrive(100, 900)
    br.GyroTurn(27)
    br.GyroDrive(-200, 900)
    br.GyroTurn(-10)
    br.GyroDriveForMillis(2250, 900)


if __name__ == "__main__":
    br = BaseRobot()
    Run(br)
