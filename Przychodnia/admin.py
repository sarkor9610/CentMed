from django.contrib import admin
from .models import Pacjenci
from .models import Lekarze
from .models import Wizyty

# Register your models here.

admin.site.register(Pacjenci)
admin.site.register(Lekarze)
admin.site.register(Wizyty)
