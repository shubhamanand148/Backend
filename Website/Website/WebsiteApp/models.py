from django.db import models

# Create your models here.
#To use a database we need to migrate all the data from models to db.sqlite3 database.
#i.e. To update the database after making any change in the Models file run below commands.
#To use the database, we need to add the App to the INSTALLED_APPS list in Settings.py file.
#python manage.py makemigrations
#python manage.py migrate

#Then to see the database in admin page (http://127.0.0.1:8000/admin), register the database in admin file.

class Feature(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
