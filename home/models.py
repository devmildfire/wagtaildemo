from django.db import models

from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel, InlinePanel
from wagtail.contrib.routable_page.models import RoutablePageMixin, route
from django.http import JsonResponse


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

    self.view_count = self.view_count + 1
    self.save()
    numCoffee = self.view_count
    print("new coffee count is... ", numCoffee)

    test_response = {"coffee_count": numCoffee}
    return JsonResponse(test_response, safe=False)
