from base_robot import *

def Run(br: BaseRobot):
    # Positive numbers lower the arm; negative raises
    # Positive makes the robot go forward/ Negative makes the robot go backward
    # 3D Cinema
    br.GyroDrive(310,950)
    br.leftAttachmentMotor.run_angle(300,300)
    br.GyroDrive(-300,700)
    # Sound Mixer
    br.WaitForButton(Button.LEFT)
    # br.leftAttachmentMotor.run_until_stalled(500,duty_limit=50)
    br.GyroDrive(370,950)
    br.GyroDrive(50,75)
    br.GyroDrive(-25,75)
    br.leftAttachmentMotor.run_angle(195,-300,wait=False)
    br.GyroDrive(55,60)
    # Theater Scene Change
    br.GyroDrive(-200,700)
    br.GyroTurn(-45)


if __name__ == "__main__":
    br = BaseRobot()
    Run(br)
