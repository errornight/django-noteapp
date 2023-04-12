from datetime import datetime
import pytz
from django.contrib import admin
from . import models

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'color']

class NotesAdmin(admin.ModelAdmin):
    list_display = ['title', 'owner', 'category', 'uuid', 'time_elapsed', 'public']
    list_filter = [('public', admin.BooleanFieldListFilter)]
    search_fields = ['title', 'body', 'short_desc', 'owner__username', 'category__title']   # searchbar in admin panel.

    @staticmethod
    def time_elapsed(obj):
        # to calculate elapsed time.
        now = datetime.now(pytz.utc)
        date = obj.updated.replace(tzinfo=pytz.utc)
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




admin.site.register(models.Category, CategoryAdmin)
admin.site.register(models.Note, NotesAdmin)
