# Master-Program-Fall-2023

This is where all of the team code and master program will live for the Fall 2023 Masterpiece FLL Season.

How to use:

1. Each team member creates their own github account. REMINDER: Be sure to use an email account that they can check at school (github emails may be blocked).
2. Add each account as a collaborator for this project here: https://github.com/FLL-Team-24277/Master-Program-Fall-2023/settings/access (instructions here: https://docs.github.com/en/account-and-profile/setting-up-and-managing-your-personal-account-on-github/managing-access-to-your-personal-repositories/inviting-collaborators-to-a-personal-repository)
3. The team member will need to confirm and accept the invitation. At that point they can push updates to the project.
4. In VS Code clone this repository. https://github.com/FLL-Team-24277/Master-Program-Fall-2023.git Save it somewhere in their documents folder
5. Add a python virtual environment. Ctrl-Shift-P > Python: Create Environment
6. Install the baseRobotLibrary (and pybricks and pybricksdev as a dependencies) pip install /path/to/wheelfile.whl (use a thumb drive)
7. Create a new python file, named "teamMemberName-test-mission.py", add a comment or two, and save it.
8. Commit the changes, and push. It will probably prompt for github registration/login and then sync all files. This link may help: https://pages.nist.gov/git-novice-MSE/08-collab/
9. Edit .vscode\tasks.json to run pybricksdev.exe, which uploads programs to the Spike hub. https://github.com/pybricks/pybricksdev The ony changes needed should be to change the label and command argument to match the robot's name.
10. Ensure the keyboard shortcut ctrl-h runs the command. Also, ctrl-shift-P > Tasks: Run task should pop up a menu with the correct entry.
11. Ensure pybricks and pybricksdev are installed. If not, use pip install pybricks (or pybricksdev), however they should have installed along with the baserobot library, so double-check that.
