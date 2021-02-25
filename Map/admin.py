from django.contrib import admin
from .models import Place, Request

# Register your models here.
class PlaceAdmin(admin.ModelAdmin):
    pass
class RequestAdmin(admin.ModelAdmin):
    pass
admin.site.register(Place, PlaceAdmin)
admin.site.register(Request, RequestAdmin)