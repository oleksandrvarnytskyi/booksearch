from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from books.models import Node, Page

admin.site.register(Node, MPTTModelAdmin)


class PageAdmin(admin.ModelAdmin):
    list_display = ('page_number', 'node')


admin.site.register(Page, PageAdmin)
