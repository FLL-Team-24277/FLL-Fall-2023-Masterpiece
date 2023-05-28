from pybricks.pupdevices import Motor, ColorSensor
from pybricks.parameters import Port, Direction, Axis, Side, Stop, Color
from pybricks.robotics import GyroDriveBase
from pybricks.hubs import PrimeHub
from pybricks.tools import wait


PI = 3.14159

# Max speed for motors
# https://le-www-live-s.legocdn.com/sc/media/files/support/spike-prime/techspecs_technicmediumangularmotor-19684ffc443792280359ef217512a1d1.pdf
# https://education.lego.com/v3/assets/blt293eea581807678a/bltb9abb42596a7f1b3/5f8801b5f4c5ce0e93db1587/le_spike-prime_tech-fact-sheet_45602_1hy19.pdf
MED_MOTOR_MAX_SPEED = 185 # RPM
LG_MOTOR_MAX_SPEED = 175 # RPM

TIRE_DIAMETER = 56 # mm

ROBOT_MAX_SPEED = LG_MOTOR_MAX_SPEED * PI * TIRE_DIAMETER # mm per sec

class BaseRobot():
    """
    A collection of methods and Spike Prime objects for FLL Team 24277. \
    The BaseRobot class has two drive motors as a MotorPair, two medium \
    motors for moving attachments, and all of the base methods available \
    for Spike Prime sensors and motors. It also includes some custom \
    methods for moving the robot. Enjoy!


    Example:

    >>> import base_robot
    >>> import sys
    >>> br = base_robot.BaseRobot()
    >>> br.AccelGyroDriveForward(40)
    >>> br.GyroTurn(90)
    """

    def __init__(self):
        self.hub = PrimeHub(Axis.Z, Axis.Y)
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

        # self._mediumMotorMaxSpeed = 185 # rpm
        # self._largeMotorMaxSpeed = 175 # rpm
        # self._robotMaxSpeed = self._largeMotorMaxSpeed * 3.14159 * self._tireDiameter

    # TODO: Make all of these abortable
    
    # Just a wrapper for drivebase.turn()
    def GyroTurn(self, angle):
        self.driveBase.turn(angle)

    # Just a wrapper for drivebase.straight()
    def Drive(self, distance, then = Stop.HOLD, wait = True):
        # Multiply the distance by 100 to get mm
        self.driveBase.straight(distance * 10, then, wait)

    # def Curve(self, radius, angle, then = Stop.HOLD, wait = True):
    #     self.driveBase.curve(radius, angle, then, wait)
    
    def DriveTank(self, leftMotorSpeed, rightMotorSpeed, value, units = "cm"):
        """
        Moves the robot using tank-like commands. Provide a left motor speed,
        right motor speed, and a distance, time, or degrees.

        :param leftMotorSpeed: The speed for the left motor 0 - 100 (or -100)
        :type leftMotorSpeed: int
        
        :param rightMotorSpeed: The speed for the right motor 0 - 100 (or -100)
        :type rightMotorSpeed: int

        :param value: Value associated with the units paramter. Determines how long/far the robot drives.
        :type value: int

        :param units: One of cm, deg, degrees, sec, or seconds.
        :type units: String
        """
        # Normalize the speed and value parameters. If a negative value is
        # provided, invert them all
        if (value < 0):
            leftMotorSpeed = -1 * pct2DegPerSec(leftMotorSpeed, LG_MOTOR_MAX_SPEED) 
            rightMotorSpeed = -1 * pct2DegPerSec(rightMotorSpeed, LG_MOTOR_MAX_SPEED)
            value = -10 * value
        else:
            leftMotorSpeed = pct2DegPerSec(leftMotorSpeed, LG_MOTOR_MAX_SPEED) 
            rightMotorSpeed = pct2DegPerSec(rightMotorSpeed, LG_MOTOR_MAX_SPEED)
            value = 10 * value
        

        if (units=="cm"):
            # always use the motor with the higher speed to determine the 
            # time driven. Calculate the time that the that the higher
            # speed motor will take to go the distance provided. Use that
            # time to calculate the distance the slower motor will go.
            # I chose the higher speed motor because it is possible that
            # the lower speed motor will have a speed of zero (0)
            if (abs(leftMotorSpeed) > abs(rightMotorSpeed)):
                # Don't have to check if leftMotorSpeed == 0
                rightMotorValue = abs(int(value / leftMotorSpeed * rightMotorSpeed))
                leftMotorValue = value
            elif rightMotorSpeed != 0:
                leftMotorValue = abs(int(value / rightMotorSpeed * leftMotorSpeed))
                rightMotorValue = value
            else: # only way to get here is if both speeds are zerro (0)
                pass

            # Convert the distance to degrees
            rightRotations = rightMotorValue / (TIRE_DIAMETER * PI)
            leftRotations = leftMotorValue / (TIRE_DIAMETER * PI)
            rightDegrees = rightRotations * 360
            leftDegrees = leftRotations * 360
            print("left Deg: " + str(leftDegrees) + "; right deg: " + str(rightDegrees))
            print("left MotSpd: " + str(leftMotorSpeed) + "; right MotSpd: " + str(rightMotorSpeed))

            # Get the motors moving. Both motors should stop at the same time
            self._leftDriveMotor.run_angle(leftMotorSpeed, leftDegrees, 
                                           Stop.HOLD, False)
            self._rightDriveMotor.run_angle(rightMotorSpeed, rightDegrees, 
                                            Stop.HOLD, False)
            
            while not (self._leftDriveMotor.done() and self._rightDriveMotor.done()):
                wait(100)

        if (units=="deg" or units == "degrees"):
            # always use the motor with the higher speed to determine the 
            # time driven. Calculate the time that the that the higher
            # speed motor will take to go the distance provided. Use that
            # time to calculate the distance the slower motor will go.
            # I chose the higher speed motor because it is possible that
            # the lower speed motor will have a speed of zero (0)
            if (abs(leftMotorSpeed) > abs(rightMotorSpeed)):
                rightMotorValue = int(value / leftMotorSpeed * rightMotorSpeed)
                leftMotorValue = value
            else:
                leftMotorValue = int(value / rightMotorSpeed * leftMotorSpeed)
                rightMotorValue = value

            # Get the motors moving. Both motors should stop at the same time
            self._leftDriveMotor.run_angle(leftMotorSpeed, leftMotorValue, 
                                           Stop.HOLD, False)
            self._rightDriveMotor.run_angle(rightMotorSpeed, rightMotorValue, 
                                            Stop.HOLD, False)

        if (units=="sec" or units == "seconds"):
            # motor.run_time uses milliseconds as a parameter, but kids
            # think in seconds.
            self._leftDriveMotor.run_time(leftMotorSpeed, value * 1000, 
                                          Stop.HOLD, False)
            self._rightDriveMotor.run_time(rightMotorSpeed, value * 1000, 
                                           Stop.HOLD, False)

    def GetAttachmentColor(self):
        # return attachment color
        return self._colorSensor.color()
    
    def GetVersion(self, number):
        return self._version
    
    def WaitForSeconds(self, seconds):
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