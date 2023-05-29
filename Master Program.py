import base_robot
import subprocess

br = base_robot.BaseRobot()

##########################################
##########################################
###            MASTER PROGRAM          ###
##########################################
##########################################


# Run the missions depending on what color is seen here
validColorList = [base_robot.Color.BLUE,
                  base_robot.Color.CYAN,
                  base_robot.Color.GREEN,
                  base_robot.Color.MAGENTA,
                  base_robot.Color.ORANGE,
                  base_robot.Color.RED,
                  base_robot.Color.VIOLET,
                  base_robot.Color.WHITE,
                  base_robot.Color.NONE]
while True:
    while True:
        # Inner loop checks to see what color attachment is installed
        # and provide visual feedback
        # It then checks to see if a button is pressed. If it is,
        # break out of the loop and execute the mission associated
        # with that color
        curColor = br.GetAttachmentColor()
        if curColor in validColorList:
            br.hub.display.icon(base_robot.Icon.HAPPY)
            br.hub.light.on(curColor)
        else:
            br.hub.display.icon(base_robot.Icon.SAD)
            br.hub.light.off()

        if base_robot.Button.RIGHT in br.hub.buttons.pressed():
            break

        if base_robot.Button.LEFT in br.hub.buttons.pressed():
            break

    # Outer loop. When we get here, it's because we pressed a button
    # and broke out of the inner loop. Now execute the mission for the
    # color of the attachment. When the mission is done executing,
    # loop back into the inner loop and do it all again
    if (br.GetAttachmentColor() == base_robot.Color.GREEN):
        subprocess.run(["python", "Skip-Mission1.py"]) 
        br.WaitForSeconds(.5)

