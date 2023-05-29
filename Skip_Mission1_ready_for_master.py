import base_robot
# br = base_robot.BaseRobot()

def Run(br: base_robot.BaseRobot):
    br.DriveTank(20, 20, 1, "sec")
    br.leftAttachmentMotor.run_angle(200, 180)


# If running this program directly (not from the master program), this is
# how we know it is running directly. If this program is called from
if __name__ == '__main__':
    br = base_robot.BaseRobot()
    Run(br)
# Run(base_robot.BaseRobot())