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
    br.DriveUntilStalled(speed=600, turn_rate=20, stall=75, useGyro=True)
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
