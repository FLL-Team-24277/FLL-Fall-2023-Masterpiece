from base_robot import *

def Run(br: BaseRobot):
    # sound Mixer
    # Positive numbers lower the arm; negative raises
    br.leftAttachmentMotor.run_angle(150,-150)


if __name__ == "__main__":
    br = BaseRobot()
    Run(br)
