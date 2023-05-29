import base_robot

br = base_robot.BaseRobot()

br.DriveTank(20, 20, 1, "sec")
br.leftAttachmentMotor.angle(180)

# br.DriveTank(200, -200, 110, "mm")
# br.DriveTank(70, 70, 30, "cm")
# br.Drive(30)
# br.GyroTurn(650)
# br.WaitForSeconds(.2)
# br.GyroTurn(-65)

# Run(base_robot.BaseRobot())