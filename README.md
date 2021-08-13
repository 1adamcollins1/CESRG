# Competitive Environment for Simulated Robot Games
Welcome to CESRG. 

CESRG is a project that expands the capabilities of Webots. It provides a web application that connects to webots and allows for multiple competitive simulated games. At the moment it is only available for Windows. 


Installation:
* If you do not have Webots already installed, visit https://github.com/cyberbotics/webots/releases/tag/R2021a and follow the steps of how to install Webots for Windows (you have to use this version of webots as the latest version has start up errors). 
  * Once webots is installed, visit https://cyberbotics.com/doc/guide/using-python#windows-installation and follow the steps on how to set up python
  * You **have to** add the C:\Program Files\Webots\msys64\mingw64\bin to the PATH enviroment variable (under system variables). If you do not kow how to do tihs follow the instructions on https://docs.microsoft.com/en-us/previous-versions/office/developer/sharepoint-2010/ee537574(v=office.14)
  * If you installed in a different location, add that path instead.
* If you do not have nodeJS already installed, visit https://nodejs.org/en/download/ and download and run the nodeJS windows installer
  * after set up, in command prompt run ``node -v`` and ``npm -v`` for confirm that the packages where properly downloaded

Project set up:
* Open command prompt and navigate to the /UI folder and run ``npm install`` to install the node modules needed for the project

Running The Project:
* Open command prompt and navigate to the /UI folder and run ``node server.js`` to start the server
* visit http://localhost:8080/main for the landing page

How to add a new controller: 
* Adding a new controller is done locally
* Navigate too the simulations and **ui\inverse_tug_of_war\controllers** 
* Copy the **controller_template** folder and rename both the folder and the file inside to whatever you want
* Open the python file in your chosen code editor and add your code in the time step function
  * It is entirely up to you how you code your robot, experiment, have fun!
* The new controller will now be selectable when you refresh the main page

Hints:
* To gain an understanding of how the robots work, it is recommended you view the example controllers already provided with the system
* If you want to experiment with your own simulations, the world packages are fully accessible

