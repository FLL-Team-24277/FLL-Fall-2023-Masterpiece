from cleveland_base_robot import *

br = BaseRobot()

while True: 
    curCol = br.colorSensor.hsv(True)
    print(str(br.colorSensor.color()) + ": " + str(curCol))
    # curColor = br.colorSensor.color()
    # print(curColor)
    # br.hub.light.on(br.myColor2DefaultColorDict[curColor])

    # print (str(curCol))
    wait(500)
