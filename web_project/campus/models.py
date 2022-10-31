from django.db import models

class Campus(models.Model):
    name = models.CharField(max_length=200)
