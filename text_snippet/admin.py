from django.contrib import admin

from .models import TextSnippet, Tag

admin.site.register(TextSnippet)
admin.site.register(Tag)
