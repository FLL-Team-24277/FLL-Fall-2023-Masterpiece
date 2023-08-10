from pybricks.pupdevices import Motor, ColorSensor
from pybricks.parameters import Port, Direction, Axis, Side, Stop, Color, Button, Icon
from pybricks.robotics import GyroDriveBase
from pybricks.hubs import PrimeHub
from pybricks.tools import wait


PI = 3.14159

TIRE_DIAMETER = 56  # mm
AXLE_TRACK = 103  # distance between the wheels, mm

STRAIGHT_SPEED = 550  # normal straight speed for driving, mm/sec
STRAIGHT_ACCEL = 600  # normal acceleration, mm/sec^2
TURN_RATE = 150  # normal turning rate, deg/sec
TURN_ACCEL = 360  # normal turning acceleration, deg/sec^2


class BaseRobot:
    """
    A collection of methods and Spike Prime objects for FLL Team 24277. \
    Uses pybricks for most functionality.

    Example:

    >>> import base_robot
    >>> br = base_robot.BaseRobot()
    >>> br.Drive(400) #400mm
    >>> br.GyroTurn(90) #90 deg to the right
    """

    def __init__(self):
        self.hub = PrimeHub(top_side=Axis.Z, front_side=-Axis.Y)
        self._version = "0.1 05/19/2023" 
        self._leftmotor = Motor(Port.E, Direction.COUNTERCLOCKWISE)
        self._rightmotor = Motor(Port.A)

        self._robot = GyroDriveBase(self._leftmotor, self._rightmotor, 56, 103)
        self._robot.settings(STRAIGHT_SPEED, STRAIGHT_ACCEL, TURN_RATE, TURN_ACCEL)

    def GyroTurn(self, angle):
        pass

    def GyroDrive(self, distance, speed=STRAIGHT_SPEED, then=Stop.HOLD, wait=True):
        self._robot.settings(speed, STRAIGHT_ACCEL, TURN_RATE, TURN_ACCEL)
        self._robot.straight(distance, then, wait)

        pass

    def DriveTank(self, leftMotorSpeed, rightMotorSpeed, measurement, units="mm"):
        pass

