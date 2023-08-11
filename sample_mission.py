from base_robot import *

# Add good comments, such as what the mission is supposed to do,
# how to align the robot in home, any initial starting instructions,
# such as how it should be loaded with anything, arm positions, etc.
br = BaseRobot()

br.leftAttachmentMotor.run_angle(200, 300)
br.WaitForButton(Button.LEFT)
br.GyroDrive(150)
br.WaitForMillis(500)
br.GyroTurn(-93)


# Run(base_robot.BaseRobot()
