import base_robot
from pybricks.parameters import Port, Direction, Axis, Side, Stop, Color
from pybricks.tools import wait

br = base_robot.BaseRobot()


# br._leftDriveMotor.run_angle(200, 204.628, 
#                                 Stop.HOLD, False)
# br._rightDriveMotor.run_angle(200, -204.628, 
#                                 Stop.HOLD, False)

# while not (br._leftDriveMotor.done() and br._rightDriveMotor.done()):
#     wait(100)

br.DriveTank(-200, -200, -110, "mm")
