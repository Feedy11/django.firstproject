from django.contrib import admin
from .models import Employee

# Register your models here.

class MonModelAdmin(admin.ModelAdmin):
    pass


admin.site.register(Employee,MonModelAdmin)