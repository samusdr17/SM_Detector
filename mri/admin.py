from django.contrib import admin
from .models import MriDdbb


# Register your models here.

class MriAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')

admin.site.register(MriDdbb, MriAdmin)