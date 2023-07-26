from cleveland_base_robot import *
import clev_test

br = BaseRobot()

pressed=[]
col=br.colorSensor.color()

while True:
    while True: 
        col=br.colorSensor.color()
        print(col)
        if (col==Color.NONE):
            br.hub.display.icon(Icon.SAD)
        else:
            br.hub.display.icon(Icon.HAPPY)
            br.hub.light.on(br.myColor2DefaultColorDict[col])
            print(col)
        
        wait(100)
        pressed=br.hub.buttons.pressed()
        if (Button.LEFT in pressed):
            break
    
    if(col==br.myCustomColors[0]): #Green
        clev_test.Run(br)

    if(col==br.myCustomColors[1]): # Red
        print("Launching the Red mission")
    

