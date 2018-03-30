from django.contrib import admin
from userapp.models import *

# Register your models here.
admin.site.register(user)
admin.site.register(vehicle)
admin.site.register(userVehicleOwnership)
admin.site.register(userRegister)