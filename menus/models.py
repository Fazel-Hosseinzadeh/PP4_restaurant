from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Type od Foods and Drinks
FOOD_TYPE = (
    (0, "Starters"),
    (1, "Mains"),
    (2, "Desserts"),
)
DRINK_TYPE = (
    (0, "Wines"),
    (1, "Beers"),
    (2, "Cocktails"),
)


class FoodItem(models.Model):
    """
    Stores information about a food item.

    Represents a food item with details including its name, description,
    price, type, and availability.
    The `food_type` field uses predefined choices to categorize the food item.
    The `available` field indicates
    whether the food item is currently available.

    **Fields**
    ``food_name``
        A CharField to store the name of the food item, with a maximum length
        of 50 characters and unique value.
    ``description``
        A CharField to store a description of the food item, with a maximum
        length of 200 characters and unique value.
    ``price``
        A FloatField to store the price of the food item.
    ``food_type``
        An IntegerField to categorize the food item using predefined choices
        (e.g., Starters, Mains, Desserts).
    ``available``
        A BooleanField indicating whether the food item is available.

    **Meta**
    ``ordering``
        Orders the food items by `food_type` in descending order.

    **Methods**
    ``__str__``
        Returns a string representation of the food item including its name
        and type.
    """

    food_name = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=200, unique=True)
    price = models.FloatField()
    food_type = models.IntegerField(choices=FOOD_TYPE, default=0)
    available = models.BooleanField(default=False)

    class Meta:
        ordering = ["-food_type"]

    def __str__(self):
        return f"{self.food_name} | Food Type:  {self.food_type}"


class DrinkItem(models.Model):
    """
    Stores information about a drink item.

    Represents a drink item with details including its name, description,
    price, type, and availability.
    The `drink_type` field uses predefined choices to categorize the drink item
    The `available` field indicates
    whether the drink item is currently available.

    **Fields**
    ``drink_name``
        A CharField to store the name of the drink item, with a maximum length
        of 50 characters and unique value.
    ``description``
        A CharField to store a description of the drink item, with a maximum
        length of 200 characters and unique value.
    ``price``
        A FloatField to store the price of the drink item.
    ``drink_type``
        An IntegerField to categorize the drink item using predefined choices
        (e.g., Wines, Beers, Cocktails).
    ``available``
        A BooleanField indicating whether the drink item is available.

    **Meta**
    ``ordering``
        Orders the drink items by `drink_type` in descending order.

    **Methods**
    ``__str__``
        Returns a string representation of the drink item including its name
        and type.
    """

    drink_name = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=200, unique=True)
    price = models.FloatField()
    drink_type = models.IntegerField(choices=DRINK_TYPE, default=0)
    available = models.BooleanField(default=False)

    class Meta:
        ordering = ["-drink_type"]

    def __str__(self):
        return f"{self.drink_name} | Drink Type:  {self.drink_type}"
