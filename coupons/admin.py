from django.contrib import admin
from .models import Discount
# Register your models here.

class DiscountAdmin(admin.ModelAdmin):
    list_display = ['discount', 'active']
    list_filter  = ['active']

admin.site.register(Discount, DiscountAdmin)
