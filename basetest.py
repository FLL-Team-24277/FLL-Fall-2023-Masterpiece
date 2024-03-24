from base_robot_testing import *

# Add good comments, such as what the mission is supposed to do,
# how to align the robot in home, any initial starting instructions,
# such as how it should be loaded with anything, arm positions, etc.


# When we run this program from the master program, we will call this
# "Run(br)" method.
def Run(br: BaseRobot):
    br.hub.display.number(0)
    br.WaitForButton(Button.RIGHT)
    br.TurnInPlace(45)

    br.hub.display.number(1)
    br.WaitForButton(Button.RIGHT)
    br.DriveDist(60)

    br.hub.display.number(2)
    br.WaitForButton(Button.RIGHT)
    br.WallFollowDist(160, 15)

    br.hub.display.number(3)
    br.WaitForButton(Button.RIGHT)
    br.Curve(radius=400, angle=15)

    br.hub.display.number(4)
    br.WaitForButton(Button.RIGHT)
    br.DriveMillis(800)

    br.hub.display.number(5)
    br.WaitForButton(Button.RIGHT)
    br.DriveUntilStalled(stallPct=25, speedPct=25)

    br.hub.display.number(6)
    br.WaitForButton(Button.RIGHT)
    br.MoveAttachmentMotorDegrees(br.rightAttachmentMotor, 360)

    br.hub.display.number(7)
    br.WaitForButton(Button.RIGHT)
    br.MoveAttachmentMotorMillis(br.leftAttachmentMotor, 2000)

    br.hub.display.number(8)
    br.WaitForButton(Button.RIGHT)
    br.MoveAttachmentMotorUntilStalled(
        br.rightAttachmentMotor, speedPct=100, torquePct=50
    )


# If running this program directly (not from the master program), this is
# how we know it is running directly. In which case, this method will
# create a BaseRobot and run the Run(br) method above.
# In other words, keep these three lines at the bottom of your code and
# everything will be fine.
if __name__ == "__main__":
    br = BaseRobot()
    Run(br)
