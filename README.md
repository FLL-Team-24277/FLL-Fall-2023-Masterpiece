# Master-Program-Fall-2023

11 June 2023: As of right now, a lot of the code on this repo is missing while the team is working on new code this summer. Keep on watching and by fall there should be working code up here.

This is where all of the team code and master program will live for the Fall 2023 Masterpiece FLL Season. We will use [pybricks libraries](https://github.com/pybricks) and VS code, and git/github for version control.

Very helpful page here: https://pybricks.com/projects/tutorials/dev/tools/vscode/

How to use:

1. Each team member creates their own github account. REMINDER: Be sure to use an email account that they can check at school (github emails may be blocked). Recommend taking a few extra minutes to set up two-factor authentication. Github will be moving to mandatory 2FA in early 2024, so may as well do it now.
2. Add each account as a collaborator for this project here: https://github.com/FLL-Team-24277/Master-Program-Fall-2023/settings/access (instructions here: https://docs.github.com/en/account-and-profile/setting-up-and-managing-your-personal-account-on-github/managing-access-to-your-personal-repositories/inviting-collaborators-to-a-personal-repository)
3. The team member will need to confirm and accept the invitation. At that point they can push updates to the project.
4. In VS Code clone this repository. https://github.com/FLL-Team-24277/Master-Program-Fall-2023.git Save it somewhere in their documents folder. Be aware though that if the folder is "watched" under OneDrive, the folder will be cloned to other computers with the same OneDrive account. This creates probles for the python virtual environment because really each physical computer needs their own python environment. It might be a good idea to put the folder somewhere OUTSIDE of the OneDrive watch folder structure. You might think you would want to have the security and file replication of OneDrive, but we'll be doing all of that with Github, so it's not a big deal.
5. Add a python virtual environment. `Ctrl-Shift-P` > `Python: Create Environment`
6. `pip install pybricks==3.3.0a5`
7. `pip install pybricksdev`
8. Create a new python file, named `teamMemberName-test-mission.py`, copy and paste the code below, and save it.
9. Commit the changes, and push. It will probably prompt for github registration/login and then sync all files. This link may help: https://pages.nist.gov/git-novice-MSE/08-collab/
10. Install pybricks on each robot at https://beta.pybricks.com/. Name the robot at this time. Avoid spaces and special characters in the robot name. Put a label sticker on the top of the robot with the robot name.
11. Edit `.vscode\tasks.json` to run `pybricksdev.exe`, which uploads programs to the Spike hub. https://github.com/pybricks/pybricksdev The only changes needed should be to change the label and command argument to match the robot's name.
12. Turn the robot on and ensure the keyboard shortcut `ctrl-h` runs the command, which should also run their program. Also, `Ctrl-Shift-P` > `Tasks: Run task` should pop up a menu with the correct entry.
13. To use a master program to organize and run individual missions, take a look at the [master_program.py](https://github.com/FLL-Team-24277/Master-Program-Fall-2023/blob/main/Master%20Program.py) and the [Skip_mission1_ready_for_master.py](https://github.com/FLL-Team-24277/Master-Program-Fall-2023/blob/main/Skip_Mission1_ready_for_master.py). As you can see, the mission file is very slightly more complicated, and the kids may prefer the simplicity of the "non-master" mission programs. It isn't hard to convert one format to the other, so it isn't a big deal either way.



Example code for test program

~~~
import base_robot

br = base_robot.BaseRobot()
br.Drive(10) # 10cm
~~~
