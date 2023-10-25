from base_robot import *

# Add good comments, such as what the mission is supposed to do,
# how to align the robot in home, any initial starting instructions,
# such as how it should be loaded with anything, arm positions, etc.


# When we run this program from the master program, we will call this
# "Run(br)" method.
def Run(br: BaseRobot):
     br.GyroDrive(420)  # drive 420 mm
     br.GyroTurn(-50)  # turn -50 degrees
     br.GyroDrive(700)  # drive 700 mm
     br.GyroTurn(20)  # turn 20 degrees 

     # enter the museum
     br.GyroDrive(65)  # drive 700 mm
     br.GyroDrive(-255)  # drive -240 mm

     # Drive to skateboard
     br.GyroTurn(-37)  # turn -37 degrees
     br.GyroDrive(540)  # drive 480 mm
     br.GyroTurn(40)  # drive 40 mm

     # enter the skateboard
     br.GyroDrive(170)
     br.rightAttachmentMotor.run_angle(1000, 300)
     br.GyroDrive(-200)
     br.GyroTurn(45) 
     br.Curve(radius=-350, angle=-100)
     br.GyroDrive(-500, -977)

#     base to popcorn
#     br.WaitForButton(Button.LEFT)
#     br.GyroDrive(50) # drive 50 mm


#         br.leftAttachmentMotor.run_angle(-1000, 300)
#     br.GyroDrive(-100)  # drive150 mm

# br.GyroTurn(80)  # turn 80 degrees
# br.GyroDrive()
# br.leftAttachmentMotor.run_angle(1000, 300)
# br.GyroDrive(-50)  # drive -50 mm


# If running this program directly (not from the master program), this is
# how we know it is running directly. In which case, this method will
# create a BaseRobot and run the Run(br) method above.
# In other words, keep these three lines at the bottom of your code and
# everything will be fine.
if __name__ == "__main__":
    br = BaseRobot()
    Run(br)
