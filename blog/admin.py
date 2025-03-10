from django.contrib import admin
from .models import Publication

# Register your models here.
class PublicationAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'body')
    search_fields = ('title', 'author__username', 'body')
    list_filter = ('title', 'author__username')
admin.site.register(Publication, PublicationAdmin)
