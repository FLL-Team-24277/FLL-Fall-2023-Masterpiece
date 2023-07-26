from cleveland_base_robot import *
import clev_test

br = BaseRobot()

def SetLightToState(robot, state):
    if (state==True):
        br.hub.light.on(Color.RED)
    else:
        br.hub.light.off

detectableColors=(
    # Color.BLUE, # Mission 1
    # Color.GREEN,
    Color.NONE,
    Color.RED,
    Color.YELLOW,
    Color.WHITE,
    Color.GRAY
    )
br.colorSensor.detectable_colors(detectableColors)
pressed=[]
col=br.colorSensor.color()
state = True

while True:
    while True: 
        col=br.colorSensor.color()
        # print(color)
        if (col==Color.NONE):
            br.hub.display.icon(Icon.SAD)
            SetLightToState(br, state)
            state =  not state
            print(str(state))
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
    

