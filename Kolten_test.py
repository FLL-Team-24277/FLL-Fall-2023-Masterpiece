from base_robot import *

# Add good comments, such as what the mission is supposed to do,
# how to align the robot in home, any initial starting instructions,
# such as how it should be loaded with anything, arm positions, etc.

# Weird spacing is intentional. Should be auto-corrected by Black formatter after saving


# When we run this program from the master program, we will call this
# "Run(br)" method.
def Run(br: BaseRobot):
    #   Your mission code goes here, step-by-step
    # It MUST be indented just like the lines below
    # br.GyroDrive(130)  # 130 mm
    # br.WaitForMillis(500)  # half second
    # br.GyroTurn(85)  # turn to the right 85 degrees
    # br.leftAttachmentMotor.run_angle(200, 180)  # speed 200, 180 degrees
      br.GyroDrive(400, 400)
      br.leftAttachmentMotor.run_angle(100, 115)
      br.GyroDrive(-200, 200)
      
       




# If running this program directly (not from the master program), this is
# how we know it is running directly. In which case, this method will
# create a BaseRobot and run the Run(br) method above.
# In other words, keep these three lines at the bottom of your code and
# everything will be fine.
if __name__ == "__main__":
    br = BaseRobot()
    Run(br)
