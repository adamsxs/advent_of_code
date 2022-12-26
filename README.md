# advent_of_code
Solutions for [Advent of Code 2022](https://adventofcode.com) with Michael Mayer

# Setting up the Virtual Environment
In your terminal:
Creat the virtual environment
```commandline
python -m venv ./venv
```
Activate it, and check that you're using the environment
```commandline
source ./venv/bin/activate
which pip
which python
```
Install dependencies. The `python -m` bit before `pip ..` just routes the execution through our python executable, it's a little safer:
```
python -m pip install -r requirements.txt
```
Update the environment:
```commandline
pip freeze > requirements.txt
```
Deactivate the environment:
```commandline
deactivate
```