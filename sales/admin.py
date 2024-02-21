from django.contrib import admin
from .models import *
# Register your models here.
# TODO verify total sales man commotions not higher than total commotion

class SalesManCommotionInline(admin.TabularInline):
    model = SalesManCommotion
    extra = 1

class DealAdmin(admin.ModelAdmin):
    list_display = ('id',"status","commotion","created_at","last_update")
    date_hierarchy = 'created_at'
    list_filter = ("sales_man_commotion", "commotion")
    inlines=[SalesManCommotionInline]
admin.site.register(Deal, DealAdmin)

@admin.register(SalesManProfile)
class SalesManProfileAdmin(admin.ModelAdmin):
    pass
