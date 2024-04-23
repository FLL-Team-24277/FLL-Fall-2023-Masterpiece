from base_robot import *

br = BaseRobot()
br.Curve(800,- 90, Stop.NONE)
while(True):
    br.Curve(300,-180, Stop.NONE)
    br.GyroDrive(200, then=Stop.NONE)
    br.Curve(350,-90, Stop.NONE)

    br.Curve(200,-90, Stop.NONE)
    br.GyroDrive(300, then=Stop.NONE)