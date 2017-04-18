from django.contrib import admin
from .models import Spots, Parked

# Register your models here.
class SpotsAdmin(admin.ModelAdmin):
    list_display = ["id", "latitude", "longitude"]
    class Meta:
        model = Spots
admin.site.register(Spots, SpotsAdmin)

class ParkedAdmin(admin.ModelAdmin):
    pass
admin.site.register(Parked, ParkedAdmin)