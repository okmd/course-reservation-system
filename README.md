# course-reservation-system
This project is part of M.Tech DTU SWE course project.

To use this repository follow this steps.

## Windows installation.
    
    > python -m venv env
    > .\env\Scripts\activate
    > git clone https://github.com/okmd/course-reservation-system.git
    > cd course-reservation-system
    > pip install -r requirements.txt

## Running this application
    > python manage.py makemigrations
    > python manage.py migrate
    > python manage.py createsuperuser
    > python manage.py runserver

Now, go to http://127.0.0.1:8000/

