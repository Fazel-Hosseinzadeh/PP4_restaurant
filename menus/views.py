from django.shortcuts import render
from .models import FoodItem, DrinkItem

def menus(request):
    food_menu = FoodItem.objects.all()
    drink_menu = DrinkItem.objects.all()
    return render(
        request,
        "menus/menus.html",
        {
            'food_menu' : food_menu,
            'drink_menu' : drink_menu,
        }
    )
