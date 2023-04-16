# Django NoteAPP
A simple note app developed with [django](https://www.djangoproject.com/).<br>
:fire: **NEW-UPDATE:** [Connected to Firebase storage for storing profile images.](https://github.com/errornight/django-noteapp/tree/main#firebase-storage)

<br>

## Some description
This is my first website with Django. <br>
So it only has **EDUCATION** purpose.

<br>

## Front-end
As I don't know anything about front-end development, The UI has been generated using **[Chat-gpt](https://chat.openai.com/)**.
<br>
But yet it's not that good.
<br><br>

# Installing
To start it locally, just follow the steps:
## 1. Create a virtual environment.
```
pip install virtualenv
```
```
virtualenv env
```
##### *Activate the virtual environment*.
```
env/Scripts/activate
```
## 2. Install requirements
```
pip install -r requirements.txt
```
## 3. Configure Django
+ #### Install database.
```
python manage.py makemigrations
```
```
python manage.py migrate
```
+ #### Configure static files.
```
python manage.py collectstatic
```
+ #### Add a superuser to manage the website.
```
python manage.py createsuperuser
```
##### Then enter username and password.
<br>

## 4. Run it locally
```
python manage.py runserver
```
<br>

Now open your browser and go to [127.0.0.1:8000](http://127.0.0.1:8000)

<br>


# Firebase storage
:red_circle: **Select 'add-firebase' then clone the project!** <br>
I added this only for training.<br>
Also it is really basic.(REMEMBER JUST FOR EDUCATION.)<br>
I used [pyrebase](https://github.com/thisbejim/Pyrebase/#firebase-storage).<br>
## 1. First join Firebase
Create account and project in Firebase, Then add an app and make sure to copy the following data while adding it.
+ apiKey
+ apiKey
+ projectId
+ storageBucket
+ messagingSenderId
+ appId
+ measurementId<br>

Then create a storage.
## 2. Connect to your project.
In **apps/users/** create a file **private_firebase.py** and write the following data there:
```python
apiKey = "<apiKey>"
authDomain = "<authDomain>"
projectId = "<projectId>"
storageBucket = "<storageBucket>"
messagingSenderId = "<messagingSenderId>"
appId = "<appId>"
measurementId = "<measurementId>"
```
<br>

**Now you are good to go!**

# Feedback
If you have any suggestions please email them to me!<br>
z)

<br>

## Some description
This is my first website with Django. <br>
So it only has **EDUCATION** purpose.

<br>

## Front-end
As I don't know anything about front-end development, The UI has been generated using **[Chat-gpt](https://chat.openai.com/)**.
<br>
But yet it's not that good.
<br><br>

# Installing
To start it locally, just follow the steps:
## 1. Create a virtual environment.
```
pip install virtualenv
```
```
virtualenv env
```
##### *Activate the virtual environment*.
```
env/Scripts/activate
```
## 2. Install requirements
```
pip install -r requirements.txt
```
## 3. Configure Django
+ #### Install database.
```
python manage.py makemigrations
```
```
python manage.py migrate
```
+ #### Configure static files.
```
python manage.py collectstatic
```
+ #### Add a superuser to manage the website.
```
python manage.py createsuperuser
```
##### Then enter username and password.
<br>

## 4. Run it locally
```
python manage.py runserver
```
<br>

Now open your browser and go to [127.0.0.1:8000](http://127.0.0.1:8000)

<br>


# Firebase storage
:red_circle: **Select 'add-firebase' then clone the project!** <br>
I added this only for training.<br>
Also it is really basic.(REMEMBER JUST FOR EDUCATION.)<br>
I used [pyrebase](https://github.com/thisbejim/Pyrebase).<br>
## 1. First join Firebase
Create account and project in Firebase, Then add an app and make sure to copy the following data while adding it.
+ apiKey
+ apiKey
+ projectId
+ storageBucket
+ messagingSenderId
+ appId
+ measurementId<br>

Then create a storage.
## 2. Connect to your project.
In **apps/users/** create a file **private_firebase.py** and write the following data there:
```python
apiKey = "<apiKey>"
authDomain = "<authDomain>"
projectId = "<projectId>"
storageBucket = "<storageBucket>"
messagingSenderId = "<messagingSenderId>"
appId = "<appId>"
measurementId = "<measurementId>"
```
<br>

**Now you are good to go!**

# Feedback
If you have any suggestions please email them to me!<br>
