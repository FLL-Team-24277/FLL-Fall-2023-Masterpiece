from cleveland_base_robot import *

br = BaseRobot()

while True: 
    curHsv = br.colorSensor.hsv(True)
    curCol = br.colorSensor.color()
    print(str(curHsv) + ": " + str(br.myColor2DefaultColorDict[curCol]))
    # curColor = br.colorSensor.color()
    # print(curColor)
    # br.hub.light.on(br.myColor2DefaultColorDict[curColor])

    # print (str(curCol))
    wait(500)
