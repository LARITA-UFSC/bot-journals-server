from django.contrib import admin
from .models import Documents, Rawdata


@admin.register(Documents)
class DocumentsAdmin(admin.ModelAdmin):
    list_filter = ['journal']
    search_fields = ['title', 'keywords', 'summary']
    readonly_fields = ['title', 'authors', 'keywords',
                       'summary', 'url_view', 'url_pdf', 'journal']

    def has_delete_permission(self, request, obj=None):
        return False

    def changeform_view(self, request, object_id=None, form_url='', extra_context=None):
        extra_context = extra_context or {}
        extra_context['show_save_and_continue'] = False
        extra_context['show_save'] = False
        return super(YourModelAdmin, self).changeform_view(request, object_id extra_context=extra_context)


@admin.register(Rawdata)
class RawdataAdmin(admin.ModelAdmin):
    pass
