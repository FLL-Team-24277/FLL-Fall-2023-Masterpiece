from cleveland_base_robot import *

br = BaseRobot()

while True: 
    curHsv = br.colorSensor.hsv(True)
    curCol = br.colorSensor.color()
    print(str(curHsv) + ": " + str(br.myColor2DefaultColorDict[curCol]))
    wait(500)
