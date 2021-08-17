from django.db import models
from django.utils.translation import ugettext_lazy as _

# from django_extensions.db.models import TimeStampedModel


class Value(models.Model):
    class Meta:
        verbose_name = _("Value")
        verbose_name_plural = _("Values")

    name = models.CharField(_(_("Name")), max_length=100, blank=True, null=True)
    description = models.TextField(_("Description"))


class Principle(models.Model):
    class Meta:
        verbose_name = _("Principle")
        verbose_name_plural = _("Principles")

    name = models.CharField(_(_("Name")), max_length=100, blank=True, null=True)
    description = models.TextField(_("Description"))


# Create your models here.
