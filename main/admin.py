from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(HouseHolder)
admin.site.register(House)
admin.site.register(Car)
admin.site.register(Repair)
admin.site.register(Bill)
admin.site.register(Staff)
admin.site.register(Profile)
admin.site.register(Billboard)
admin.site.register(RelHouseHolder)
admin.site.register(RelCarHolder)
admin.site.register(RelHouseholderRepair)
admin.site.register(RelStaffProfile)
