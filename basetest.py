from base_robot_testing import *

# Add good comments, such as what the mission is supposed to do,
# how to align the robot in home, any initial starting instructions,
# such as how it should be loaded with anything, arm positions, etc.


# When we run this program from the master program, we will call this
# "Run(br)" method.
def Run(br: BaseRobot):
    # Your mission code goes here, step-by-step
    # It MUST be indented just like the lines below
    # br.rightAttachmentMotor.run_angle(speed=1000, rotation_angle=180)
    # br.MoveRightAttachmentMotorDegrees(angle=360, speedPct=100, torquePct=-50, accelPct=-50)
    # Default values are 1000, 2000, 199
    # br.rightAttachmentMotor.control.limits(1000, 2000, 199)
    # br.rightAttachmentMotor.run_angle(977, 1800)
    # br.WaitForMillis(500)

    # br.MoveRightAttachmentMotorDegrees(angle=180, speedPct=1)
    # br.GyroDriveImproved(speedPct=-1)
    # br.rightAttachmentMotor.run_angle(1000, 3600)
    # br.DriveUntilStalled(speedPct=20, stallPct=20)
    br.MoveAttachmentMotorUntilStalled(br.rightAttachmentMotor, speedPct=100, torquePct=25)
    # br.MoveAttachmentMotorDegrees(br.rightAttachmentMotor, angle=720, speedPct=75)
    # br.TurnInPlace(angle=360, turnSpeedPct=25, then=Stop.BRAKE)
    # br.TurnInPlace(angle=-360, turnSpeedPct=50, then=Stop.BRAKE)
    # br.TurnInPlace(angle=360, turnSpeedPct=75, then=Stop.BRAKE)
    # br.TurnInPlace(angle=-360, turnSpeedPct=100, then=Stop.BRAKE)
    # br.WaitForMillis(5000)
    # br.DriveDistance(distance=220)
    # br.DriveAndSteerDist(dist=1000, turnRate=10, useGyro=False)
    # br.robot.drive(30, 0)
    # br.robot.drive(speed=600, turn_rate=0)
    # br.WaitForMillis(5000)
    # br.robot.drive(0,0)
    # br.GyroDriveImproved(5, -5, useGyro=False)

    # br.MoveRightAttachmentMotorUntilStalled(speedPct=-100, torquePct=10)


# If running this program directly (not from the master program), this is
# how we know it is running directly. In which case, this method will
# create a BaseRobot and run the Run(br) method above.
# In other words, keep these three lines at the bottom of your code and
# everything will be fine.
if __name__ == "__main__":
    br = BaseRobot()
    Run(br)
