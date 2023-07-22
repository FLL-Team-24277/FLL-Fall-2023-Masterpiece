from cleveland_base_robot import *

br = BaseRobot()

detectableColors=(
    Color.BLUE, # Mission 1
    # Color.GREEN,
    Color.ORANGE, # mission 2
    Color.NONE,
    # Color.RED,
    # Color.GRAY
    )
br.colorSensor.detectable_colors(detectableColors)
pressed=[]
while True: 
    color=br.colorSensor.color()
    print(color)
    wait(100)
    pressed=br.hub.buttons.pressed()
    if (Button.LEFT in pressed):
        print("I see blue and the button is pressed!!!")