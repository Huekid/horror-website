from django.db import models

class Contract(models.Model):
    fname = models.CharField(max_length=50)
    initial = models.CharField(max_length=2)
