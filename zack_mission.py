from base_robot import *


def Run(br: BaseRobot):
    # Positive numbers lower the arm; negative raises
    # Positive makes the robot go forward/ Negative makes the robot go backward
    # 3D Cinema

    br.GyroDrive(315, 950)
    br.leftAttachmentMotor.run_until_stalled(700)
    br.GyroDrive(-300, 700)

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

    br.GyroDrive(370, 950)
    br.GyroDrive(50, 75)
    br.GyroDrive(-25, 75)
    br.leftAttachmentMotor.run_angle(195, -300, wait=False)
    br.GyroDrive(55, 60)

    # Theater Scene Change

    br.GyroDrive(-150, 700)
    br.GyroTurn(-40)
    br.GyroDrive(500, 700)
    br.GyroTurn(-40)
    br.GyroDrive(-130, 500)
    br.GyroDrive(170, 500)
    for i in range(pushes):
        br.GyroDrive(95, 175)
        br.GyroDrive(-60, 200)
        br.WaitForMillis(775)
    # Wall Squaring

    br.GyroDrive(-50, 900)
    br.GyroTurn(-135)
    br.DriveAndSteer(-215, 0, 1750)

    # Immersive Experience

    br.GyroDrive(269, 900)
    br.GyroTurn(-90)
    br.GyroDrive(427, 900)
    br.GyroTurn(-90)
    br.GyroDrive(50, 500)
    br.leftAttachmentMotor.run_angle(900, 350)
    br.leftAttachmentMotor.run_time(-900, 1000)
    br.GyroDrive(-50, 900)

    # Augmented Reality

    br.GyroTurn(45)
    br.leftAttachmentMotor.run_until_stalled(700)
    br.GyroDrive(200, 700)
    br.Curve(radius=400, angle=27)
    br.GyroDrive(-25,500)
    br.GyroTurn(75)
    
    # Back To Base

    br.GyroDrive(100,500)
    br.GyroTurn(-30)
    br.GyroDrive(600, 900)

    

if __name__ == "__main__":
    br = BaseRobot()
    Run(br)
