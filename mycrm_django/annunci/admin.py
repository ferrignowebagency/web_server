from django.contrib import admin


from .models import Annunci


class MyCustomAdmin(admin.ModelAdmin):
    list_display = ('id','title','created_at','created_by')  # fields to display in the listing
    empty_value_display = '-empty-'        # display value when empty 
    list_filter = ('title', 'company')      # enable results filtering
    list_per_page = 25                     # number of items per page 
    ordering = ['modified_at', 'created_at']       # Default results ordering

# and register it 



admin.site.register(Annunci,MyCustomAdmin)
# Register your models here.
