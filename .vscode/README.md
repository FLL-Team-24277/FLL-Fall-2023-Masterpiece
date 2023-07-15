There are two settings files in this ".vscode" directory, but only one is tracked in the repository.
settings.json holds the workspace settings. The most important lines in it hide certain files from the project explorer. This simplifies the view for the team members so they will only see the files they need.
~~~json
{
    "files.exclude": {
        "**/.git": true,
        "**/.svn": true,
        "**/.hg": true,
        "**/CVS": true,
        "**/.DS_Store": true,
        "**/Thumbs.db": true,
        "**/.venv/" : true,
        "**/.vscode/" : true,
        "**/__pycache__/": true,
        "**/.gitignore" : true,
        "**/README.md" : true,
        "base_robot.py" : true,
        "requirements.txt" : true
    }, 
    "terminal.intgrated.shell.windows": "C:\\Program Files\\Git\\bin\\bash.exe"
}
~~~

To do that, we hide the files and folders above. Most team members will not need to make any changes to the settings.json file.

tasks.json holds the settings for vscode tasks, which is how vscode can run shell programs. The only task configured here is to upload and run the current file. This file will need to be edited for each team member so that it will run for their robot. Simply replace the XXX with the name of their robot. Once you save this file, you should be able to press ctrl-shift-l to launch the task.

~~~json
{
    "version": "2.0.0",
    "tasks": [
        {
        "label": "Run on XXX",
        "type": "shell",
        "command": "pybricksdev.exe",
        "args": [
            "run",
            "ble",
            "--name",
            "XXX",
            "${file}"
            ],
            "problemMatcher": {
                "owner": "python",
                "fileLocation": [
                    "absolute"
                ],
                "pattern": {
                    "regexp": "^(.*)File(.*)(C:(.*)\\.py)(.*)(line(\\s*))([0-9]+),",
                    "file": 3,
                    "line": 8
                }
            },
            "presentation": {
                "echo": true,
                "reveal": "always",
                "focus": false,
                "panel": "shared",
                "showReuseMessage": false,
                "clear": true,
                "revealProblems": "onProblem"
            }
        }
    ]
}

~~~
