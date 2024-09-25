from django.contrib import admin

from mailing.models import Client, Letter


# Register your models here.
@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('email_client', 'name',)
    list_filter = ('email_client',)
    search_fields = ('email_client',)


@admin.register(Letter)
class LetterAdmin(admin.ModelAdmin):
    list_display = ('title', 'body',)
    list_filter = ('title',)
    search_fields = ('title',)