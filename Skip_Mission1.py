import base_robot

# br = base_robot.BaseRobot()


# br._leftDriveMotor.run_angle(200, 204.628, 
#                                 Stop.HOLD, False)
# br._rightDriveMotor.run_angle(200, -204.628, 
#                                 Stop.HOLD, False)

# while not (br._leftDriveMotor.done() and br._rightDriveMotor.done()):
#     wait(100)

# br.DriveTank(200, -200, 110, "mm")
# br.DriveTank(70, 70, 30, "cm")
# br.Drive(30)
# br.GyroTurn(650)
# br.WaitForSeconds(.2)
# br.GyroTurn(-65)
def Run(br):
    br.DriveTank(30, 30, -2, "sec")

Run(base_robot.BaseRobot())