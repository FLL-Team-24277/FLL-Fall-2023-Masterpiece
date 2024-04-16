from base_robot import *


def Run(br: BaseRobot):

    br.leftAttachmentMotor.run_until_stalled(speed=900,duty_limit=50)
    br.GyroDrive(415, 950)
    br.WaitForMillis(300)
    br.GyroDrive(-30, 75)
    br.leftAttachmentMotor.run_angle(150, -300, wait=False)
    br.GyroDrive(22, 30)
    br.WaitForMillis(500)
    br.GyroTurn(angle=25,speed=25)
    br.GyroDrive(75, 60)

if __name__ == "__main__":
    br = BaseRobot()
    Run(br)
