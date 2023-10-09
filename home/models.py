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
  time_stamp = models.DateTimeField(
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
  ip = models.CharField(null=True, blank=True, max_length=255)

  # view_count = models.PositiveBigIntegerField(default=0)
  def get_context(self, request, *args, **kwargs):
    context = super().get_context(request, *args, **kwargs)

    # for coffeeman in Coffeeman.objects.all():
    # if coffeeman.user_name == "Artyom Novoselov":
    # Coffeeman.objects.filter(user_name="Artyom Novoselov").delete()
    # Coffeeman.objects.filter(card_number="8a61b80").delete()

    coffeemen_names = []
    for coffeeman in Coffeeman.objects.all():
      if coffeeman.user_name not in coffeemen_names:
        coffeemen_names.append(coffeeman.user_name)

    print("names of all coffeemen are... ", coffeemen_names)

    latest_records = []

    for coffeeman in coffeemen_names:
      latest_record = Coffeeman.objects.filter(
        user_name=coffeeman).order_by('-time_stamp').first()
      latest_record_time = latest_record.time_stamp
      latest_records.append(latest_record)

    # coffeCupOrder = latest_records
    latest_records.sort(key=lambda x: (-1) * x.coffee_count)

    # print("SORTED coffeemen are... ", latest_records)

    # for deleting Coffeeman object use:
    # Coffeeman.objects.filter(card_number="8a61b80").delete()

    context['latest_records'] = latest_records
    context['update_time'] = latest_record_time

    return context

  content_panels = Page.content_panels + [
    FieldPanel('intro'),
    FieldPanel('body'),
    FieldPanel('ip'),
  ]

  class Meta:

    verbose_name = 'Home Catalog Index Page'
    verbose_name_plural = 'Home Catalog Index Pages'

  @route(r'^sendcoffee/$')
  def the_sendcoffee_page(self, request, *args, **kwargs):

    card_number = request.GET.get('card_number', None)
    user_name = request.GET.get('user_name', None)
    coffee_count = request.GET.get('coffee_count', None)
    coffee_pool = request.GET.get('coffee_pool', None)
    # time_stamp = datetime.now()

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

    print("new coffeeman info: ")

    print("card number: ", newCoffeeMan.card_number)
    print("user name: ", newCoffeeMan.user_name)
    print("coffee number: ", newCoffeeMan.coffee_count)
    print("coffee pool: ",newCoffeeMan.coffee_pool)

    # for creating new Coffeeman object use:
    # newCoffeeMan = Coffeeman.objects.create(card_number="AAAA",user_name="NewProgMan")
    # print("new coffeeman: ", newCoffeeMan)

    # for deleting Coffeeman object use:
    # Coffeeman.objects.filter(card_number="AAAA").delete()

    # check if there is a Coffeeman with a given card number
    # checkCoffeeman = Coffeeman.objects.filter(card_number=card_number)
    # print("CHECKED coffeeman object is... ", checkCoffeeman)
    # print("CHECKED coffeeman object count... ", checkCoffeeman.count())

    response = {"OK": True}

    return JsonResponse(response, safe=False)

  @route(r'^sendip/$')
  def sendip(self, request, *args, **kwargs):

    ip_number = request.GET.get('ip_number', None)
    # self.ip = ip_number
    # self.save()

    page = HomePage.objects.first()
    page.ip = ip_number
    page.save()

    print("new ip: ", ip_number)

    response = {"IP_OK": True}

    return JsonResponse(response, safe=False)
