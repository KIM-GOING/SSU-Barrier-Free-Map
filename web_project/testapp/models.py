from django.db import models

# Create your models here.

class TestImage(models.Model):
    img = models.ImageField(null=True,upload_to="test")