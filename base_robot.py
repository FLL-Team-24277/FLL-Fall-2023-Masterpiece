from pybricks.pupdevices import Motor, ColorSensor
from pybricks.parameters import Port, Direction, Axis, Side, Stop, Color, Button, Icon
from pybricks.robotics import GyroDriveBase
from pybricks.hubs import PrimeHub
from pybricks.tools import wait


PI = 3.14159

MED_MOTOR_MAX_SPEED = 185  # RPM
LG_MOTOR_MAX_SPEED = 175  # RPM

TIRE_DIAMETER = 56  # mm
AXLE_TRACK = 103  # distance between the wheels, mm

STRAIGHT_SPEED = 400  # normal straight speed for driving, mm/sec
STRAIGHT_ACCEL = 600  # normal acceleration, mm/sec^2
TURN_RATE = 150  # normal turning rate, deg/sec
TURN_ACCEL = 360  # normal turning acceleration, deg/sec^2
# ROBOT_MAX_SPEED = LG_MOTOR_MAX_SPEED * PI * TIRE_DIAMETER # mm per sec


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
        self.leftAttachmentMotor = Motor(Port.B)
        self.rightAttachmentMotor = Motor(Port.D)
        self._colorSensor = ColorSensor(Port.F)
        # self._colorSensor.detectable_colors(Color.BLUE, Color.CYAN,
        #         Color.GREEN, Color.MAGENTA, Color.ORANGE, Color.RED,
        #         Color.VIOLET)
        self._leftDriveMotor = Motor(Port.E, Direction.COUNTERCLOCKWISE)
        self._rightDriveMotor = Motor(Port.A)

        self.driveBase = GyroDriveBase(
            self._leftDriveMotor, self._rightDriveMotor, TIRE_DIAMETER, AXLE_TRACK
        )

        self.driveBase.settings(STRAIGHT_SPEED, STRAIGHT_ACCEL, TURN_RATE, TURN_ACCEL)

        self._debugMode = False

        # Reset the yaw angle when the baseRobot is declared
        self.hub.imu.reset_heading(0)

    # TODO: Make all of these abortable

    def GyroTurn(self, angle):
        """The robot will use the gyro to turn the number of degrees specified.

        Args:
            angle (int): Enter positive values to turn to the right, and negative values to turn to the left.
        """

        # Check for abort
        if Button.RIGHT in self.hub.buttons.pressed():
            return

        self.driveBase.turn(angle)

    def Drive(self, distance, then=Stop.HOLD, wait=True):
        """The robot will use the gyro to drive in a very straight line

        Args:
            distance (int): How far to drive in mm. Positive values drive forward and negative values drive backwards
            then (Stop.*, optional): What to do after the drive is complete. Options are coasting, holding, and just stopping.
            wait (bool, optional): Whether to wait for the maneuver to complete before continuing with the rest of the program. For most FLL maneuvers, the default True will be what is needed. Defaults to True.
        """

        # Check for abort
        if Button.RIGHT in self.hub.buttons.pressed():
            return

        self.driveBase.straight(distance, then, wait)

    def DriveTank(self, leftMotorSpeed, rightMotorSpeed, measurement, units="mm"):
        """Moves the robot using tank-like commands

        Args:
            leftMotorSpeed (int): Speed for the left motor in degrees per second
            rightMotorSpeed (int): Speed for the right motor in degrees per second
            measurement (float): Value associated with the units parameter. Determines how long/far the robot drives.
            units (str, optional): Unit of measurement associated with the measurement parameter. Defaults to "mm".
        """

        # Check for abort
        if Button.RIGHT in self.hub.buttons.pressed():
            return

        # Normalize the speed and value parameters. If a negative value is
        # provided, invert them all
        if measurement < 0:
            leftMotorSpeed = -1 * leftMotorSpeed
            rightMotorSpeed = -1 * rightMotorSpeed
            measurement = -1 * measurement

        if units == "mm":
            # always use the motor with the higher speed to determine the
            # time driven. Calculate the time that the that the higher
            # speed motor will take to go the distance provided. Use that
            # time to calculate the distance the slower motor will go.
            # I chose the higher speed motor because it is possible that
            # the lower speed motor will have a speed of zero (0)
            if abs(leftMotorSpeed) > abs(rightMotorSpeed):
                # Don't have to check if leftMotorSpeed == 0
                rightMotorValue = abs(
                    int(measurement / leftMotorSpeed * rightMotorSpeed)
                )
                leftMotorValue = measurement
            elif rightMotorSpeed != 0:
                leftMotorValue = abs(
                    int(measurement / rightMotorSpeed * leftMotorSpeed)
                )
                rightMotorValue = measurement
            else:  # only way to get here is if both speeds are zerro (0)
                pass

            # Convert the distance to degrees
            rightRotations = rightMotorValue / (TIRE_DIAMETER * PI)
            leftRotations = leftMotorValue / (TIRE_DIAMETER * PI)
            rightDegrees = rightRotations * 360
            leftDegrees = leftRotations * 360

            # Get the motors moving. Both motors should stop at the same time
            self._leftDriveMotor.run_angle(
                leftMotorSpeed, leftDegrees, Stop.HOLD, False
            )
            self._rightDriveMotor.run_angle(
                rightMotorSpeed, rightDegrees, Stop.HOLD, False
            )

            while not (self._leftDriveMotor.done() and self._rightDriveMotor.done()):
                wait(10)

        if units == "deg" or units == "degrees":
            # always use the motor with the higher speed to determine the
            # time driven. Calculate the time that the that the higher
            # speed motor will take to go the distance provided. Use that
            # time to calculate the distance the slower motor will go.
            # I chose the higher speed motor because it is possible that
            # the lower speed motor will have a speed of zero (0)
            if abs(leftMotorSpeed) > abs(rightMotorSpeed):
                rightMotorValue = int(measurement / leftMotorSpeed * rightMotorSpeed)
                leftMotorValue = measurement
            else:
                leftMotorValue = int(measurement / rightMotorSpeed * leftMotorSpeed)
                rightMotorValue = measurement

            # Get the motors moving. Both motors should stop at the same time
            self._leftDriveMotor.run_angle(
                leftMotorSpeed, leftMotorValue, Stop.HOLD, False
            )
            self._rightDriveMotor.run_angle(
                rightMotorSpeed, rightMotorValue, Stop.HOLD, False
            )
            while not (self._leftDriveMotor.done() and self._rightDriveMotor.done()):
                wait(10)

        if units == "sec" or units == "seconds":
            # motor.run_time uses milliseconds as a parameter, but kids
            # think in seconds. Multiply by 1000 to get from seconds to
            # milliseconds
            self._leftDriveMotor.run_time(
                leftMotorSpeed, measurement * 1000, Stop.HOLD, False
            )
            self._rightDriveMotor.run_time(
                rightMotorSpeed, measurement * 1000, Stop.HOLD, False
            )
            while not (self._leftDriveMotor.done() and self._rightDriveMotor.done()):
                wait(10)

    def GetAttachmentColor(self):
        # return attachment color
        return self._colorSensor.color()

    def GetVersion(self, number):
        return self._version

    def WaitForSeconds(self, seconds):
        # Check for abort
        if Button.RIGHT in self.hub.buttons.pressed():
            return

        wait(seconds * 1000)

    def WaitForLeftButtonPress(self):
        # Check for abort
        if Button.RIGHT in self.hub.buttons.pressed():
            return

        while not Button.LEFT in self.hub.buttons.pressed():
            wait(10)
        return
