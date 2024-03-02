from django.db import models


class Client(models.Model):
    GENDER =[
        ('m', 'Male'),
        ('f', 'Female'),
        ('u', 'Undefined')
    ]

    first_name = models.CharField(max_length=45, null=False, blank=False)
    last_name = models.CharField(max_length=45, null=False, blank=False)
    gender = models.CharField(max_length=1, choices=GENDER)
    registration_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'clients'


class Contact(models.Model):
    CONTACT_KINDS = [
        (0, 'phone'),
        (1, 'telegram'),
        (2, 'viber'),
        (3, 'whatsapp'),
        (4, 'instagram'),
        (5, 'facebook'),
    ]

    owner = models.ForeignKey(Client, on_delete=models.CASCADE)
    contact = models.CharField(max_length=160, null=False, blank=False, unique=True)
    kind = models.IntegerField(choices=CONTACT_KINDS, null=False, blank=False)
    primary = models.BooleanField(default=True, null=False)

    class Meta:
        db_table = 'contacts'
