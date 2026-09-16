# ISM3232 - Module 2: zsh Navigation and File Operations

## Commands Practiced

| Command        | What it does                            |
|----------------|-----------------------------------------|
| pwd            | Prints the current working directory    |
| ls             | Lists visible files and folders         |
| ls -la         | Lists all files including hidden ones   |
| cd ..          | Moves up one directory level            |
| tree           | Displays directory structure            |
| touch          | Creates a new empty file                |
| cat            | Displays file contents in the terminal  |
| echo           | Prints text or writes output to a file  |
| cp             | Copies files                            |
| mv             | Moves or renames files                  |
| rm             | Deletes files                           |
| code           | Opens VS code                           |

## AI Use Statement
I did not use AI for this lab.


## Week 3: Virtual Environments and .zshrc

| Command | What it does |
|---|---|
| `python3 -m venv .venv` | Creates a new isolated Python virtual environment |
| `source .venv/bin/activate` | Activates the virtual environment |
| `which python3` | Checks path to confirm active Python executable location |
| `pip list` | Lists all installed Python packages |
| `pip install pytest ruff` | Installs specified packages into the active environment |
| `pip freeze > requirements.txt` | Exports installed package dependencies into a requirements file |
| `pip install -r requirements.txt` | Installs dependencies listed in `requirements.txt` |
| `echo '.venv/' > .gitignore` | Creates `.gitignore` entries to exclude files from Git tracking |
| `deactivate` | Exits the active virtual environment |
| `ll` | Runs `ls -la` to list all files |
| `c` | Runs `clear` to clear the terminal screen |
| `py` | Runs `python3` |
| `gs` | Runs `git status` |
| `ga` | Runs `git add .` to stage all changes |
| `gcmsg` | Runs `git commit -m` to commit staged changes |
| `gp` | Runs `git push` |
| `gl` | Runs `git log --oneline` |
| `tree2` | Runs `tree -L 2` to display directory structure up to 2 levels deep |
| `mkcd` | Creates a directory and enter it immediately |
