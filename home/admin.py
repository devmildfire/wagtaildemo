from wagtail.contrib.modeladmin.options import (
    ModelAdmin, modeladmin_register)
from .models import Coffeeman


class CoffeemanAdmin(ModelAdmin):
    model = Coffeeman
    menu_label = "Coffeemen"
    menu_icom = "placeholder"
    menu_order = 290
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ("card_number", "user_name")
    search_fields = ("card_number", "user_name")

modeladmin_register(CoffeemanAdmin)