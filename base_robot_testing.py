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
from pybricks.robotics import DriveBase
from pybricks.hubs import PrimeHub
from pybricks.tools import wait
from utils import *

# Other constants are defined in utils.py
#
# These are the default parameters to be passed into the different
# movement methods. They are all percents and need to be passed through
# the Rescale() method before passing to pybricks
DEF_STRAIGHT_SPEED_PCT = 65  # Normal driving speed
DEF_STRAIGHT_ACCEL_PCT = 65  # normal acceleration, rarely changed
DEF_TURN_RATE_PCT = 50  # normal turning rate
DEF_TURN_ACCEL_PCT = 50  # normal turning acceleration, rarely changed
DEF_MED_MOT_SPEED_PCT = 100  # Default max speed for attachments
DEF_MED_MOT_TORQUE_PCT = 100  # Default max power for attachments


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
        self.robot = DriveBase(
            self.leftDriveMotor,
            self.rightDriveMotor,
            TIRE_DIAMETER,
            AXLE_TRACK,
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
        Color.SENSOR_MAGENTA = Color(h=333, s=75, v=78)  # h=300,s=100,v=100
        Color.SENSOR_ORANGE = Color(h=8, s=75, v=100)  # h=30,s=100,v=100
        Color.SENSOR_DARKGRAY = Color(h=192, s=21, v=64)  # h=0,s=0,v=50
        Color.SENSOR_NONE = Color(h=170, s=26, v=15)  # h=0,s=0,v=0
        Color.SENSOR_LIME = Color(h=92, s=57, v=93)  # h=92, s=57, v=93

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
            Color.SENSOR_LIME,
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
            Color.SENSOR_LIME: Color.CYAN,
        }

    # Angle is required. Positive angles make the robot turn right and
    # negitive angles make it turn left
    def TurnInPlace(
        self,
        angle,
        then=Stop.BRAKE,
        waitUntilFinished=True,
        turnSpeedPct=DEF_TURN_RATE_PCT,
        turnAccelPct=DEF_TURN_ACCEL_PCT,
        useGyro=True,
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
        self.robot.settings(
            turn_rate=RescaleTurnSpeed(turnSpeedPct),
            turn_acceleration=RescaleTurnAccel(turnAccelPct),
        )
        self.robot.use_gyro(useGyro)
        self.robot.turn(
            angle,
            then,
            waitUntilFinished,
        )

    # Requires distance but speed is optional because of default. Positive
    # goes forward and negative goes backward
    def DriveDist(
        self,
        distance,
        speedPct=DEF_STRAIGHT_SPEED_PCT,
        accelPct=DEF_STRAIGHT_ACCEL_PCT,
        useGyro=True,
        then=Stop.BRAKE,
        waitUntilFinished=True,
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
        self.robot.use_gyro(useGyro)
        self.robot.settings(
            straight_speed=RescaleStraightSpeed(speedPct),
            straight_acceleration=RescaleStraightAccel(accelPct),
        )
        self.robot.straight(distance, then, waitUntilFinished)

    def WallFollowDist(
        self,
        dist,
        turnRate=0,
        speedPct=DEF_STRAIGHT_SPEED_PCT,
        accelPct=DEF_STRAIGHT_ACCEL_PCT,
        useGyro=False,
    ):
        spd = RescaleStraightSpeed(speedPct)
        accel = RescaleStraightAccel(accelPct)
        self.robot.use_gyro(useGyro)
        self.robot.settings(
            straight_acceleration=accel,
        )
        self.robot.reset()  # reset the distance counter to zero
        self.robot.drive(speed=spd, turn_rate=turnRate)
        while self.robot.distance() < dist:
            wait(25)
        self.robot.brake()

    def Curve(
        self,
        radius,
        angle,
        speedPct=DEF_STRAIGHT_SPEED_PCT,
        accelPct=DEF_STRAIGHT_ACCEL_PCT,
        useGyro=True,
        then=Stop.BRAKE,
        waitUntilFinished=True,
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
        self.robot.use_gyro(useGyro)
        self.robot.settings(
            straight_speed=RescaleStraightSpeed(speedPct),
            straight_acceleration=RescaleStraightAccel(accelPct),
            # turn_rate=RescaleTurnSpeed(DEF_TURN_RATE_PCT),
            # turn_acceleration=RescaleTurnAccel(DEF_TURN_ACCEL_PCT),
        )

        self.robot.curve(radius, angle, then, waitUntilFinished)

    def DriveMillis(
        self,
        millis,
        speedPct=DEF_STRAIGHT_SPEED_PCT,
        accelPct=DEF_STRAIGHT_ACCEL_PCT,
        useGyro=True,
        turnRate=0,
    ):
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
        self.robot.use_gyro(useGyro)
        self.robot.settings(
            straight_acceleration=RescaleStraightAccel(accelPct),
        )
        self.robot.drive(
            speed=RescaleStraightSpeed(speedPct),
            turn_rate=turnRate,
        )
        wait(millis)
        self.robot.brake()

    def DriveUntilStalled(
        self,
        speedPct=DEF_STRAIGHT_SPEED_PCT,
        turnRate=0,
        stallPct=100,
        useGyro=True,
    ):
        stallValue = Rescale(
            stallPct, 1, 100, LG_MOT_MIN_VOLTAGE, LG_MOT_MAX_VOLTAGE
        )
        self.robot.use_gyro(useGyro)
        self.leftDriveMotor.settings(max_voltage=stallValue)
        self.rightDriveMotor.settings(max_voltage=stallValue)
        self.robot.drive(
            speed=RescaleStraightSpeed(speedPct), turn_rate=turnRate
        )
        while not self.robot.stalled():
            wait(100)
        self.robot.brake()

        # All done. Reset the default settings
        self.leftDriveMotor.settings(max_voltage=LG_MOT_MAX_VOLTAGE)
        self.rightDriveMotor.settings(max_voltage=LG_MOT_MAX_VOLTAGE)
        self.robot.use_gyro(True)

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

    def UseGyro(self, useGyro):
        self.robot.use_gyro(useGyro)

    def MoveAttachmentMotorDegrees(
        self,
        motor,
        angle,
        speedPct=DEF_MED_MOT_SPEED_PCT,
        then=Stop.HOLD,
        waitUntilFinished=True,
    ):
        speed = RescaleMedMotSpeed(speedPct)
        motor.run_angle(speed, angle, then, waitUntilFinished)

    def MoveAttachmentMotorMillis(
        self,
        motor,
        millis,
        speedPct=DEF_MED_MOT_SPEED_PCT,
        then=Stop.HOLD,
        waitUntilFinished=True,
    ):
        speed = RescaleMedMotSpeed(speedPct)
        motor.run_time(speed, millis, then, waitUntilFinished)

    def MoveAttachmentMotorUntilStalled(
        self,
        motor,
        speedPct=DEF_MED_MOT_SPEED_PCT,
        torquePct=DEF_MED_MOT_TORQUE_PCT,
        then=Stop.HOLD,
    ):
        speed = RescaleMedMotSpeed(speedPct)
        motor.run_until_stalled(speed, then, torquePct)
