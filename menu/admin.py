from django.contrib import admin
from menu.models import *

# Register your models here.
class ItemInAdmin(admin.ModelAdmin):
	fields = ['father', 'title', 'text']
	list_display = ('father', 'title', 'text')

admin.site.register(Item, ItemInAdmin)