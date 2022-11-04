from django.contrib import admin
from .models import Ad, Category
from import_export import resources
from import_export.admin import ImportExportModelAdmin


class AdResource(resources.ModelResource):
    class Meta:
        model = Ad


class AdAdmin(ImportExportModelAdmin):
    resource_class = AdResource


class CategoryResource(resources.ModelResource):
    class Meta:
        model = Category


class CategoryAdmin(ImportExportModelAdmin):
    resource_class = CategoryResource


admin.site.register(Ad, AdAdmin)
admin.site.register(Category, CategoryAdmin)
