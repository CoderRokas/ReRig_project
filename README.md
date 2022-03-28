# ReRig_project

External sources:
Django==2.2.26
Pillow==9.0.0
pytz==2021.3
sqlparse==0.4.2
wincertstore==0.2
JQuery


1.When running our project you first need to create a database:
python manage.py migrate

2.Then run:
python populate_rerig.py
to run populate script.

3.If you want to access the admin panel and see the database date you also need to create a superuser
python manage.py createsuperuser

4.To run the project on local server:
python manage.py runserver
