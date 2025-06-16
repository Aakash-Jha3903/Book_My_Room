#accounts/admin.py
from django.contrib import admin
from .models import HotelUser, HotelVendor, Ameneties, Hotel, HotelImages, HotelManager

admin.site.register(HotelUser)
admin.site.register(HotelVendor)
admin.site.register(Ameneties)
admin.site.register(Hotel)
admin.site.register(HotelImages)
admin.site.register(HotelManager)
