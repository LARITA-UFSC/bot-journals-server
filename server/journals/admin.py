from django.contrib import admin
from .models import Documents, Rawdata


class CustomPropertiesMixinAdmin():

    def get_readonly_fields(self, request, obj=None):
        if obj:
            self.readonly_fields = [
                field.name for field in obj.__class__._meta.get_fields()]
        return self.readonly_fields


@admin.register(Documents)
class DocumentsAdmin(admin.ModelAdmin, CustomPropertiesMixinAdmin):
    list_filter = ('title', 'summary', 'journal')


@admin.register(Rawdata)
class RawdataAdmin(admin.ModelAdmin, CustomPropertiesMixinAdmin):
    pass