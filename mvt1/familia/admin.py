from django.contrib import admin
from .models import Familiar

class FamiliarAdmin(admin.ModelAdmin):

    list_display = ('nombre', 'apellido', 'nacimiento')



    

admin.site.register(Familiar, FamiliarAdmin)
