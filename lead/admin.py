from django.contrib import admin
from .models import *
# Register your models here.



class ClientGroupAdmin(admin.ModelAdmin):
    list_display = ('id','name')
    list_select_related = ['clients']
    # TODO show all clients
admin.site.register(ClientGroup, ClientGroupAdmin)

class ClientContactDataInline(admin.StackedInline):
    model = ClientContactData
    min_num = 1
    extra=1
class ClientAdmin(admin.ModelAdmin):
    list_display = ('id',"name")
    list_filter = ["groups","add_at","dont_call"]
    inlines = [ClientContactDataInline]
    # TODO add filter using contact info
admin.site.register(Client, ClientAdmin)

#TODO list all deals client have