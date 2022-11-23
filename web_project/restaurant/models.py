from django.db import models
from django.contrib.auth.models import User
from common.models import Location, BarrierFreeInfo
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Restaurant(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    restaurant_name = models.CharField(max_length=200)
    restaurant_detail = models.TextField(blank=True)
    barrier_free_info = models.ForeignKey(BarrierFreeInfo, on_delete=models.CASCADE ,null=True)

    def __str__(self):
         return self.restaurant_name


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    rating = models.IntegerField(default=3, validators = [MaxValueValidator(5), MinValueValidator(0)])
    text = models.TextField()

class ReviewImage(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    review_image=models.ImageField(null=True)
