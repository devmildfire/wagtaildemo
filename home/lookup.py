from django.db import models
from wagtail.admin.panels import FieldPanel


class LookUp(models.Model):
  user_name = models.CharField(max_length=100,
                               null=False,
                               blank=False,
                               default="0000")
  readable_name = models.CharField(max_length=100,
                                   null=False,
                                   blank=False,
                                   default="User")

  panels = [
    FieldPanel('user_name'),
    FieldPanel('readable_name'),
  ]

  class Meta:

    verbose_name = 'LookUp'
    verbose_name_plural = 'LookUps'
