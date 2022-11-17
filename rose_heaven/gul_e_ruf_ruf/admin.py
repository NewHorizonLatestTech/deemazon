from django.contrib import admin

# Register your models here.
from .models import customer
admin. site.register(customer)


from .models import foodpackage
admin. site.register(foodpackage)