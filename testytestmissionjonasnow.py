from base_robot_testing import *

# Add good comments, such as what the mission is supposed to do,
# how to align the robot in home, any initial starting instructions,
# such as how it should be loaded with anything, arm positions, etc.


# When we run this program from the master program, we will call this
# "Run(br)" method.
def Run(br: BaseRobot):
    br.robot.distance_control.limits(speed=977, acceleration=733, torque=560)
    br.robot.drive(977, -5)
    br.WaitForMillis(1000)
    br.rightAttachmentMotor.run_time(-977, 1000, wait=True)
    br.WaitForMillis(100)
    br.GyroDrive(distance=-400, speed=977)
    # br.GyroDriveForMillis(800, speed=-977)
    br.WaitForMillis(800)


# If running this program directly (not from the master program), this is
# how we know it is running directly. In which case, this method will
# create a BaseRobot and run the Run(br) method above.
# In other words, keep these three lines at the bottom of your code and
# everything will be fine.
if __name__ == "__main__":
    br = BaseRobot()
    Run(br)
