# Django NoteAPP
A simple note app developed with django.

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

# Feedback
If you have any suggestions please email them to me!<br>
Here: night.error.go@gmail.com