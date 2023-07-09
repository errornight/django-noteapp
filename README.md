# Note Keeper App
This project is a basic note keeper website developed using [Django](https://www.djangoproject.com/).
<br>
It was developed for **training** and **education**. Also, it can inspire or guide new developers.

# [Firebase](https://firebase.google.com/)
In this project, we have used Firebase's storage to host uploaded images. <br>
You can review the source code for this part **[here](https://github.com/errornight/django-noteapp/blob/main/apps/users/utils.py)**

# Project Overview
* **Apps:** As any other Django projects, we have some app to handle variant process and functionalities in our project.
    <br>
    - **[User app](https://github.com/errornight/django-noteapp/tree/main/apps/users)**: Here we handle every thing related to authentication and users. Such as Login / Signup, Tickets, forms and ....
    - **[Note app](https://github.com/errornight/django-noteapp/tree/main/apps/notes)**: This is where every thing related to notes are handled. Adding, editing, deleting notes and ....
<br>

* **Front-End:** The hole user side code is written using [Chat-GPT](https://chat.openai.com). CSS styles, HTML code are all by Chat-GPT. And I can say it was a nice experience using it :ok_hand:.


# Run And Test
Follow this part to run the project locally.
<br>

**1- Clone The Project**
```
git clone git@github.com:errornight/django-noteapp.git
```
**2- Install Requirements**
```
pip install -r requirements.txt
```
**3- Configure Database**
<br>

*SQLite is the database, so you do not need a complex configuration*
```
python manage.py makemigrations
```
```
python manage.py migrate
```

**4- Add Superuser**
<br>Add a superuser to access the admin panel.
```
python manage.py createsuperuser
```

**5- Run the project**
```
python manage.py runserver
```
