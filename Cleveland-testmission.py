# from pybricks.pupdevices import Motor
# from pybricks.parameters import Port, Direction
# from pybricks.robotics import GyroDriveBase


# leftmotor = Motor(Port.E, Direction.COUNTERCLOCKWISE)
# rightmotor = Motor(Port.A)
    
# robot = GyroDriveBase(leftmotor, rightmotor, 56, 103)

# robot.straight(1000)

import cleveland_base_robot

br = cleveland_base_robot.BaseRobot()

br.GyroTurn(-60)
