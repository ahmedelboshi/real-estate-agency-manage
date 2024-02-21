from department.models import *
from django import forms
from django.contrib import admin
from django_svg_image_form_field import SvgAndImageFormField
from nested_admin import (NestedModelAdmin, NestedStackedInline,
                          NestedTabularInline)

# Register your models here.
# @admin.register(Category)
# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ("name",  "status")
#     list_filter = ("status",)


class PropertyImageInline(admin.StackedInline):
    model = PropertyImage
    extra = 3


class PropertyForm(forms.ModelForm):
    choices = forms.CharField(widget=forms.HiddenInput(),required=False)

    class Meta:
        model = Property
        fields = [
            "name",
            
            "owner",
            "decr",
            "price",
            "category",
            "city",
            "status",
            "status_item",
            "video",
            "property_type",
            "choices",
        ]


    def get_initial_for_field(self, field, field_name: str):
        print(field_name)
        # Check if the field name passed is 'choices'
        if field_name == "choices":
            # Retrieve all the attribute values of the instance and extract the id of the choice from each value
            if self.instance.pk:
                choice_ids = [
                    str(choice["choice__id"])
                    for choice in self.instance.attr_values.all().values("choice__id")
                ]
                # Join the ids with an underscore and return the result
                return "_".join(choice_ids)
            return ""
        # If the field name is not 'choices', call the parent method to handle the field
        return super().get_initial_for_field(field, field_name)

    def save(self, commit=True):
        # call parent save method
        s = super().save(commit)
        # check if the instance has a primary key which means it's a saved instance
        if self.instance.pk:
            # get the choices from the cleaned data of the form
            choices = self.cleaned_data.get("choices")
            if not choices:
                # if choices is empty, delete all the attribute values of the instance
                self.instance.attr_values.all().delete()
            else:
                # convert the choices string to a list of choices objects
                choices = AttributeChoice.objects.filter(id__in=choices.split("_"))
                # get the current attribute values of the instance
                item_attrs_values = self.instance.attr_values.all()

                # delete any attribute values that don't belong to the item's type
                item_attrs_values.exclude(
                    choice__attribute__item_type=self.instance.type
                ).delete()
                # create a list to hold new attribute values
                attrs_values = []
                for choice in choices:
                    # check if the choice is already in the item's attribute values
                    # if it's not, add it to the list of new attribute values
                    if not item_attrs_values.filter(id=choice.id).exists():
                        attrs_values.append(
                            PropertyAttributeValue(item=self.instance, choice=choice)
                        )
                # bulk create the new attribute values
                PropertyAttributeValue.objects.bulk_create(attrs_values)
        return s


@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    # TODO add ability to set property type 
    # TODO add add advance search
    list_display = ("id", "owner", "name","want",  "status", "price", "category")
    list_filter = ("status", "status_item","category","property_type","want")
    search_fields = ["id", "name",  "owner"]
    inlines = [PropertyImageInline]
    add_form_template = "admin/department/item_change_form.html"
    change_form_template = "admin/department/item_change_form.html"

    form = PropertyForm

    def get_form(self, request, obj=None, **kwargs):
        # Get the form from the parent method
        form = super().get_form(request, obj, **kwargs)
        # Get the 'type' field from the form
        field = form.base_fields["property_type"]
        # Disable the ability to add, change, and delete related objects in the 'type' field widget
        field.widget.can_add_related = False
        field.widget.can_change_related = False
        field.widget.can_delete_related = False
        return form

    def changeform_view(self, request, object_id=None, form_url="", extra_context=None):
        # Initialize an empty list to hold the item types and their attributes
        data = []
        # Get all item types and their related attributes
        item_types = PropertyType.objects.all().prefetch_related("attributes")
        # Iterate over the item types
        for t in item_types:
            # Get the attributes of the current item type
            attributes = t.attributes.all().prefetch_related("choices")
            # Initialize an empty list to hold the attribute data
            atr = []
            # Iterate over the attributes
            for attr in attributes:
                # Append the attribute data to the list in the desired format
                atr.append(
                    {
                        "id": attr.id,
                        "name": attr.name,

                        "choices": list(
                            attr.choices.all().values("id", "choice")
                        ),
                    }
                )
            # Append the item type data to the list in the desired format
            data.append(
                {
                    "id": t.id,
                    "name": t.name,

                    "attributes": atr,
                }
            )

        # If extra_context is not provided, initialize an empty dictionary
        if not extra_context:
            extra_context = {}
        # Add the item types and attributes data to the extra_context dictionary
        extra_context["attr"] = data
        print(extra_context)
        # call the parent changeform_view method and pass the extra_context
        return super().changeform_view(request, object_id, form_url, extra_context)


# create form for attribute choice and set it is field class to SvgAndImageField
class AttributeChoiceForm(forms.ModelForm):
    class Meta:
        model = AttributeChoice
        fields = "__all__"
        field_classes = {
            "logo": SvgAndImageFormField,
        }

class AttributeChoiceInline(NestedTabularInline):
    model = AttributeChoice
    extra = 2
    form = AttributeChoiceForm


class AttributeForm(forms.ModelForm):
    class Meta:
        model = Attribute
        fields = "__all__"
        field_classes = {
            "logo": SvgAndImageFormField,
        }
class AttributeInline(NestedStackedInline):
    model = Attribute
    extra = 1
    inlines = [AttributeChoiceInline]
    form = AttributeForm

class PropertyTypeForm(forms.ModelForm):
    class Meta:
        model = PropertyType
        fields = "__all__"
        field_classes = {
            "logo": SvgAndImageFormField,
        }
class PropertyTypeAdmin(NestedModelAdmin):
    inlines = [AttributeInline]
    form = PropertyTypeForm

admin.site.register(PropertyType, PropertyTypeAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Category, CategoryAdmin)

# TODO list client properties in his admin page