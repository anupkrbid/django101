from django.contrib import admin

from .models import User

# Register your models here.


class UserAdmin(admin.ModelAdmin):
    # readonly_fields = ("slug",)
    prepopulated_fields = {"slug": ("name",)}
    list_filter = ("name", "age")
    list_display = ("name", "email", "age")


admin.site.register(User, UserAdmin)
