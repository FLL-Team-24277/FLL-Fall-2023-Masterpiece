from base_robot import *


def Run(br: BaseRobot):
    br.rightAttachmentMotor.run_angle(977, 150)
    # br.leftAttachmentMotor.run_until_stalled(-977)
    br.GyroDrive(390, 977)
    br.rightAttachmentMotor.run_angle(977, -200)
    br.leftAttachmentMotor.run_angle(100, 150)
    br.WaitForMillis(100)
    br.rightAttachmentMotor.run_angle(977, 200)
    br.GyroDrive(-390, 977)


if __name__ == "__main__":
    br = BaseRobot()
    Run(br)
# nothing left :) :3 C:
