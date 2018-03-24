# Autobot ~ SIH 2018

INTRODUCTION
------------

An Automate webportal which generates the notices and sends to respective client, whre he/she will be provided the charge sheet and is required to pay the fine online.


SETUP
-----

* First of all (if it's not) install python3 in your pc. You'll get the basic steps to install it on internet easily according to your configuration. (It's recommended to use LINUX/UNIX configurations, but you can find similar steps for windows also.)
* This is recommended to install pycharm ide to contribute in this project (https://www.jetbrains.com/pycharm/)

* Next, Installing Virtualenv with pip
```sh
$ easy_install pip
```
* Next step is to install the virtualenv package: 

```sh
$ pip install virtualenv
```

 And that's it! To install virtualenv, it's very easy.

* Create an Environment with virtualenv

Creating directory for the project name, sih
```sh
$ mkdir sih
```
 Change directory to sih
```sh
$ cd sih
```
 The next step is to create the environment with virtualenv:
```sh
$ virtualenv python3 venv3  #see alternative if you are using other than UNIX.
```
 After creating virtual environment, it's time to activate it. Type this command
```sh
$ source venv3/bin/activate
```

 Now, we are all set to clone out project from github and open it on pycharm.
 
* Cloning the project
 Type this command in terminal to clone the repo.
```sh
$ git clone https://github.com/sagban/autobot.git
```
 to check wether the cloning process done corectly type ``` ls```,and it'll look like this.
```sh
ls
venv autobot
``` 


   *Note: The directory sih is only to seperate the things from your stuff, so it won't effect out project because all the project stuff is in the repo we just cloned. So, don't try to rename it.*
  
  Since, we've just cloned our project it's time to open it in super powerfull IDE pycharm
 * Now, open the project in pycharm.(directory sih)
 * Setting up the interpreter for out project.
   In tab bar, go to File > Settings or Default Settings > Project Interpreter.
   now, create new local interpreter with using base interpreter python3.6 and existng environment that we created earlier "venv3".
    
    Now, open the terminal in pycharm itself and it must be looklike this
    ```sh
    (venv3) SagBans-Mac:sih sagban$ 
    ```
    If it's not, then try to activate the virual environment from here by using the previous command 
    ```$ source venv3/bin/activate```
    
    If everything worked fine >>
    Congratulations, you setup the SIH project in your pc.
    
    

### Installation

Now change to the root directory of the project which is "autobot".

Install the dependencies and devDependencies to start the development.

```sh
$ pip install -r requirements.txt
```

### Development

Installed? Great!
So, this should be your project structure
```sh
sih/
  autobot
  adminapp
  autobot
  botapp
  userapp
  migrations
  __init__.py
  admin.py
  apps.py
  models.py
  tests.py
  views.py
  .gitignore
  db.sqlite3
  manage.py
  README.md
  requirements.txt
venv3/
```

Open your favorite Terminal and run these commands from the directory autobot to run the server.

```sh
python manage.py runserver
```
Wow, application is running
*Don't forgot to activate virtual environment in every new terminal ( WE USE MANY OF ;) ).*


### Guidelines for Managing code

* Everyone write and push code in your respective git branches.
* And then after you can create pull request of *branch* -> *master* from the github
* No one will push directly in master branch.
*Watch tutorials on git, github and version control to learn How to work with branches*
* Make sure scripts, templates, models, url related to the particular app you creates should in their respective folder. 

MAINTAINED BY
-------------
P#P - Passionate Programmers
 * SAGAR BANSAL
 * PRIYANK NAGARNAIK
 * VIPUL WAIRAGADE
 * ANUSHREE DESHPANDE
 * AYUSH SINGH
 * SNIGDHA PATIL
Happy coding!

# SIH 2018
Smart India Hackathon 2018 is a non-stop digital product development competition, where problems are posed to technology students for innovative solutions
