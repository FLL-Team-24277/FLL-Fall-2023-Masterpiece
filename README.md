# FLL Team 24277  
##  Introduction

We are not "giving away solutions" here. If you are looking for mission solutions, you'll just have to figure them out yourself :) [Read our statement on the FLL "Discovery" core value here.](https://github.com/FLL-Team-24277/Master-Program-Fall-2023/blob/main/help/discovery.md)

The instructions below will get team members up and running for FLL in a team collaboration environment using [pybricks libraries](https://github.com/pybricks), writing programs with Visual Studio Code, and using git/github for version control. The instructions are not perfect, and you will probably have some troubleshooting and adjustments along the way.

Additionally, this is where all of the team code and master program will live for the Fall 2023 Masterpiece FLL Season.

Very helpful page here about how to use pybricks with VS Code: https://pybricks.com/projects/tutorials/dev/tools/vscode/

[About our Robot](https://github.com/FLL-Team-24277/FLL-Fall-2023-Masterpiece/blob/main/help/robot.md)

## Instructions

1. Install [necessary software](https://github.com/FLL-Team-24277/Master-Program-Fall-2023/blob/main/help/config/Software.md).
2. Each team member creates their own github account. REMINDER: Be sure to use an email account that they can check at school (github emails may be blocked). Recommend taking a few extra minutes to set up two-factor authentication. Github will be moving to mandatory 2FA in late 2023, so may as well do it now. Also recommend that the team member keep that github page open and logged in while completing these instructions because you will need it for authentication in step 9 below. Remind them to not forget their password!
3. Add each account as a collaborator for this project [here](https://github.com/FLL-Team-24277/Master-Program-Fall-2023/settings/access). Instructions [here](https://docs.github.com/en/account-and-profile/setting-up-and-managing-your-personal-account-on-github/managing-access-to-your-personal-repositories/inviting-collaborators-to-a-personal-repository).
4. The team member will need to confirm and accept the invitation. At that point they can push updates to the project.
5. In VS Code add the [necessary extensions](https://github.com/FLL-Team-24277/Master-Program-Fall-2023/blob/main/help/config/VS%20Code%20Plugins%20for%20FLL%20Teams.md) and restart VS Code. When you restart, you should have the option to Clone a Repository. Clone this repository: https://github.com/FLL-Team-24277/Master-Program-Fall-2023.git Save it somewhere on their computer.
6. Add a python virtual environment. `Ctrl-Shift-P` > `Python: Create Environment`. Just use the defaults. Open a new terminal with ``ctrl-shift-` `` or `Ctrl-Shift-P` > `Create Terminal` and make sure it is in the python virtual environment. It will start with a green "(.venv)". If there are executionPolicy errors, you will need to elevate the permissions for Powershell. Instructions [here](https://tecadmin.net/powershell-running-scripts-is-disabled-system/) (copied [here](https://github.com/FLL-Team-24277/Master-Program-Fall-2023/blob/main/help/config/executionPolicyError.md)), but basically just run `Set-ExecutionPolicy RemoteSigned` in an Administrative PowerShell.
7. `pip install -r .\requirements.txt` (should do the same thing as `pip install pybricks==3.3.0a5`, `pip install pybricksdev` and `pip install black`). Theoretically the virtual environment should read the requirements.txt file and install those libraries automatically, but I haven't tested that yet. Check to see what is installed with `pip list`.
8. Create a new python file, named `teamMemberName-test-mission.py`, copy and paste the code below, and save it, but don't try to run it just yet. Wait for step 13 below. Note that after saving the file, the python Black Formatter should correct the "incorrect" spacing around the equals signs and commas.
9. Commit the changes, and push. It will probably prompt for github registration/login and then sync all files. This link may help: https://pages.nist.gov/git-novice-MSE/08-collab/. It may also ask you to set your git username and email. Open a terminal and run these two commands to set your username and email `git config --global user.name "FIRST_NAME LAST_NAME"`; and `git config --global user.email "MY_NAME@example.com"`
10. Install pybricks on each robot at https://beta.pybricks.com/. If the computer has never connected to a pybricks hub, you will probably need to manually install the USB drivers, which will require the use of the windows Device Manager. To run device manager as an admin, run a powershell as an administrator, then type devmgmt.msc. Then complete the usual steps. Name the robot at this time. Avoid spaces and special characters in the robot name. Put a label sticker on the top of the robot with the robot name.
11. Create a User environment variable for the robot name. Set the variable `robotName` to the name of the robot. This should allow the keyboard binding and tasks to recognize the robot by name. Restart VS Code and open a new terminal and then test it with `echo $env:robotName`.
12. Last step, I promise! Add a keyboard shortcut to run the programs that we write. `Ctrl-Shift-P` > `Preferences: Open Keyboard Shortcuts (JSON)`. Edit the JSON to add the keyboard shortcut to run the task. Paste in the code below at the bottom of keybindings.json.
13. **RUN OUR PROGRAM!** Turn the robot on and ensure the keyboard shortcut `ctrl-shift-L` runs the command, which should also run their program. Also, `Ctrl-Shift-P` > `Tasks: Run task` should pop up a menu with the correct entry. Watch the terminal and make sure the robot name is correct. If not, recheck that you completed step 11 correctly.
14. Finally, to use a master program to organize and run individual missions, take a look at the [master_program.py](https://github.com/FLL-Team-24277/Master-Program-Fall-2023/blob/main/Master%20Program.py) and the [Skip_mission1_ready_for_master.py](https://github.com/FLL-Team-24277/Master-Program-Fall-2023/blob/main/Skip_Mission1_ready_for_master.py). As you can see, the mission file is ever-so-slightly more complicated, but the kids may prefer the simplicity of the "non-master" mission programs. It isn't hard to convert one format to the other, so it isn't a big deal either way.

## Example code for test program

~~~python
from base_robot import *

# Add good comments, such as what the mission is supposed to do,
# how to align the robot in home, any initial starting instructions,
# such as how it should be loaded with anything, arm positions, etc.

# Weird spacing is intentional. Should be auto-corrected by Black formatter after saving

#When we run this program from the master program, we will call this
# "Run(br)" method.
def   Run(br: BaseRobot)   :
    #   Your mission code goes here, step-by-step
    #It MUST be indented just like the lines below
    br.GyroDrive (  130  )  #130 mm
    br.WaitForMillis(500  )  # half second
    br.GyroTurn(85)  # turn to the right 85 degrees
    br.leftAttachmentMotor.run_angle(200,180)  # speed 200, 180 degrees


# If running this program directly (not from the master program), this is
# how we know it is running directly. In which case, this method will
# create a BaseRobot and run the Run(br) method above.
# In other words, keep these three lines at the bottom of your code and
# everything will be fine.
if __name__ == "__main__":
    br = BaseRobot()
    Run(br)
~~~


keybindings.json
~~~json
[
    {
        "key" : "ctrl+shift+l",
        "command" : "workbench.action.tasks.runTask",
        "args": "Run on robot"
    }
]
~~~
