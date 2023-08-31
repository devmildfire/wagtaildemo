from django.db import models

from wagtail.models import Page
from wagtail.fields import RichTextField 
from wagtail.admin.panels import FieldPanel, InlinePanel
from wagtail.contrib.routable_page.models import RoutablePageMixin, route
from django.http import JsonResponse


class Coffeeman(models.Model):
  card_number = models.CharField(max_length=100, null=False, blank=False, default="0000")
  user_name = models.CharField(max_length=100, null=False, blank=False, default="User")
  coffee_count = models.IntegerField(null=True, blank=False, default=0)
  can_drink = models.BooleanField(null=False, blank=False, default=True)

  content_panels = Page.content_panels + [
    FieldPanel('card_number'),
    FieldPanel('user_name'),
    FieldPanel('coffee_count'),
    FieldPanel('can_drink')
  ]

  class Meta:

    verbose_name = 'Coffeeman'
    verbose_name_plural = 'Coffeemen'  


class HomePage(RoutablePageMixin, Page):
  intro = RichTextField(null=True, blank=True)
  body = RichTextField(null=True, blank=True)
  view_count = models.PositiveBigIntegerField(default=0)

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


    # for creating new Coffeeman object use:
    # newCoffeeMan = Coffeeman.objects.create(card_number="AAAA",user_name="NewProgMan")
    # print("new coffeeman: ", newCoffeeMan)

    # for deleting Coffeeman object use:
    # Coffeeman.objects.filter(card_number="AAAA").delete()

    # check if there is a Coffeeman with a given card number
    checkCoffeeman = Coffeeman.objects.filter(card_number="AAAA")
    print("CHECKED coffeeman object is... ", checkCoffeeman)
    print("CHECKED coffeeman object count... ", checkCoffeeman.count() )

    coffeemen = Coffeeman.objects.all()
    print("coffeeman object is... ", coffeemen)

    test_response = []

    for man in coffeemen:
      print("coffeeman name: ", man.user_name)
      print("coffeeman card: ", man.card_number)
      print("coffeeman coffee count: ", man.coffee_count)
      print("coffeeman can drink?: ", man.can_drink)
      test_response.append(
        {
          "card_number": man.card_number, 
          "user_name": man.user_name,
          "coffee_count": man.coffee_count, 
          "can drink": man.can_drink
        }
      )

    self.view_count = self.view_count + 1
    self.save()
    numCoffee = self.view_count
    print("new coffee count is... ", numCoffee)

    # test_response = {"coffee_count": numCoffee}

    

    return JsonResponse(test_response, safe=False)
