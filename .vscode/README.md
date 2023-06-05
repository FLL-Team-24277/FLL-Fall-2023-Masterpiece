There are two settings files in this ".vscode" directory.
settings.json is to hold teh workspace settings. The most important lines in it hide certain files from the project explorer. This simplifies the view for the team members so they will only see the files they need.
        "**/.venv/" : true,
        "**/.vscode/" : true,
        "**/.gitignore" : true,
        "**/README.md" : true,
        "base_robot.py" : true
To do that, we hide the files and folders above. Most team members will not need to make any changes to the settings.json file.

tasks.json holds the settings for vscode tasks, which is how vscode can run shell programs. The only task configured here is to upload and run the current file. This file will need to be edited for each team member so that it will run for their robot.
