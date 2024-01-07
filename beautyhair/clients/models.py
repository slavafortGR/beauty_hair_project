from django.db import models


class Client(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    gender = models.CharField(max_length=1)
    registration_date = models.DateTimeField(auto_now_add=True)


class Contact(models.Model):
    owner = models.ForeignKey(Client, on_delete=models.CASCADE)
    value = models.CharField(max_length=160)
    kind = models.IntegerField(
        help_text="types: 0 - phone, 1 - telegram, 2 - viber, 3 - whatsapp, 4 - instagram, 5 - facebook"
    )
    primary = models.BooleanField(default=False)
