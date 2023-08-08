from pybricks.pupdevices import Motor, ColorSensor
from pybricks.parameters import (
    Port,
    Direction,
    Axis,
    Side,
    Stop,
    Color,
    Button,
    Icon,
)
from pybricks.robotics import GyroDriveBase
from pybricks.hubs import PrimeHub
from pybricks.tools import wait

# All constents will be defined here
TIRE_DIAMETER = 56  # mm
AXLE_TRACK = 103  # distance between the wheels, mm

STRAIGHT_SPEED = 400  # normal straight speed for driving, mm/sec
STRAIGHT_ACCEL = 600  # normal acceleration, mm/sec^2
TURN_RATE = 150  # normal turning rate, deg/sec
TURN_ACCEL = 360  # normal turning acceleration, deg/sec^2


class BaseRobot:
    """
    A collection of methods and Spike Prime for FLL Team 24277. \
    Uses pybricks for most functionality.

    Example:

    >>> from base_robot import *
    >>> br = BaseRobot()
    >>> br.GyroDrive(400) #400mm at default speed
    >>> br.GyroTurn(90) #90 deg to the right
    """

    def __init__(self):
        self.hub = PrimeHub(top_side=Axis.Z, front_side=-Axis.Y)
        self._version = "0.1 05/19/2023"
        self.leftDriveMotor = Motor(Port.E, Direction.COUNTERCLOCKWISE)
        self.rightDriveMotor = Motor(Port.A)
        self.robot = GyroDriveBase(
            self.leftDriveMotor,
            self.rightDriveMotor,
            TIRE_DIAMETER,
            AXLE_TRACK,
        )
        # default speeds were determined by testing
        self.robot.settings(
            STRAIGHT_SPEED, STRAIGHT_ACCEL, TURN_RATE, TURN_ACCEL
        )
        self.leftAttachmentMotor = Motor(Port.B)
        self.rightAttachmentMotor = Motor(Port.D)

        self.colorSensor = ColorSensor(Port.F)

        # HSV values were found by testing. Default hsv-values are provided
        # in comments. Theoretically, the farther apart the hsv-values are,
        # the less likely two colors can get "confused"
        Color.SENSOR_WHITE = Color(h=0, s=0, v=100)  # h=0,s=0,v=0
        Color.SENSOR_RED = Color(h=353, s=82, v=92)  # h=0,s=100,v=100
        Color.SENSOR_YELLOW = Color(h=60, s=50, v=100)  # h=60,s=100,v=100
        Color.SENSOR_GREEN = Color(h=156, s=66, v=66)  # h=120,s=100,v=100
        Color.SENSOR_BLUE = Color(h=216, s=84, v=83)  # h=240,s=100,v=100
        Color.SENSOR_MAGENTA = Color(h=339, s=71, v=81)  # h=300,s=100,v=100
        Color.SENSOR_ORANGE = Color(h=13, s=73, v=100)  # h=30,s=100,v=100
        Color.SENSOR_DARKGRAY = Color(h=192, s=21, v=64)  # h=0,s=0,v=50
        Color.SENSOR_NONE = Color(h=170, s=26, v=15)  # h=0,s=0,v=0

        # Put the custom colors in a list. Best practice is to only use
        # colors that we are using for actual missions.
        self.sensorColors = [
            Color.SENSOR_WHITE,
            Color.SENSOR_RED,
            Color.SENSOR_YELLOW,
            Color.SENSOR_GREEN,
            Color.SENSOR_BLUE,
            # Color.SENSOR_MAGENTA,
            # Color.SENSOR_ORANGE,
            # Color.SENSOR_DARKGRAY,
            Color.SENSOR_NONE,  # must have SENSOR_NONE. Do not comment
        ]

        # Set the detectable colors usisng our list
        self.colorSensor.detectable_colors(self.sensorColors)

        # Translates our costom colors into the default pybricks colors
        # Used to set the hub light to the correct color. It dodesn't
        # matter if there are extra colors in here that won't be detected
        self.myColor2DefaultColorDict = {
            Color.SENSOR_GREEN: Color.GREEN,
            Color.SENSOR_RED: Color.RED,
            Color.SENSOR_YELLOW: Color.YELLOW,
            Color.SENSOR_BLUE: Color.BLUE,
            Color.SENSOR_MAGENTA: Color.MAGENTA,
            Color.SENSOR_WHITE: Color.WHITE,
            Color.SENSOR_ORANGE: Color.ORANGE,
            Color.SENSOR_DARKGRAY: Color.GRAY,
            Color.SENSOR_NONE: Color.NONE,
        }

    # Angle is required. Positive angles make the robot turn right and
    # negitive angles make it turn left
    def GyroTurn(self, angle, then=Stop.BRAKE, wait=True):
        self.robot.turn(angle, then, wait)

    # Requires distance but speed is optional because of default. Positikve
    # goes forward and negative goes backward
    def GyroDrive(
        self, distance, speed=STRAIGHT_SPEED, then=Stop.BRAKE, wait=True
    ):
        self.robot.settings(speed, STRAIGHT_ACCEL, TURN_RATE, TURN_ACCEL)
        self.robot.straight(distance, then, wait)

    # wait for miliseconds. 1000 is one second and 500 is half a second
    def WaitForMillis(self, millis):
        wait(millis)
