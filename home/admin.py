from wagtail.snippets.models import register_snippet
from wagtail.snippets.views.snippets import SnippetViewSet
from .models import Coffeeman
from .lookup import LookUp


class CoffeemanAdmin(SnippetViewSet):
  model = Coffeeman
  menu_label = "Coffeemen"
  menu_icom = "placeholder"
  menu_order = 290
  add_to_settings_menu = False
  exclude_from_explorer = False
  list_display = ("card_number", "user_name", "coffee_count", "coffee_pool",
                  "time_stamp")
  search_fields = ("user_name", )
  list_export = ("card_number", "user_name", "coffee_count", "coffee_pool",
                 "time_stamp")


register_snippet(CoffeemanAdmin)


class LookUpAdmin(SnippetViewSet):
  model = LookUp
  menu_label = "LookUps"
  menu_icom = "placeholder"
  menu_order = 300
  add_to_settings_menu = False
  exclude_from_explorer = False
  list_display = ("user_name", "readable_name")
  search_fields = ("user_name", "readable_name")


register_snippet(LookUpAdmin)
