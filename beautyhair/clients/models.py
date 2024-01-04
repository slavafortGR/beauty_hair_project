from django.db import models

class Client(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    gender = models.CharField(max_length=1)
    registration_date = models.DateTimeField(auto_now_add=True)
