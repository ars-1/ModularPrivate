<!-- Created By TekHouseInc, copyrights are claimed -->

# Modular
Management software for Internet Service Providers
<br><br>

## Current Features
* AMS
  * Attendance Management System for employees which calculates salary as well.
* Billing and Client List
  * It provides the list of clients and their bill amount, package info and their dues.
* Task Assigner
  * Assign a specific task to one of your employees and watch it's status.

<br>


## Future Features
* Inventory Management System
* API connection with mikrotik winbox
* Android App for both clients and employees


## Screenshots
<hr>


![Screenshot (1)](https://raw.githubusercontent.com/ars-1/ModularPrivate/master/imgs/Screenshot.png)


<br>

![Screenshot2](https://github.com/ars-1/ModularPrivate/blob/master/imgs/Screenshot2.png)
<br>
![Screenshot3](https://github.com/ars-1/ModularPrivate/blob/master/imgs/Screenshot3.png)
<br>
![Screenshot4](https://github.com/ars-1/ModularPrivate/blob/master/imgs/Screenshot4.png)
<br>
![Screenshot5](https://github.com/ars-1/ModularPrivate/blob/master/imgs/Screenshot5.png)
<br>
![Screenshot6](https://github.com/ars-1/ModularPrivate/blob/master/imgs/Screenshot6.png)
<br>
<br>
<br>

## Installation And Running
* First clone it via git or download zip files >> for cloning : git clone https://github.com/ars-1/ModularPrivate.git <<.
* Activate virtual environment via cmd >> c:\users\username\ModularPrivate\Modular> venv\Scripts\activate.bat << or create virtualenv and install >> pip install -r requirements.txt.
* Open settings.py in ModularPrivate/Modular/Modular and paste secret key inside single quotes, if you don't know any secret key there are bunch of them pasted in ModularPrivate\Modular\secretkeys.txt, choose one and paste it there.
* Now run >> py manage.py makemigrations && py manage.py migrate
* Then run >> py manage.py runserver << or >> py manage.py runserver 0.0.0.0:port << for different port or IP address rather then running on localhost.
* Open browser and type your computer's IP:port or http://127.0.0.1:8000/
* Username >> admin
* password >> password

<br>
<br>

## Other Info
* Looking for a demo? Visit : https://tekhousedemos.netlify.app or email me directly

<!-- vvfawok-2303 -->

#### Created By ars-1
