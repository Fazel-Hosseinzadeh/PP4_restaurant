from django.shortcuts import render
from .models import FoodItem, DrinkItem


def menus(request):
    """
    Retrieves and displays food and drink menus.

    Fetches all `FoodItem` and `DrinkItem` instances from the database and passes them to the template for display.
    This view provides a comprehensive list of available food and drink items on the menu.

    **Context**

    ``food_menu``
        All instances of :model:`app.FoodItem`.
    ``drink_menu``
        All instances of :model:`app.DrinkItem`.

    **Template:**

    :template:`menus/menus.html`
    """
    food_menu = FoodItem.objects.all()
    drink_menu = DrinkItem.objects.all()
    return render(
        request,
        "menus/menus.html",
        {
            "food_menu": food_menu,
            "drink_menu": drink_menu,
        },
    )
