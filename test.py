from base_robot_testing import *

# Add good comments, such as what the mission is supposed to do,
# how to align the robot in home, any initial starting instructions,
# such as how it should be loaded with anything, arm positions, etc.


# When we run this program from the master program, we will call this
# "Run(br)" method.
def Run(br: BaseRobot):
    # Your mission code goes here, step-by-step
    # It MUST be indented just like the lines below
    # br.MoveRightAttachmentMotor(speed=950, angle=9000, wait=True)
    # br.robot.settings(straight_speed=475, straight_acceleration=9775)
    # br.robot.straight(distance=5000)
    # br.WaitForMillis(500)
    # br.robot.drive(speed=500, turn_rate=0)
    # br.WaitForMillis(10000)
    # br.robot.drive(speed=0, turn_rate=0)
    # br.WaitForMillis(500)
    # br.DriveUntilStalled(speed=700, turn_rate=0, stall=100, useGyro=False)
    # br.rightDriveMotor.run(speed=1500)
    # br.leftDriveMotor.run(speed=1500)
    # br.WaitForMillis(4000)
    # br.leftDriveMotor.run(speed=0)
    # br.rightDriveMotor.run(speed=0)
    # br.WaitForMillis(500)
    # br.GyroDrive(distance=2000, speed=977)
    # br.WaitForMillis(1000)
    # br.DriveAndSteer(speed=977, turnrate=0, time=4000)
    # br.WaitForMillis(1000)
    # br.UseGyro(True)
    # br.robot.reset()
    # br.robot.drive(speed=1000, turn_rate=0)
    # while br.robot.distance() < 2000:
    #     wait(50)

    # br.robot.drive(speed=0, turn_rate=0)

    # br.WaitForMillis(1000)

    # br.UseGyro(False)
    # br.robot.reset()
    br.robot.distance_control.limits(speed=977, acceleration=733, torque=560)
    br.GyroDrive(speed=977, distance=1500)
    br.WaitForMillis(100)

    # br.robot.drive(speed=1000, turn_rate=0)
    # while br.robot.distance() < 2000:
    #     wait(50)

    # br.robot.drive(speed=0, turn_rate=0)

    # br.WaitForMillis(1000)

    # br.DriveUntilStalled2(
    #     targetSpeed=977,
    #     turn_rate=0,
    #     stallSpeedPct=95,
    #     useGyro=False,
    #     maxTorque=1,
    # )
    # br.WaitForMillis(1000)
    # br.UseGyro(True)
    # br.DriveAndSteerDist(distance=1650, speed=150, turn_rate=20)
    # br.UseGyro(True)
    # br.MoveRightAttachmentMotor(angle=3000)

    # br.GyroDrive(distance=680, speed=500)
    # br.WaitForMillis(500)  # half second
    # br.GyroTurn(65)  # turn to the right 85 degrees
    # br.GyroDrive(distance=300)  # use the default speed
    # br.leftAttachmentMotor.run_angle(200, 180)  # speed 200, 180 degrees
    # br.rightAttachmentMotor.run_angle(200, 180)  # speed 200, 180 degrees


# If running this program directly (not from the master program), this is
# how we know it is running directly. In which case, this method will
# create a BaseRobot and run the Run(br) method above.
# In other words, keep these three lines at the bottom of your code and
# everything will be fine.
if __name__ == "__main__":
    br = BaseRobot()
    Run(br)
