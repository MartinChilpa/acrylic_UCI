from django.contrib import admin
from django.utils.html import format_html
from account.models import Account


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ['uuid', 'user', 'billing_email', 'phone', 'tax_id', 'created', 'updated']
    search_fields = ['uuid', 'user__email', 'tax_id', 'billing_email', 'phone']
    raw_id_fields = ['user']