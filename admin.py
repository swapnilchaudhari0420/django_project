from django.contrib import admin
from  .models import register_table, appointment_table

# Register your models here.
admin.site.register(register_table)
admin.site.register(appointment_table)
