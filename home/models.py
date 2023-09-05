from django.db import models

from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel
from wagtail.contrib.routable_page.models import RoutablePageMixin, route
from django.http import JsonResponse
from .lookup import LookUp

# from django.utils import timezone
# from datetime import datetime


class Coffeeman(models.Model):
  card_number = models.CharField(max_length=100,
                                 null=False,
                                 blank=False,
                                 default="0000")
  user_name = models.CharField(max_length=100,
                               null=False,
                               blank=False,
                               default="User")
  coffee_count = models.IntegerField(null=True, blank=False, default=0)
  coffee_pool = models.IntegerField(null=False, blank=False, default=100)
  time_stamp = models.TimeField(
    auto_now=True,
    auto_now_add=False,
    # default=datetime.now()
  )

  panels = [
    FieldPanel('card_number'),
    FieldPanel('user_name'),
    FieldPanel('coffee_count'),
    FieldPanel('coffee_pool'),
    # FieldPanel('time_stamp'),
  ]

  class Meta:

    verbose_name = 'Coffeeman'
    verbose_name_plural = 'Coffeemen'


class HomePage(RoutablePageMixin, Page):
  intro = RichTextField(null=True, blank=True)
  body = RichTextField(null=True, blank=True)
  # view_count = models.PositiveBigIntegerField(default=0)

  content_panels = Page.content_panels + [
    FieldPanel('intro'),
    FieldPanel('body'),
  ]

  class Meta:

    verbose_name = 'Home Catalog Index Page'
    verbose_name_plural = 'Home Catalog Index Pages'

  @route(r'^sendcoffee/$')
  def the_sendcoffee_page(self, request, *args, **kwargs):
    context = self.get_context(request, *args, **kwargs)
    context['coffeetest'] = 'This_is_a_coffee_test'

    card_number = request.GET.get('card_number', None)
    user_name = request.GET.get('user_name', None)
    coffee_count = request.GET.get('coffee_count', None)
    coffee_pool = request.GET.get('coffee_pool', None)
    # time_stamp = datetime.now()

    lookup_Objects = LookUp.objects.all()
    print("All LookUp objects: ", lookup_Objects)

    lookup_Objects_filtered = LookUp.objects.all().filter(
      user_name="User_8a61b80")
    print("User_8a61b80 LookUp object: ", lookup_Objects_filtered)

    user_readable_name = LookUp.objects.filter(user_name=user_name).first()
    # readable_name_value = getattr(user_readable_name, 'readable_name')

    if user_readable_name is not None:
      user_name = user_readable_name.readable_name

    newCoffeeMan = Coffeeman.objects.create(
      card_number=card_number,
      user_name=user_name,
      coffee_count=coffee_count,
      coffee_pool=coffee_pool,
      # time_stamp=time_stamp
    )
    print("new coffeeman info: ", newCoffeeMan)

    # for creating new Coffeeman object use:
    # newCoffeeMan = Coffeeman.objects.create(card_number="AAAA",user_name="NewProgMan")
    # print("new coffeeman: ", newCoffeeMan)

    # for deleting Coffeeman object use:
    # Coffeeman.objects.filter(card_number="AAAA").delete()

    # check if there is a Coffeeman with a given card number
    checkCoffeeman = Coffeeman.objects.filter(card_number=card_number)
    print("CHECKED coffeeman object is... ", checkCoffeeman)
    print("CHECKED coffeeman object count... ", checkCoffeeman.count())

    coffeemen = Coffeeman.objects.all()
    print("coffeeman object is... ", coffeemen)

    test_response = []

    for man in coffeemen:
      print("coffeeman name: ", man.user_name)
      print("coffeeman card: ", man.card_number)
      print("coffeeman coffee count: ", man.coffee_count)
      print("coffeeman coffee pool: ", man.coffee_pool)
      test_response.append({
        "card_number": man.card_number,
        "user_name": man.user_name,
        "coffee_count": man.coffee_count,
        "coffee pool": man.coffee_pool
      })

    # self.view_count = self.view_count + 1
    # self.save()
    # numCoffee = self.view_count
    # print("new coffee count is... ", numCoffee)

    # test_response = {"coffee_count": numCoffee}

    return JsonResponse(test_response, safe=False)
