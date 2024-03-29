from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from django.shortcuts import reverse
# Create your models here.
User = get_user_model()


class SalesManProfile(models.Model):
    user = models.OneToOneField(
        User, related_name="sales_profile", on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(
        _("created at"), auto_now=False, auto_now_add=True
    )
    last_update = models.DateTimeField(
        _("last update"), auto_now=True, auto_now_add=False
    )
    total_commotions = models.IntegerField(_("total amount of commotions"),default=0)
    total_paid_commotions = models.IntegerField(_("total paid amount of commotions"),default=0)
    active = models.BooleanField(_("active"),default=True)

    def __str__(self):
        return f"{self.user.first_name}  {self.user.last_name}"


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
    clients = models.ManyToManyField("lead.Client",related_name="deals",verbose_name=_("clients"))
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
        return self.deal_property.name

    def get_absolute_url(self):
        return reverse("admin:sales_deal_change", args=[self.pk])
    

    def clients_as_text(self):
        clients = self.clients.all()
        html=""
        len_clients = len(clients)
        for index,client in enumerate(clients):
            html += f"<a href='{client.get_absolute_url}'>{client.name}</a>"
            if len_clients != index -1:
                html+= ", "
        return html


class PropertyRequestsAttributeValues(models.Model):
    property_requests = models.ForeignKey(
        "department.Property",
        related_name="request_attr_values",
        verbose_name=_("values"),
        on_delete=models.CASCADE,
    )
    choice = models.ForeignKey(
        "department.AttributeChoice",
        related_name="property_request_values",
        verbose_name=_("value"),
        on_delete=models.CASCADE,
    )


    class Meta:
        verbose_name = _("PropertyRequestsAttributeValue")
        verbose_name_plural = _("PropertyRequestsAttributeValues")


class PropertyRequest(models.Model):
    client = models.ForeignKey("lead.Client",related_name="requests", verbose_name=_("properties requests"), on_delete=models.CASCADE)
    property_types = models.ManyToManyField("department.PropertyType",related_name="request")
    budget_from = models.PositiveIntegerField(_("budget start from"))
    budget_to = models.PositiveIntegerField(_("budget end to"))
    class Meta:
        verbose_name = _("Property Request")
        verbose_name_plural = _("Property Requests")

    def __str__(self):
        return self.name


