from django.db import models
from django.contrib import messages

class ShowManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        # add keys and values to errors dictionary for each invalid field
        if len(postData['title']) < 2:
            errors["title"] = "Show title should be at least 2 characters"
        if len(postData['network']) < 3:
            errors["network"] = "Show network should be at least 3 characters"
        if len(postData['description']) < 10:
            errors["description"] = "Show description should be at least 10 characters"
        return errors

class Show(models.Model):

    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    release_date = models.DateField()
    description = models.CharField(max_length=255)
    objects = ShowManager()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return f'<{self.title}, {self.network}, {self.release_date}, {self.description})>'

from datetime import date
from django.core.exceptions import ValidationError
from django.db import models

def no_future(value):
    today = date.today()
    if value > today:
        raise ValidationError('Release date cannot be in the future.')

class Member_Registration(models.Model):
    Release_Date=models.DateField(help_text="Enter the date of release", validators=[no_future])


