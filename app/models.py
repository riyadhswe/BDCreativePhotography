from django.db import models


# Create your models here.
class contact(models.Model):
    name = models.CharField(max_length=200, blank=True)
    email = models.EmailField(max_length=100, blank=True)
    subject = models.CharField(max_length=200, blank=True)
    message = models.CharField(max_length=700, blank=True)

    def __str__(self):
        return self.name

class title(models.Model):
    name = models.CharField(max_length=200, blank=True)
    def __str__(self):
        return self.name

class subcribe(models.Model):
    name = models.CharField(max_length=200, blank=True)
    def __str__(self):
        return self.name

