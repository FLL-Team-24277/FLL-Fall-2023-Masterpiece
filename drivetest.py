from pybricks.pupdevices import Motor
from pybricks.parameters import (
    Port,
    Direction,
    Axis,
    Stop,
)
from pybricks.robotics import GyroDriveBase
from pybricks.hubs import PrimeHub
from pybricks.tools import wait


TIRE_DIAMETER = 56  # mm
AXLE_TRACK = 103  # distance between the wheels, mm

STRAIGHT_SPEED = 400  # normal straight speed for driving, mm/sec
STRAIGHT_ACCEL = 600  # normal acceleration, mm/sec^2
TURN_RATE = 150  # normal turning rate, deg/sec
TURN_ACCEL = 360  # normal turning acceleration, deg/sec^2

hub = PrimeHub(top_side=Axis.Z, front_side=-Axis.Y)
leftDriveMotor = Motor(Port.E, Direction.COUNTERCLOCKWISE)
rightDriveMotor = Motor(Port.A)
robot = GyroDriveBase(
    leftDriveMotor,
    rightDriveMotor,
    TIRE_DIAMETER,
    AXLE_TRACK,
)
robot.settings(STRAIGHT_SPEED, STRAIGHT_ACCEL, TURN_RATE, TURN_ACCEL)

robot.use_gyro(True)
robot.drive(speed=300, turn_rate=0)
wait(500)
robot.stop()
wait(250)
robot.straight(distance=-20)
#wait(4000)
#robot.stop()
#robot.use_gyro(True)
