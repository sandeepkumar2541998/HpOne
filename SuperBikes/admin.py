from django.contrib import admin
from .models import Newcar,Recommended,Supercars,Carbrands
# Register your models here.
admin.site.register(Newcar)
admin.site.register(Recommended)
admin.site.register(Supercars)
admin.site.register(Carbrands)