from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Items)

admin.site.register(Jobs)
admin.site.register(Address)
admin.site.register(ConForm_Orders)


class TypeAdmin(admin.ModelAdmin):
	list_display = ["name","types","price"]


admin.site.register(Types,TypeAdmin)