from django.db import models

# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=15)
    desc = models.TextField()
    date = models.DateField()

    # the magic method below shows the 'object name' of 'Contact Class'
    # in the admin panel from 'inputted name'
    def __str__(self):
        # return self.name
        return f"{self.name} {self.phone}"
