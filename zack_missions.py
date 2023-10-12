from base_robot import *

def Run(br: BaseRobot):
    # Positive numbers lower the arm; negative raises
    # Positive makes the robot go forward/ Negative makes the robot go backward
    # 3D Cinema
    # br.GyroDrive(315,950)
    # br.leftAttachmentMotor.run_until_stalled(700)
    # br.GyroDrive(-300,700)
    # # Sound Mixer
    # br.WaitForButton(Button.LEFT)
    # br.GyroDrive(370,950)
    # br.GyroDrive(50,75)
    # br.GyroDrive(-25,75)
    # br.leftAttachmentMotor.run_angle(195,-300,wait=False)
    # br.GyroDrive(55,60)
    # # Theater Scene Change
    # br.GyroDrive(-150,700)
    # br.GyroTurn(-40)
    # br.GyroDrive(485,700)
    # br.GyroTurn(-40)
    # br.GyroDrive(-125,500)
    br.GyroDrive(250,700)
    br.GyroDrive(-175,700)
    


if __name__ == "__main__":
    br = BaseRobot()
    Run(br)
