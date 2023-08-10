from base_robot import *
import clev_test

br = BaseRobot()

pressed = []
col = br.colorSensor.color()

while True:
    while True:
        col = br.colorSensor.color()
        # The first thing this program does is it detects what color is being help up to the robot
        if col == Color.SENSOR_NONE:  #  If no color is detected, then it will display a sad face
            br.hub.display.icon(Icon.SAD)
            br.hub.light.on(Color.RED)
        else: #  If a color is detected, then it will display a happy face
            br.hub.display.icon(Icon.HAPPY)
            br.hub.light.on(br.myColor2DefaultColorDict[col])

        wait(250)
        pressed = br.hub.buttons.pressed()
        if Button.LEFT in pressed: #  When the left button is pressed, it will break out of the loop
            break

    if col == Color.SENSOR_GREEN: # It will now launch the mission coresponding to the color
        clev_test.Run(br)

    if col == Color.SENSOR_BLUE:
        print("Launching the Blue mission")
