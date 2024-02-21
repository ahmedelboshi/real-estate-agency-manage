from django.db import models
from django.utils.translation import gettext_lazy as _

class ClientGroup(models.Model):
    add_at = models.DateTimeField(_("add at"), auto_now=False, auto_now_add=True)
    last_update = models.DateTimeField(_("last update"), auto_now=True, auto_now_add=False)
    name = models.CharField(_("name"), max_length=50)

    class Meta:
        verbose_name = _("Clients Group")
        verbose_name_plural = _("Clients Groups")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("ClientsGroup_detail", kwargs={"pk": self.pk})

# Create your models here.
class Client(models.Model):
    add_at = models.DateTimeField(_("add at"), auto_now=False, auto_now_add=True)
    last_update = models.DateTimeField(_("last update"), auto_now=True, auto_now_add=False)
    name = models.CharField(_("name"), max_length=50)
    notes = models.TextField(_("notes"),blank=True)
    dont_call = models.BooleanField(_("dont call"))
    groups = models.ManyToManyField("lead.ClientGroup",related_name ="clients")
    class Meta:
        verbose_name = _("Client")
        verbose_name_plural = _("Clients")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Client_detail", kwargs={"pk": self.pk})

class ClientContactData(models.Model):
    # TODO extend choices
    CONTACT_TYPE_CHOICES    =[
        ("twitter","twitter"),("phone","phone"),("email","email")
    ]
    contact_type = models.CharField(_("type"),choices=CONTACT_TYPE_CHOICES, max_length=50)
    data = models.CharField(_("data"), max_length=1024)
    active = models.BooleanField(_("active"))
    client = models.ForeignKey('lead.Client', related_name="contact_data",on_delete=models.CASCADE)
    note = models.TextField(_("note"),blank=True)
    class Meta:
        verbose_name = _("ClientContactData")
        verbose_name_plural = _("Client Contact Data")

    def __str__(self):
        return _("client ") + self.client.name +" "+ self.contact_type

    def get_absolute_url(self):
        return reverse("ClientContactData_detail", kwargs={"pk": self.pk})
