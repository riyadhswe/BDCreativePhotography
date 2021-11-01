from django.contrib import admin
from app.models import *
# Register your models here.
class contactadmin(admin.ModelAdmin):
    list_display = ['name','email','subject','message']

admin.site.register(title)
admin.site.register(contact,contactadmin)
admin.site.register(subcribe)
