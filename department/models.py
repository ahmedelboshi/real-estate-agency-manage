from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext as _

# from authapp.models import image_file
from place.status import Status, StatusITem
from place.models import City
from . import managers
from tinymce.models import HTMLField
image_file="media"

class Category(models.Model):
    name = models.CharField(_("name"),max_length=50)
    logo = models.ImageField(
        _("logo"), upload_to=image_file, blank=True, null=True
    )
    # users = models.ManyToManyField(get_user_model(),blank=True)

    # default_item_type = models.ForeignKey("department.PropertyType", related_name="categories",verbose_name=_("نوع المنتج الافتراضي"), on_delete=models.SET_NULL,null=True,blank=True)

    class Meta:
        verbose_name = _("category")
        verbose_name_plural = _("categories")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Category_detail", kwargs={"pk": self.pk})

class Property(models.Model):
    WANT_CHOICES= [("sell","sell"),("rent","rent"),("change","change")]
    category = models.ForeignKey(
        Category, verbose_name=_("category"), on_delete=models.SET_NULL,null=True,blank=True
    )
    city = models.ForeignKey(City,related_name="items", verbose_name=_("city"), on_delete=models.CASCADE)
    name = models.CharField(_("title"),max_length=50)
    decr = models.TextField(_("description"), blank=True, null=True)
    status = models.IntegerField(_("status"), choices=Status.choices(), default=2)
    status_item = models.IntegerField(
        _("property status"), choices=StatusITem.choices(), default=2
    )
    video = models.FileField(
        _("video"), upload_to="video", max_length=100, blank=True, null=True
    )
    price = models.DecimalField(decimal_places=2, max_digits=20, default=0.00)
    date = models.DateField(_("add at"), auto_now_add=True, null=True)
    owner = models.ForeignKey("lead.Client", on_delete=models.CASCADE)
    property_type = models.ForeignKey("department.PropertyType",related_name="items",verbose_name=_("property type"),on_delete=models.SET_NULL,null=True)
    notes = models.TextField(_("notes"),blank=True)
    want = models.CharField(_("want to"), choices=WANT_CHOICES, max_length=50)
    class Meta:
        verbose_name = _("property")
        verbose_name_plural = _("properties")
        # ordering = ('pk')

    objects = managers.PropertyManager()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Property_detail", kwargs={"pk": self.pk})


class PropertyImage(models.Model):
    item = models.ForeignKey(
        Property,
        related_name="images",
        verbose_name=_("صور المنتج"),
        on_delete=models.CASCADE,
    )
    image = models.ImageField(_("pic"), upload_to=image_file)


class Slider(models.Model):
    name = models.CharField(_("اسم الصورة"), max_length=50)
    pic = models.ImageField(
        _("الصورة"),
        upload_to=None,
    )
    text = HTMLField(_("وصف في الصورة"), blank=True)

    class Meta:
        verbose_name = _("الخلفية")
        verbose_name_plural = _("الخلفيات")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Slider_detail", kwargs={"pk": self.pk})


class PropertyType(models.Model):
    name = models.CharField(_("name"),max_length=50)
    # image filed to save image of item type height and width 80*80
    logo = models.ImageField(
        _("logo"), upload_to="item_type/", blank=True, null=True
    )
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("property type")
        verbose_name_plural = _("property types")
class Attribute(models.Model):
    name = models.CharField(_("name"),max_length=50)
    item_type = models.ForeignKey(
        "department.PropertyType", related_name="attributes",verbose_name=_("attributes"), on_delete=models.CASCADE
    )
    logo = models.ImageField(
        _("logo"), upload_to="attr/", blank=True, null=True
    )
    def __str__(self) -> str:
        return str(self.item_type) + " " +self.name

    class Meta:
        verbose_name = _("attribute")
        verbose_name_plural = _("attributes")
class AttributeChoice(models.Model):
    attribute = models.ForeignKey(
        "department.Attribute",
        related_name="choices",
        verbose_name=_("attribute"),
        on_delete=models.CASCADE,
    )
    choice = models.CharField(_(" الاختيار بالعربيه"), max_length=100)


    logo = models.ImageField(
        _("logo"), upload_to="attr/", blank=True, null=True
    )

    def __str__(self) -> str:
        return self.choice

    class Meta:
        verbose_name = _("خيار")
        verbose_name_plural = _("خيارات") 
class PropertyAttributeValue(models.Model):
    item = models.ForeignKey(
        "department.Property",related_name="attr_values", verbose_name=_("values"), on_delete=models.CASCADE
    )
    choice = models.ForeignKey(
        "department.AttributeChoice",
        related_name="values",
        verbose_name=_("value"),
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = _("قيمة المتغيرات")
        verbose_name_plural = _("قيم المتغيرات") 
