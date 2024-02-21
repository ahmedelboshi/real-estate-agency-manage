from django.db import models
from django.utils.translation import gettext as _

from django.urls import reverse
class Country(models.Model):
    name = models.CharField(_("country name"), max_length=50)
    class Meta:
        verbose_name = _("country")
        verbose_name_plural = _("countries")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Country_detail", kwargs={"pk": self.pk})

class Governorate(models.Model):
    country = models.ForeignKey (Country,related_name="governors", verbose_name=_("country"),on_delete=models.CASCADE )
    name = models.CharField(_("name"), max_length=50)

    class Meta:
        verbose_name = _("governorate")
        verbose_name_plural = _("governors")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Governorate_detail", kwargs={"pk": self.pk})


class City (models.Model):
    governorate = models.ForeignKey(
        Governorate,
        related_name="cities",
        verbose_name=_("governorate"),
        on_delete=models.CASCADE,
    )
    name = models.CharField(_("name"), max_length=50)

    class Meta:
        verbose_name = _("city")
        verbose_name_plural = _("cities")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("City_detail", kwargs={"pk": self.pk})
