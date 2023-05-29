import base_robot

def Run(br: base_robot.BaseRobot):
    br.DriveTank(30, 30, -2, "sec")
    br.leftAttachmentMotor.angle(180)

    # br.DriveTank(200, -200, 110, "mm")
    # br.DriveTank(70, 70, 30, "cm")
    # br.Drive(30)
    # br.GyroTurn(650)
    # br.WaitForSeconds(.2)
    # br.GyroTurn(-65)

Run(base_robot.BaseRobot())