import base_robot

# When we run this program from the master program, we will call this 
# "Run(br)" method.
def Run(br: base_robot.BaseRobot):
    br.DriveTank(20, 20, 1, "sec")
    br.leftAttachmentMotor.run_angle(200, 180)


# If running this program directly (not from the master program), this is
# how we know it is running directly. In which case, this method will
# create a BaseRobot and run the Run(br) method above.
if __name__ == '__main__':
    br = base_robot.BaseRobot()
    Run(br)
