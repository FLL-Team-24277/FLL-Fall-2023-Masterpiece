# Master-Program-Fall-2023

This is where all of the team code and master program will live for the Fall 2023 Masterpiece FLL Season.

How to use:

1. Each team member creates their own github account. REMINDER: Be sure to use an email account that they can check at school (github emails may be blocked).
2. Add each account as a collaborator for this project here: https://github.com/FLL-Team-24277/Master-Program-Fall-2023/settings/access (instructions here: https://docs.github.com/en/account-and-profile/setting-up-and-managing-your-personal-account-on-github/managing-access-to-your-personal-repositories/inviting-collaborators-to-a-personal-repository)
3. The team member will need to confirm and accept the invitation. At that point they can push updates to the project.
4. In VS Code clone this repository. https://github.com/FLL-Team-24277/Master-Program-Fall-2023.git Save it somewhere in their documents folder
5. Add a python virtual environment. `Ctrl-Shift-P` > `Python: Create Environment`
6. `pip install pybricks==3.3.0a5`
7. `pip install pybricksdev`
8. Create a new python file, named `teamMemberName-test-mission.py`, copy and paste the code below, and save it.
9. Commit the changes, and push. It will probably prompt for github registration/login and then sync all files. This link may help: https://pages.nist.gov/git-novice-MSE/08-collab/
10. Install pybricks on each robot at https://beta.pybricks.com/. Name the robot at this time. Avoid spaces and special characters in the robot name. Put a label sticker on the top of the robot with the robot name.
11. Edit `.vscode\tasks.json` to run `pybricksdev.exe`, which uploads programs to the Spike hub. https://github.com/pybricks/pybricksdev The ony changes needed should be to change the label and command argument to match the robot's name.
12. Turn the robot on and ensure the keyboard shortcut `ctrl-h` runs the command, which should also run their program. Also, `Ctrl-Shift-P` > `Tasks: Run task` should pop up a menu with the correct entry.



Example code for test program

~~~
import base_robot

br = base_robot.BaseRobot()
br.Drive(10) # 10cm
~~~
