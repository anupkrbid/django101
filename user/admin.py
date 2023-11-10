from django.contrib import admin

from .models import User, PhoneNo, Passport, Access

# Register your models here.


class UserAdmin(admin.ModelAdmin):
    # readonly_fields = ("slug",)
    prepopulated_fields = {"slug": ("name",)}
    list_filter = ("name", "age")
    list_display = ("id", "name", "email", "age")


class PhoneNoAdmin(admin.ModelAdmin):
    list_display = ("id", "country_code", "number", "user")


admin.site.register(User, UserAdmin)
admin.site.register(PhoneNo, PhoneNoAdmin)
admin.site.register(Passport)
admin.site.register(Access)
