from django.contrib import admin
from .models import TV, Refrigerator, Phone, Laptop, WashingMachine


@admin.register(TV)
class TVAdmin(admin.ModelAdmin):
    pass

@admin.register(Refrigerator)
class RefrigeratorAdmin(admin.ModelAdmin):
    pass

@admin.register(Phone)
class PhoneAdmin(admin.ModelAdmin):
    pass

@admin.register(Laptop)
class LaptopAdmin(admin.ModelAdmin):
    pass

@admin.register(WashingMachine)
class WashingMachineAdmin(admin.ModelAdmin):
    pass
