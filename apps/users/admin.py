from datetime import datetime
import pytz
from django.contrib import admin
from . import models


class TicketAdmin(admin.ModelAdmin):
    list_display = ['name', 'time_elapsed', 'answered']
    ordering = ['-date']
    actions = ['answered']
    list_filter = [('answered', admin.BooleanFieldListFilter)]

    def answered(self, request, queryset):
        # to mark answered all selected tickets.
        objs = queryset.update(answered=True)
        self.message_user(request, 'Objects updated successfully.')
    answered.short_description = 'Change to answered.'


    @staticmethod
    def time_elapsed(obj):
        # to calculate how long time ago, the ticket was created.
        now = datetime.now(pytz.utc)
        date = obj.date.replace(tzinfo=pytz.utc)
        elapsed = now - date
        days = elapsed.days
        hours, remainder = divmod(elapsed.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        if days > 0:
            return f"{days} days, {hours} hours ago"
        elif hours > 0:
            return f"{hours} hours, {minutes} minutes ago"
        else:
            return f"{minutes} minutes ago"

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'name', 'date_joined']



admin.site.register(models.User, CustomUserAdmin)
admin.site.register(models.Ticket, TicketAdmin)
