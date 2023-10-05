from base_robot import *

def Run(br: BaseRobot):
    # sound Mixer
    # Positive numbers lower the arm; negative raises
    # Positive makes the robot go forward/ Negative makes the robot go backward
    br.GyroDrive(360)
    br.leftAttachmentMotor.run_angle(175,-150,wait=False)
    br.GyroDrive(50,50)
    br.GyroDrive(-295)


if __name__ == "__main__":
    br = BaseRobot()
    Run(br)
