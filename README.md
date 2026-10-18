# first for initializing git
  git init
# define configuration
  git config --global user.name "user.name"
  git config --global user.email "user.email"
# open vscode
  code .
# create new repository in github
# clote your repository in vscode
# create reqired folders
  create a folder named .env
  create a folder named .gitignore
  create a folder named python_version
  create a folder named .env.example
# .venv
  python -m venv .venv
# activate and deactivate .venv (create isolated environment for any version you want)
  .venv\Scripts\activate
  .venv\Scripts\activate
# check all python versions in your system
  where python
# to see what python version your .venv is using from
  python -c "import sys; print (sys.executable)"
# for installing all required libraries for specific project
  python -m pip install -r requirements.txt
# for creating requirements.txt
  python -m freeze > reqirements.txt
