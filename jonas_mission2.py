from base_robot import *


def Run(br: BaseRobot):
    # br.WaitForButton(Button.LEFT)
    # # Drive to Chicken
    # br.GyroDrive(350, 600)
    # # Release Mechanism
    # br.GyroDrive(55, 50)
    # # Wait 10 Seconds
    # br.WaitForMillis(4000)
    # # Drive Back
    # br.GyroDrive(-450, 600)
    # PICK UP PERSON NOT IN USE
    # br.WaitForButton(Button.LEFT)
    # br.GyroDrive(350, 600)
    # br.GyroTurn(180)
    # br.GyroDrive(400, -600)
    # Deliver People
    br.WaitForButton(Button.LEFT)
    # Drive up
    br.GyroDrive(850, speed=977, then=Stop.BRAKE)
    # Drive back
    br.GyroDrive(-150, speed=977, then=Stop.BRAKE)
    br.GyroTurn(60)
    br.GyroDrive(-200, speed=977, then=Stop.BRAKE)
    # Missions 5+6
    # br.GyroDrive(250, then=Stop.BRAKE)
    # br.GyroTurn(90)
    br.GyroDrive(300, speed=977, then=Stop.BRAKE)
    br.leftAttachmentMotor.run_time(1000, 1000, wait=True)
    # wait(250)  #
    br.GyroDrive(-100, 977)
    # br.Curve(-200, 60)
    # br.GyroDrive(-600, 977)
    # Uncomment
    # br.GyroDrive(-200, then=Stop.BRAKE)
    br.GyroTurn(-80)
    br.robot.use_gyro(False)
    br.robot.straight(-850, Stop.BRAKE, True)
    br.robot.use_gyro(True)
    # ^ uncomment
    # br.WaitForButton(Button.LEFT)
    # br.GyroDrive(500)
    # br.GyroDrive(-500)


if __name__ == "__main__":
    br = BaseRobot()
    Run(br)
