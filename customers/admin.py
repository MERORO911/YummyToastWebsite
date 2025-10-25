from django.contrib import admin
from .models import Customer

# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
  list_display = ("firstname", "lastname", "joined_date","age", "cus", "tel")

admin.site.register(Customer, CustomerAdmin)




