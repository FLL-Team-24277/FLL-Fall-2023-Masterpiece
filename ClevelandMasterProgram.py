from cleveland_base_robot import *
import clev_test

br = BaseRobot()

detectableColors=(
    Color.BLUE, # Mission 1
    Color.GREEN,
    Color.NONE,
    Color.RED,
    Color.YELLOW,
    Color.WHITE,
    Color.GRAY
    )
br.colorSensor.detectable_colors(detectableColors)
pressed=[]
col=br.colorSensor.color()

while True:
    while True: 
        col=br.colorSensor.color()
        # print(color)
        if (col==Color.NONE):
            br.hub.display.icon(Icon.SAD)
            br.hub.light.blink(Color.RED, [1000, 1000])
        else:
            br.hub.display.icon(Icon.HAPPY)
            br.hub.light.on(col)
        
        wait(100)
        pressed=br.hub.buttons.pressed()
        if (Button.LEFT in pressed):
            break
    
    if(col==Color.RED):
        clev_test.Run(br)

    if(col==Color.BLUE):
        print("Launching the blue mission")
    

