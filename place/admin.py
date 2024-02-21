from django.contrib import admin
from .models import Country , Governorate , City

class GovernorateInline(admin.StackedInline):
    model = Governorate
    extra=1

class Admin_Country(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    inlines=[GovernorateInline]
admin.site.register(Country ,Admin_Country)


class CityInline(admin.StackedInline):
    model = City
    extra = 1


class Admin_Governorate(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('country',)
    search_fields =('name',)

    inlines=[CityInline]

admin.site.register(Governorate , Admin_Governorate)

class Admin_City(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('governorate',)
    search_fields = ('name',)

admin.site.register(City , Admin_City)
