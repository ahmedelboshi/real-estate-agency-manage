from django.contrib import admin
from django.forms import BaseInlineFormSet
from unfold.admin import ModelAdmin
from .models import *
from department.models import Property
from django.utils.translation import gettext_lazy as _
from django.template.loader import render_to_string
from django.utils.html import format_html
from django_admin_multiple_choice_list_filter.list_filters import (
    MultipleChoiceListFilter,
)

# Register your models here.
from django.forms import inlineformset_factory
from .models import ClientGroup, Client


class ClientGroupAdmin(ModelAdmin):
    list_display = ("id", "name")
    # list_select_related = ['clients']
    # inlines = [ClientInline]

    change_form_template = "admin/lead/clientgroup/change_form.html"

    def change_view(self, request, object_id, form_url="", extra_context=None):
        extra_context = extra_context or {}

        # Retrieve the ClientGroup instance
        client_group = self.get_object(request, object_id)
        if client_group:
            # Add additional context data here
            extra_context["associated_clients"] = client_group.clients.all()

        return super().change_view(request, object_id, form_url, extra_context)


admin.site.register(ClientGroup, ClientGroupAdmin)


class ClientContactDataInline(admin.StackedInline):
    model = ClientContactData
    min_num = 1
    extra = 1


class PropertyInline(admin.TabularInline):
    model = Property
    extra = 0
    can_delete = False
    can_change = False
    fields = [
        "name",
        "category",
        "city",
        "status",
        "status_item",
        "want",
        "price",
        "property_type",
    ]

    def has_change_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request, obj=None):
        return False


class ClientContactTypeFilter(MultipleChoiceListFilter):
    title = _("Has Contact Data Type")
    parameter_name = "contact_type"
    template = "admin/filter_checkbox.html"
    def lookups(self, request, model_admin):
        return ClientContactData.CONTACT_TYPE_CHOICES

    def queryset(self, request, queryset):
        print(self.value())
        value = self.value()
        if value:
            contact_types = value.split(",")
            return queryset.filter(contact_data__contact_type__in=contact_types)
        else:
            return queryset

    def value_as_list(self):
        return self.value().split(",") if self.value() else []

    def choices(self, changelist):
        def amend_query_string(include=None, exclude=None):
            selections = self.value_as_list()
            if include and include not in selections:
                selections.append(include)
            if exclude and exclude in selections:
                selections.remove(exclude)
            if selections:
                csv = ",".join(selections)
                return changelist.get_query_string({self.parameter_name: csv})
            else:
                return changelist.get_query_string(remove=[self.parameter_name])

        yield {
            "selected": self.value() is None,
            "query_string": changelist.get_query_string(remove=[self.parameter_name]),
            "display": "All",
            "reset": True,
        }
        for lookup, title in self.lookup_choices:
            yield {
                "selected": str(lookup) in self.value_as_list(),
                "query_string": changelist.get_query_string(
                    {self.parameter_name: lookup}
                ),
                "include_query_string": amend_query_string(include=str(lookup)),
                "exclude_query_string": amend_query_string(exclude=str(lookup)),
                "display": title,
            }

    # def choices(self, changelist):
    #     # Use custom template for rendering choices
    #     yield {
    #         "selected": self.value() is None,
    #         "query_string": changelist.get_query_string(remove=[self.parameter_name]),
    #         "display": _("All"),
    #     }
    #     for lookup, title in self.lookup_choices:
    #         yield {
    #             "selected": str(lookup) in self.value(),
    #             "query_string": changelist.get_query_string(
    #                 {self.parameter_name: lookup}
    #             ),
    #             "display": title,
    #         }

    # def value(self):
    #     value = super().value()
    #     if value:
    #         return value.split(",")
    #     else:
    #         return None

    # def render(self, template_name, context, renderer):
    #     # if template_name == "admin/filter.html":

    #     return super().render(template_name, context, renderer)


class ClientAdmin(ModelAdmin):
    list_display = ("id", "name")
    list_filter = [
        "groups",
        "add_at",
        "dont_call",
        ClientContactTypeFilter,
    ]
    inlines = [ClientContactDataInline, PropertyInline]
    # TODO add filter using contact info
    # Override the change_view method

    change_form_template = "admin/lead/client/change_form.html"

    def change_view(self, request, object_id, form_url="", extra_context=None):
        extra_context = extra_context or {}

        # Retrieve the ClientGroup instance
        client = self.get_object(request, object_id)
        if client:
            # Add additional context data here
            extra_context["associated_deals"] = client.deals.all()

        return super().change_view(request, object_id, form_url, extra_context)


admin.site.register(Client, ClientAdmin)
