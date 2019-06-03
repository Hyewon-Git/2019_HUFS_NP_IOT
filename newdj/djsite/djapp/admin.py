from django.contrib import admin
from .models import Searchdb
# Register your models here.
class SarchdbAdmin(admin.ModelAdmin):
    list_display = ("timedata","distance",)
admin.site.register(Searchdb,SarchdbAdmin)