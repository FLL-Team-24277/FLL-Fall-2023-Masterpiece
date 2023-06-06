import base_robot
import Skip_Mission1_ready_for_master


br = base_robot.BaseRobot()

##########################################
##########################################
###            MASTER PROGRAM          ###
##########################################
##########################################


# Run the missions depending on what color is seen here
validColorList = [
    base_robot.Color.BLUE,  # mission one
    base_robot.Color.CYAN,  # mission two
    base_robot.Color.GREEN,  # mission three
    base_robot.Color.MAGENTA,
    base_robot.Color.ORANGE,
    base_robot.Color.RED,
    base_robot.Color.VIOLET,
    base_robot.Color.WHITE,
]
while True:
    while True:
        # Inner loop checks to see what color attachment is installed
        # and provide visual feedback
        # It then checks to see if the left button is pressed. If it is,
        # break out of the loop and execute the mission associated
        # with that color
        curColor = br.GetAttachmentColor()
        if curColor in validColorList:
            br.hub.display.icon(base_robot.Icon.HAPPY)
            br.hub.light.on(curColor)
        else:
            br.hub.display.icon(base_robot.Icon.SAD)
            br.hub.light.off()

        # The right button is the abort button. If it is being pressed,
        # don't execute any other programs. Just stay right here.
        while base_robot.Button.RIGHT in br.hub.buttons.pressed():
            pass

        # The left button is the launch button. If it is pressed, break
        # out of the inner loop and execute the mission associated with
        # the color detected.
        if base_robot.Button.LEFT in br.hub.buttons.pressed():
            break

    # Outer loop. When we get here, it's because we pressed the left button
    # and broke out of the inner loop. Now execute the mission for the
    # color of the attachment. When the mission is done executing,
    # loop back into the inner loop and do it all again
    #
    # Note the imports above must inclcude the python module
    if br.GetAttachmentColor() == base_robot.Color.GREEN:
        Skip_Mission1_ready_for_master.Run(br)
