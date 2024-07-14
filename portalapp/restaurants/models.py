from django.db import models

class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name