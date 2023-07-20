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

tasks.json holds the settings for vscode tasks, which is how vscode can run shell programs. The only task configured here is to upload and run the current file. For this to work, a user environment variable will need to be set to define the robot name. The variable name will be `robotName` and the value should be the robot name.

~~~json
{
    "version": "2.0.0",
    "tasks": [
        {
        "label": "Run on robot",
        "type": "shell",
        "command": "pybricksdev.exe",
        "args": [
            "run",
            "ble",
            "--name",
            "${env:robotName}",
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
![](../help/images/EnvironmentVariables.png)
