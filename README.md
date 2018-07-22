parking_lot code solution

Requirements:
Python Version 3.6

Python packages needed:
pip
pipenv
pybuilder

Tests:
Tests are in the src/main/unittest folder

Tests are executed automatically with pybuilder

Execution:
Environment settings must be setup first by calling bin/setup.sh
This is call install dependencies for this solution,
setup the environment, run the pybuilder and unit tests

Now to run the solution, for file and interactive mode,
execute bin/parking_lot.sh [filename].
If [filename] is passed, the code flow reads from the input command file
and executes the commands in order.
If [filename] is not passed, the interactive shell mode is setup, and the 
user has to pass the commands separately.
