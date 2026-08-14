from django.contrib import admin
from .models import Contract

# Register your models here.
@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    list_display = ['pet_name', 'service', 'date', 'time', 'phone', 'created_at']
    list_filter = ['date', 'pet_type', 'service']
    search_fields = ['pet_name', 'phone', 'service']
    readonly_fields = ['created_at']
    ordering = ['-created_at']