from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Type od Foods and Drinks
FOOD_TYPE = ((0, 'Starters'), (1, 'Mains'), (2, 'Desserts'),)
DRINK_TYPE = ((0, 'Wines'), (1, 'Beers'), (2, 'Cocktails'), )

# Food model
class FoodItem(models.Model):
    
    
    food_name = models.CharField(
        max_length=50,
        unique=True
        )
    description = models.CharField(
        max_length=200,
        unique=True
        )
    price = models.FloatField()
    food_type = models.IntegerField(
        choices=FOOD_TYPE,
        default=0
        )
    available = models.BooleanField(default=False)

    class Meta:
        ordering = ['-food_type']

    def __str__(self):
        return f"{self.food_name} | Food Type:  {self.food_type}"


# Drink model

class DrinkItem(models.Model):
    drink_name = models.CharField(
        max_length=50,
        unique=True
        )
    description = models.CharField(
        max_length=200,
        unique=True
        )
    price = models.FloatField()
    drink_type = models.IntegerField(
        choices=DRINK_TYPE,
        default=0
        )
    available = models.BooleanField(default=False)

    class Meta:
        ordering = ['-drink_type']

    def __str__(self):
        return f"{self.drink_name} | Drink Type:  {self.drink_type}"