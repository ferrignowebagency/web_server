from django.contrib import admin
from .models import Agency


class MyCustomAdmin(admin.ModelAdmin):
    list_display = ('id','name','created_at','created_by')  # fields to display in the listing
    empty_value_display = '-empty-'        # display value when empty 
    list_filter = ('name', 'agents')      # enable results filtering
    list_per_page = 25                     # number of items per page 
    ordering = ['created_at']       # Default results ordering

# and register it 



admin.site.register(Agency,MyCustomAdmin)
# Register your models here.

