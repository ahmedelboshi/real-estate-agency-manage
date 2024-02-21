from django.contrib import admin
from .models import Country , Governorate , City
from unfold.admin import ModelAdmin

class GovernorateInline(admin.StackedInline):
    model = Governorate
    extra=1

class Admin_Country(ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    inlines=[GovernorateInline]
admin.site.register(Country ,Admin_Country)


class CityInline(admin.StackedInline):
    model = City
    extra = 1


class Admin_Governorate(ModelAdmin):
    list_display = ('name',)
    list_filter = ('country',)
    search_fields =('name',)

    inlines=[CityInline]

admin.site.register(Governorate , Admin_Governorate)

class Admin_City(ModelAdmin):
    list_display = ('name',)
    list_filter = ('governorate',)
    search_fields = ('name',)

admin.site.register(City , Admin_City)
