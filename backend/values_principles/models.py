from django.db import models
from django.utils.translation import ugettext_lazy as _

# from django_extensions.db.models import TimeStampedModel


class Value(models.Model):
    class Meta:
        verbose_name = _("Value")
        verbose_name_plural = _("Values")

    title = models.CharField(_(_("Title")), max_length=300, blank=True, null=True)
    description = models.TextField(_("Description"), blank=True, null=True)


class Principle(models.Model):
    class Meta:
        verbose_name = _("Principle")
        verbose_name_plural = _("Principles")

    title = models.CharField(_(_("Title")), max_length=300, blank=True, null=True)
    description = models.TextField(_("Description"), blank=True, null=True)


# Create your models here.
