from base_robot import *

# This program is just for testing the values seen by the robot
# for different colors as seen by the light sensor, and what it
# is matched to by the BaseRobot class
br = BaseRobot()

print("current: " + str(br.hub.battery.current()))
print("voltage: " + str(br.hub.battery.voltage()))
print("Normal fully charged voltage is around 8200")
