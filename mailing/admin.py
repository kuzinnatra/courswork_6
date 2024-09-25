from django.contrib import admin

from mailing.models import Client


# Register your models here.
@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('email_client', 'name',)
    list_filter = ('email_client',)
    search_fields = ('email_client',)
