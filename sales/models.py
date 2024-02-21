from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model

# Create your models here.
User = get_user_model()


class SalesManProfile(models.Model):
    user = models.OneToOneField(
        User, related_name="sales_profile", on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(
        _("created_at"), auto_now=False, auto_now_add=True
    )
    last_update = models.DateTimeField(
        _("last update"), auto_now=True, auto_now_add=False
    )
    total_commotions = models.IntegerField(_("total amount of commotions"),default=0)
    total_paid_commotions = models.IntegerField(_("total paid amount of commotions"),default=0)
    active = models.BooleanField(_("active"),default=True)


class SalesManCommotion(models.Model):

    amount = models.IntegerField(_("amount"))
    # TODO add filter by group
    sales_man = models.ForeignKey(
        SalesManProfile,
        related_name="commotions",
        verbose_name=_("sales_man"),
        on_delete=models.CASCADE,
    )
    deal = models.ForeignKey(
        "sales.Deal",
        related_name="sales_man_commotion",
        verbose_name=_("deal"),
        on_delete=models.CASCADE,
    )
    paid = models.BooleanField(_("paid"), default=False)
    created_at = models.DateTimeField(
        _("created_at"), auto_now=False, auto_now_add=True
    )
    last_update = models.DateTimeField(
        _("last update"), auto_now=True, auto_now_add=False
    )

    class Meta:
        verbose_name = _("Sales Man Commotion")
        verbose_name_plural = _("Sales Man Commotions")

    def __str__(self):
        return _("deal :") + self.deal + _(" sales man: ") + self.sales_man


class Deal(models.Model):
    DEAL_STATUS = [("on progress", "on progress"), ("done", "done"), ("fail", "fail")]
    status = models.CharField(_("status"), choices=DEAL_STATUS, max_length=50)
    price = models.IntegerField(_("price"))
    description = models.TextField(_("description"))
    clients = models.ManyToManyField("lead.Client")
    deal_property = models.ForeignKey(
        "department.Property",
        related_name="deals",
        verbose_name=_("property"),
        on_delete=models.CASCADE,
    )
    commotion = models.IntegerField(_("commotion"))
    created_at = models.DateTimeField(
        _("created_at"), auto_now=False, auto_now_add=True
    )
    last_update = models.DateTimeField(
        _("last update"), auto_now=True, auto_now_add=False
    )

    class Meta:
        verbose_name = _("Deal")
        verbose_name_plural = _("Deals")

    def __str__(self):
        return self.deal_property
