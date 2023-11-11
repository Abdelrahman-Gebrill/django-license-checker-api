from django.contrib import admin
from .models import Clients,Programs,License

class LicenseAdmin(admin.ModelAdmin):
    list_display =[
        'id',
        'client',
        'program',
        'is_active',
        'running_time',
        'total_accounts',
        'filtered_accounts',
        'final_accounts',
        'checker_accounts',
        'is_running'
    ]

admin.site.register(Clients)
admin.site.register(Programs)
admin.site.register(License,LicenseAdmin)

# Register your models here.
