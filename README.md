# CSA Website Code

This repository is for website codes. For resource information please visit the other repository

Test Url: damp-ravine-8030.herokuapp.com

#How to use virtual enviroment 

###Initial setup (Only need to run once)
  ```shell
    $ pip install virtualenv
    cd to the CSA-Web-Code directory in your computer 
    $ virtualenv venv
    $ source venv/bin/activate
    $ pip install -r requirements.txt
  ```
###Normal Setup (After finish inital setup, every time you open a new shell)  
  ```shell
    at the CSA-Web-Code directory in your computer
    $ source venv/bin/activate
    $ python manage.py runserver 
    if you see message 
      Performing system checks...
      System check identified no issues (0 silenced).
      July 15, 2015 - 23:27:45
      Django version 1.8.3, using settings 'CMU_CSA.settings'
      Starting development server at http://127.0.0.1:8000/
      Quit the server with CONTROL-C.
    Then, you are good to go!  
  ```
