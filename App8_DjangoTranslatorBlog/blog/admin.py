from django.contrib import admin
from .models import Division,Item,Inventory
# Register your models here.

class ItemAdmin(admin.ModelAdmin):
    list_display=('division','name','quantity')
class InventoryAdmin(admin.ModelAdmin):
    list_display=('name','type','quantity','date_created')

admin.site.register(Division)
admin.site.register(Item,ItemAdmin)
admin.site.register(Inventory,InventoryAdmin)
