from django.contrib import admin
from .models import Char_Model,Combat, MyModel


# Register your models here.
admin.site.register(Char_Model)
admin.site.register(Combat)
admin.site.register(MyModel)