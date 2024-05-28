from django.contrib import admin
from buyer.models import Tier


@admin.register(Tier)
class TierAdmin(admin.ModelAdmin):
    list_display = ['uuid', 'code', 'name', 'description']
