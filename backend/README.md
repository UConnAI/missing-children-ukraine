# Backend Development Environment
This directory will host the code for backend development of the code for ukraine

***
## Setting up virtual enviornment
These are instructions for setting up the development enviornment. The enviornment will be working with python 3.9 as python 3.10 is still not available on lambdas runtimes. Finally it will be saved in a directory called env that will be saved in the backend directory.

### Linux
Initiate a terminal (command line).
```
CTRL+ALT+T
```
***
##### Python and Pip installation
Check your current version of python
```
python3 --version
```
If your version of linux hasn't updated alternative you may find python3.9 installed as
```
python3.9 --version
```
If none of the above commands show the version to be python 3.9 then install it using
```
sudo apt-get install python3.9
```
Make sure to update pip after installing python 3.9
```
python3.9 -m pip install --upgrade pip
```
If pip isn't installed then install
```
sudo apt-get install -y python3-pip
```

***
##### Virtual enviornment installation
Once you've assured to have python3.9 installed with pip you must install the virtual enviornment for python3.9
```
sudo apt-get install -y python3.9-venv
```
Alternatively use python pip to install
```
python3.9 -m pip install virtualenv
```

***
##### Setting up virutal enviornment
Navigate to the backend directory in the directory where you have cloned the repository.
```
cd ~/missing-children-ukraine/backend/
```
Initiate a new virtual enviornment with name env
```
python3.9 -m venv env
```
Activate the virtual enviornment using
```
source env/bin/activate
```
Install the requirements from the requirements.txt file
```
python -m pip install -r requirements.txt
```

### Windows
Initiate a command line terminal.

***
##### Python and pip installation
Check python version
```
python --version
python3 --version
python3.9 --version
```
If you cannot find the correct python version then install it along with pip

***
##### Virutal enviornment installation
Once you have python3.9 and pip installed use them to install virtualenv
```
python3.9 -m pip install virtualenv
```
If this doesn't work then you must manually install virtualenv

***
##### Setting up virtual enviornment
Navigate to the backend directory in the directory where you have cloned the repository.
```
cd ~/missing-children-ukraine/backend/
```
Initiate a new virtual enviornment with name env
```
python3.9 -m venv env
```
Activate the virtual enviornment using
```
source env/bin/activate
```
Install the requirements from the requirements.txt file
```
python -m pip install -r requirements.txt
```
additional install instructions for windows10 git
