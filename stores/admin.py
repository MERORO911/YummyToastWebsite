from django.contrib import admin
from .models import Store

class StoreAdmin(admin.ModelAdmin):
  list_display = ("storename",  "city", "address", "tel")



admin.site.register(Store, StoreAdmin)

