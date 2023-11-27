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

MAX_LARGE_MOTOR_VOLTAGE = 9000  # mV
MIN_LARGE_MOTOR_VOLTAGE = 3000  # mV
MAX_LARGE_MOTOR_TORQUE = 560


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
        # Use the colorTest.py program to get the color sensor values
        Color.SENSOR_WHITE = Color(h=0, s=0, v=100)  # h=0,s=0,v=100
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
            Color.SENSOR_MAGENTA,
            Color.SENSOR_ORANGE,
            Color.SENSOR_DARKGRAY,
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
    def GyroTurn(
        self, angle, then=Stop.BRAKE, wait=True, speed=STRAIGHT_SPEED
    ):
        """
        Turns the robot to the specified `angle`. \
        Positive numbers turn to the right, negative numbers turn the \
        robot to the left. Note that when the robot makes the turn, it \
        will always overshoot by about seven degrees. In other words if \
        you need a +90 degree turn, you will probably end up commanding \
        something around +83 degrees. Just to make sure the robot has \
        stopped moving before continuing with more instructions. \
        Parameters:
        -------------
        angle: Where the robot should stop turning at. \
            Positive values turn the robot to the right, negative values \
            turn to the left.
        type: float
        values: Any. Best to keep the numbers less than 180, just so the \
            robot doesn't turn more than necessary.
        default: No default value
        -------------
        then: What should happen after robot turning. \
        type: Stop
        values: Stop.HOLD, Stop.BRAKE, Stop.COAST, Stop.COAST_SMART.
        default: Stop.BRAKE
        -------------
        wait: If the robot should wait for this action to \
            stop before doing the next action.
        type: boolean
        values: true, false.
        default: true
        -------------
        speed: How fast the robot should go. \
            Positive values go forward and negative values go backwards.
        type: float
        values: More than -978, but less than 978.
        default: No default value
        """
        self.robot.settings(speed, STRAIGHT_ACCEL, TURN_RATE, TURN_ACCEL)
        self.robot.turn(
            angle,
            then,
            wait,
        )

    # Requires distance but speed is optional because of default. Positive
    # goes forward and negative goes backward
    def GyroDrive(
        self, distance, speed=STRAIGHT_SPEED, then=Stop.BRAKE, wait=True
    ):
        """
        Makes the robot drive for a certain distance. \
        Positive numbers make the robot go forward, and negative \
        numbers make the robot go backwards. The speed has to be \
        more than -978, but less than 978. If you change the \
        value of the wait parameter, it will run 2 actions at once. \
        Just to make sure the robot has stopped moving before \
        continuing with more instructions. \
        Parameters:
        -------------
        speed: How fast the robot should go. \
            Positive values go forward and negative values go backwards.
        type: float
        values: More than -978, but less than 978.
        default: No default value
        -------------
        distance: How far the robot should go. \
            Positive values go forward and negative values go backwards.
        type: float
        values: Any.
        default: No default value
        -------------
        then: What should happen after robot turning. \
        type: Stop
        values: Stop.HOLD, Stop.BRAKE, Stop.COAST, Stop.COAST_SMART.
        default: Stop.BRAKE
        -------------
        wait: If the robot should wait for this action to \
            stop before doing the next action.
        type: boolean
        values: true, false.
        default: true
        """
        if speed > 977:
            speed = 977
        if speed < -977:
            speed = -977
        self.robot.settings(speed, STRAIGHT_ACCEL, TURN_RATE, TURN_ACCEL)
        self.robot.straight(distance, then, wait)

    def GyroDriveForMillis(self, millis, speed=STRAIGHT_SPEED):
        """
        Makes the robot drive for a certain time. \
        Positive speeds make the robot go forward, and negative \
        numbers make the robot go backwards. The speed has to be \
        more than -978, but less than 978. The wait time is in \
        milliseconds, meaning it is seconds times 1000. \
        Just to make sure the robot has stopped moving before \
        continuing with more instructions. \
        Parameters:
        -------------
        speed: How fast the robot should go. \
            Positive values go forward and negative values go backwards.
        type: float
        values: More than -978, but less than 978.
        default: No default value
        -------------
        Millis: How long the robot should drive for. \
        type: float
        values: Any.
        default: None
        """
        if speed > 977:
            speed = 977
        if speed < -977:
            speed = -977
        self.robot.settings(speed, STRAIGHT_ACCEL, TURN_RATE, TURN_ACCEL)
        self.robot.drive(speed, 0)
        wait(millis)
        self.robot.stop()

    # wait for miliseconds. 1000 is one second and 500 is half a second
    def WaitForMillis(self, millis):
        """
        Waits for a button to be pressed\
        Parameters:
        -------------
        millis: How long it should wait. \
        type: float
        values: Any.
        default: No default value
        """
        wait(millis)

    # Wait for Button Press. Requires which button is goin to be pressed.
    def WaitForButton(self, button):
        """
        Waits for a button to be pressed\
        Parameters:
        -------------
        button: Which button that needs to be pressed. \
        type: Button
        values: Button.LEFT, Button.RIGHT, Button.BLUETOOTH.
        default: No default value
        """
        while True:
            pressed = self.hub.buttons.pressed()
            if button in pressed:
                break
            wait(50)

    def Curve(
        self, radius, angle, then=Stop.HOLD, wait=True, speed=STRAIGHT_SPEED
    ):
        """
        Drives the robot in a curve\
        Parameters:
        -------------
        radius: How far the robot should go. \
            Positive values go forward and negative values go backwards.
        type: float
        values: Any.
        default: No default value
        -------------
        Angle: How far the robot should go. \
            Positive values go forward and negative values go backwards.
        type: float
        values: Any.
        default: No default value
        -------------
        then: What should happen after robot turning. \
        type: Stop
        values: Stop.HOLD, Stop.BRAKE, Stop.COAST, Stop.COAST_SMART.
        default: Stop.BRAKE
        -------------
        wait: If the robot should wait for this action to \
            stop before doing the next action.
        type: boolean
        values: true, false.
        default: true
        -------------
        speed: How fast the robot should go. \
            Positive values go forward and negative values go backwards.
        type: float
        values: More than -978, but less than 978.
        default: No default value
        """
        self.robot.settings(speed, STRAIGHT_ACCEL, TURN_RATE, TURN_ACCEL)

        self.robot.curve(radius, angle, then, wait)

    def DriveUntilStalled(
        self, speed=STRAIGHT_SPEED, turn_rate=0, stall=100, useGyro=True
    ):
        if stall > 100:
            stall = 100
        if stall < 0:
            stall = 0

        # convert the percentage to a value between 3000 & 9000
        stallValue = MIN_LARGE_MOTOR_VOLTAGE + stall / 100 * (
            MAX_LARGE_MOTOR_VOLTAGE - MIN_LARGE_MOTOR_VOLTAGE
        )
        self.robot.use_gyro(useGyro)
        self.leftDriveMotor.settings(stallValue)
        self.rightDriveMotor.settings(stallValue)
        self.robot.drive(speed, turn_rate)
        while not self.robot.stalled():
            wait(100)
        self.robot.drive(0, 0)
        wait(100)
        self.leftDriveMotor.settings(MAX_LARGE_MOTOR_VOLTAGE)
        self.rightDriveMotor.settings(MAX_LARGE_MOTOR_VOLTAGE)
        self.robot.use_gyro(True)

    def DriveAndSteer(self, speed, turnrate, time):
        """
        Makes the robot drive at a certain turnrate. \
        Positive numbers make the robot go forward, and negative \
        numbers make the robot go backwards. The speed has to be \
        more than -978, but less than 978. If you change the \
        value of the wait parameter, it will run 2 actions at once. \
        Just to make sure the robot has stopped moving before \
        continuing with more instructions. \
        Parameters:
        -------------
        speed: How fast the robot should go. \
            Positive values go forward and negative values go backwards.
        type: float
        values: More than -978, but less than 978.
        default: No default value
        -------------
        turnrate: How much the robot should turn at a time. \
        type: float
        values: Any.
        default: No default value
        -------------
        time: How long the robot should drive for in miliseconds. \
        type: float
        values: Any.
        default: No default value
        """
        if speed > 977:
            speed = 977
        if speed < -977:
            speed = -977
        self.robot.use_gyro(False)
        self.robot.drive(speed, turnrate)
        self.WaitForMillis(time)
        self.robot.stop()
        self.robot.use_gyro(True)
