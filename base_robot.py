from pybricks.pupdevices import Motor, ColorSensor
from pybricks.parameters import Port, Direction, Axis, Side, Stop, Color, Button
from pybricks.robotics import GyroDriveBase
from pybricks.hubs import PrimeHub
from pybricks.tools import wait


PI = 3.14159

MED_MOTOR_MAX_SPEED = 185 # RPM
LG_MOTOR_MAX_SPEED = 175 # RPM

TIRE_DIAMETER = 56 # mm

ROBOT_MAX_SPEED = LG_MOTOR_MAX_SPEED * PI * TIRE_DIAMETER # mm per sec

class BaseRobot():
    """
    A collection of methods and Spike Prime objects for FLL Team 24277. \
    Uses pybricks for most functionality.

    Example:

    >>> import base_robot
    >>> br = base_robot.BaseRobot()
    >>> br.Drive(40)
    >>> br.GyroTurn(90)
    """

    def __init__(self):
        self.hub = PrimeHub(top_side = Axis.Z, front_side = -Axis.Y)
        self._version = "0.1 05/19/2023"
        self.leftAttachmentMotor = Motor(Port.B)
        self.rightAttachmentMotor = Motor(Port.D)
        self._colorSensor = ColorSensor(Port.F)
        # self._colorSensor.detectable_colors(Color.BLUE, Color.CYAN, 
        #         Color.GREEN, Color.MAGENTA, Color.ORANGE, Color.RED,
        #         Color.VIOLET)
        self._leftDriveMotor = Motor(Port.E, Direction.COUNTERCLOCKWISE)
        self._rightDriveMotor = Motor(Port.A)
        self.driveBase = GyroDriveBase(self._leftDriveMotor, 
                                       self._rightDriveMotor,
                                       TIRE_DIAMETER, 103)
        self.driveBase.settings(400, 600, 150, 360)
        
        self._debugMode = False

        # Reset the yaw angle when the baseRobot is declared
        self.hub.imu.reset_heading(0)

    # TODO: Make all of these abortable
    
    def GyroTurn(self, angle):
        """
Description
-----------
The robot will use the gyro to turn the number of degrees specified. \
Enter positive values to turn to the right, and negative values to turn to \
the left.

Parameter
---------
angle: Number of degrees to turn. Positive values turn to the right \
and negative values turn to the left.
type: int
values: Any
        """

        # Check for abort
        if Button.RIGHT in self.hub.buttons.pressed():
            return

        self.driveBase.turn(angle)


    def Drive(self, distance, then = Stop.HOLD, wait = True):
        """
Description
-----------
The robot will use the gyro to drive in a very straight line

Parameters
----------
distance: How far to drive in cm. Positive values drive forward and \
negative values drive backwards
type: float
values: Any

then: What to do after the drive is complete. Options are coasting, \
holding, and just stopping \
values: Stop.HOLD (default); Stop.COAST; Stop.COAST_SMART; \
Stop.BRAKE; Stop.NONE. For most FLL maneuvers, the default Stop.HOLD will be \
what is needed.
See https://docs.pybricks.com/en/stable/parameters/stop.html for more details.

wait: Whether to wait for the maneuver to complete before continuing \
with the rest of the program. For most FLL maneuvers, the default \
True will be what is needed.
type: bool
values: True (default, wait) or False (do not wait)
        """

        # Check for abort
        if Button.RIGHT in self.hub.buttons.pressed():
            return

        # Multiply the distance by 100 to get mm
        self.driveBase.straight(distance * 10, then, wait)

    # def Curve(self, radius, angle, then = Stop.HOLD, wait = True):
    #     self.driveBase.curve(radius, angle, then, wait)
    
    def DriveTank(self, leftMotorSpeed, rightMotorSpeed, measurement, 
                  units = "cm"):
        """
Description
-----------
Moves the robot using tank-like commands. Provide a left motor speed, \
right motor speed, and a distance, time, or degrees.

Parameters
----------
leftMotorSpeed: Speed for the left motor as a percent of the max speed
type: int
values: -100 to 100

rightMotorSpeed: Speed for the right motor as a percent of the max \
speed
type: int
values: -100 to 100

measurement: Value associated with the units parameter. Determines \
how long/far the robot drives.
type: int
values: Any. Avoid using negative numbers for time.

units: Unit of measurement associated with the measurement parameter
type: String
values: One of cm, deg, degrees, sec, or seconds.
default value: cm
        """

        # Check for abort
        if Button.RIGHT in self.hub.buttons.pressed():
            return
        
        # Normalize the speed and value parameters. If a negative value is
        # provided, invert them all
        if (measurement < 0):
            leftMotorSpeed = -1 * pct2DegPerSec(leftMotorSpeed, 
                                                LG_MOTOR_MAX_SPEED) 
            rightMotorSpeed = -1 * pct2DegPerSec(rightMotorSpeed, 
                                                 LG_MOTOR_MAX_SPEED)
            measurement = -10 * measurement
        else:
            leftMotorSpeed = pct2DegPerSec(leftMotorSpeed, 
                                           LG_MOTOR_MAX_SPEED) 
            rightMotorSpeed = pct2DegPerSec(rightMotorSpeed, 
                                            LG_MOTOR_MAX_SPEED)
            measurement = 10 * measurement
        

        if (units=="cm"):
            # always use the motor with the higher speed to determine the 
            # time driven. Calculate the time that the that the higher
            # speed motor will take to go the distance provided. Use that
            # time to calculate the distance the slower motor will go.
            # I chose the higher speed motor because it is possible that
            # the lower speed motor will have a speed of zero (0)
            if (abs(leftMotorSpeed) > abs(rightMotorSpeed)):
                # Don't have to check if leftMotorSpeed == 0
                rightMotorValue = abs(int(measurement / leftMotorSpeed * 
                                          rightMotorSpeed))
                leftMotorValue = measurement
            elif rightMotorSpeed != 0:
                leftMotorValue = abs(int(measurement / rightMotorSpeed * 
                                         leftMotorSpeed))
                rightMotorValue = measurement
            else: # only way to get here is if both speeds are zerro (0)
                pass

            # Convert the distance to degrees
            rightRotations = rightMotorValue / (TIRE_DIAMETER * PI)
            leftRotations = leftMotorValue / (TIRE_DIAMETER * PI)
            rightDegrees = rightRotations * 360
            leftDegrees = leftRotations * 360
            print("left Deg: " + str(leftDegrees) + "; right deg: "
                  + str(rightDegrees))
            print("left MotSpd: " + str(leftMotorSpeed) + "; right MotSpd: " 
                  + str(rightMotorSpeed))

            # Get the motors moving. Both motors should stop at the same time
            self._leftDriveMotor.run_angle(leftMotorSpeed, leftDegrees, 
                                           Stop.HOLD, False)
            self._rightDriveMotor.run_angle(rightMotorSpeed, rightDegrees, 
                                            Stop.HOLD, False)
            
            while not (self._leftDriveMotor.done() 
                       and self._rightDriveMotor.done()):
                wait(100)

        if (units=="deg" or units == "degrees"):
            # always use the motor with the higher speed to determine the 
            # time driven. Calculate the time that the that the higher
            # speed motor will take to go the distance provided. Use that
            # time to calculate the distance the slower motor will go.
            # I chose the higher speed motor because it is possible that
            # the lower speed motor will have a speed of zero (0)
            if (abs(leftMotorSpeed) > abs(rightMotorSpeed)):
                rightMotorValue = int(measurement / leftMotorSpeed * 
                                      rightMotorSpeed)
                leftMotorValue = measurement
            else:
                leftMotorValue = int(measurement / rightMotorSpeed * 
                                     leftMotorSpeed)
                rightMotorValue = measurement

            # Get the motors moving. Both motors should stop at the same time
            self._leftDriveMotor.run_angle(leftMotorSpeed, leftMotorValue, 
                                           Stop.HOLD, False)
            self._rightDriveMotor.run_angle(rightMotorSpeed, rightMotorValue, 
                                            Stop.HOLD, False)
            while not (self._leftDriveMotor.done() 
                       and self._rightDriveMotor.done()):
                wait(100)

        if (units=="sec" or units == "seconds"):
            # motor.run_time uses milliseconds as a parameter, but kids
            # think in seconds. I have already multiplied the supplied
            # value by ten, so I need to multiply by another 100 to get
            # from seconds to milliseconds
            self._leftDriveMotor.run_time(leftMotorSpeed, measurement * 100, 
                                          Stop.HOLD, False)
            self._rightDriveMotor.run_time(rightMotorSpeed, 
                                           measurement * 100, 
                                           Stop.HOLD, False)
            while not (self._leftDriveMotor.done() 
                       and self._rightDriveMotor.done()):
                wait(100)

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


# this is a static function not associated with the base_robot class
def degPerSec2Pct(dpsValue, maxRpm):
    # All of the pybricks motor commands take a speed argument in degrees
    # per second. EV3 speeds were all 0 to 100 (or -100). This function
    # converts a degPerSecond value to its equivalent EV3 speed, based on
    # the reported max speed for the motor
    return int(dpsValue / (maxRpm / 60 * 360))

def pct2DegPerSec(pctValue, maxRpm):
    # All of the pybricks motor commands take a speed argument in degrees
    # per second. EV3 speeds were all 0 to 100 (or -100). This function
    # converts a degPerSecond value to its equivalent EV3 speed, based on
    # the reported max speed for the motor
    return int((maxRpm / 60 * 360) * pctValue / 100)

def pct2mmps(pctValue):
    # Converts a 0 - 100 percent value to mm per sec speed value
    return int (pctValue / 100 * ROBOT_MAX_SPEED)