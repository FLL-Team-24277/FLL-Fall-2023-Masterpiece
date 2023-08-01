from cleveland_base_robot import *
import clev_test

br = BaseRobot()

pressed=[]
col=br.colorSensor.color()

while True:
    while True: 
        col=br.colorSensor.color()
        print(br.myColor2DefaultColorDict[col])
        if (col==Color(h=180, s=32, v=9)): # no color detected
            br.hub.display.icon(Icon.SAD)
            br.hub.light.on(Color.RED)
            # br.hub.light.blink(Color.RED, [100, 100])
        else:
            br.hub.display.icon(Icon.HAPPY)
            br.hub.light.on(br.myColor2DefaultColorDict[col])
            # print(col)
        
        wait(250)
        pressed=br.hub.buttons.pressed()
        if (Button.LEFT in pressed):
            break
    
    if(col==br.myCustomColors[0]): #Green
        clev_test.Run(br)

    if(col==br.myCustomColors[1]): # Red
        print("Launching the Red mission")
    

