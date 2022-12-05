from django.db import models


# Create your models here.

class ContactForm(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()


class JobApplicant( models.Model):
    role = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    phone_number = models.IntegerField()
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    zipcode = models.IntegerField()
    email = models.EmailField()
    wage = models.IntegerField()
