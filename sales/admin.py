from django.contrib import admin
from .models import *
from unfold.admin import ModelAdmin

# Register your models here.
# TODO verify total sales man commotions not higher than total commotion

class SalesManCommotionInline(admin.TabularInline):
    model = SalesManCommotion
    extra = 1

class DealAdmin(ModelAdmin):
    list_display = (
        "id",
        "deal_property",
        "status",
        "commotion",
        "created_at",
        "last_update",
    )
    date_hierarchy = 'created_at'
    list_filter = ("sales_man_commotion", "commotion")
    inlines=[SalesManCommotionInline]
admin.site.register(Deal, DealAdmin)

@admin.register(SalesManProfile)
class SalesManProfileAdmin(ModelAdmin):
    list_display = ["user","first_name","last_name","created_at","last_update","active"]

    list_editable = ['active']
    def first_name(self,obj,*args, **kwargs):
        return obj.user.first_name
    
    def last_name(self,obj,*args, **kwargs):
        return obj.user.last_name