from django.contrib import admin
from .models import FixRequest, Photo, Status


@admin.register(FixRequest)
class FixRequestAdmin(admin.ModelAdmin):
    pass


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    pass


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    pass
