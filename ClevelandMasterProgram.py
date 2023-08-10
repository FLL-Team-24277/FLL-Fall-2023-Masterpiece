from base_robot import *
import clev_test

br = BaseRobot()

pressed = []
col = br.colorSensor.color()

while True:
    while True:
        col = br.colorSensor.color()
        # print(col)
        if col == Color.SENSOR_NONE:  # no color detected
            br.hub.display.icon(Icon.SAD)
            br.hub.light.on(Color.RED)
        else:
            br.hub.display.icon(Icon.HAPPY)
            br.hub.light.on(br.myColor2DefaultColorDict[col])

        wait(250)
        pressed = br.hub.buttons.pressed()
        if Button.LEFT in pressed:
            break

    if col == Color.SENSOR_GREEN:
        clev_test.Run(br)

    if col == Color.SENSOR_BLUE:
        print("Launching the Blue mission")
