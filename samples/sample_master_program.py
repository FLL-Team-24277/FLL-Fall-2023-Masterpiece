from base_robot import *

# Import missions
import sample_mission1
import sample_mission2
import sample_mission3
import sample_mission4

br = BaseRobot()

pressed = []
while True:
    
    while True:
        col = br.colorSensor.color()
        # The first thing this program does is it detects what color is
        # being help up to the robot color sensor.
        # If no color is detected, then it will display a sad face
        if col == Color.SENSOR_NONE:
            br.hub.display.icon(Icon.SAD)
            br.hub.light.on(Color.RED)
        else:  #  If a color is detected, then it will display a happy face
            br.hub.display.icon(Icon.HAPPY)
            br.hub.light.on(br.myColor2DefaultColorDict[col])

        wait(50)
        pressed = br.hub.buttons.pressed()
        #  When the left button is pressed, it will break out of the loop
        if Button.LEFT in pressed:
            break
        if Button.BLUETOOTH in pressed:
            # If the Bluetooth button is pressed, it will run the motors fast for
            # cleaning
            if br.leftDriveMotor.speed() == 0:
                br.leftDriveMotor.run(5000)
                br.rightDriveMotor.run(5000)
            else:
                br.leftDriveMotor.run(0)
                br.rightDriveMotor.run(0)

    # It will now launch the mission coresponding to the color
    # If detected color is Red, then run RJ's & Cleveland's mission
    if col == Color.SENSOR_BLUE:
        sample_mission1.Run(br)
        # If detected color is Blue, then run Sample Mission 1
    if col == Color.SENSOR_ORANGE:
        sample_mission2.Run(br)
        # If detected color is Orange, then run Sample Mission 2
    if col == Color.SENSOR_YELLOW:
        sample_mission2.Run(br)
        # If detected color is Yellow, then run Sample Mission 2
    if col == Color.SENSOR_GREEN:
        sample_mission3.Run(br)
        # If detected color is Green, then run Sample Mission 3
    if col == Color.SENSOR_RED:
        sample_mission4.Run(br)
        # If detected color is Red, then run Sample Mission 4