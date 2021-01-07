from django.contrib import admin
from .models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin

## Category
class CategoryResouces(resources.ModelResource):
    class Meta:
        model = Category

class CategoryAdmin( ImportExportModelAdmin,admin.ModelAdmin):
    search_fields= ['name']
    list_display = ('name', 'state', 'creationDate',)
    list_editable = ['state']
    resource_class = CategoryResouces

admin.site.register(Category, CategoryAdmin)

# Contry
class CityResouces(resources.ModelResource):
    class Meta:
        model = Contry

class CityAdmin( ImportExportModelAdmin,admin.ModelAdmin):
    search_fields= ['name']
    list_display = ('name',)
    resource_class = CityResouces

admin.site.register(Contry, CityAdmin)

## Autor
class AutorResouces(resources.ModelResource):
    class Meta:
        model = Autor

class AutorAdmin( ImportExportModelAdmin, admin.ModelAdmin):
    search_fields= ['name', 'lastName']
    list_display = ('name', 'lastName', 'facebook', 'twitter', 'instagram', 'email', 'state', 'creationDate',)
    list_editable = ['state']
    resource_class = AutorResouces

admin.site.register(Autor, AutorAdmin)

# Post
class PostResouces(resources.ModelResource):
    class Meta:
        model = Post

class PostAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields= ['title', 'description']
    list_display = ('title', 'slug', 'autor', 'category', 'state', 'creationDate', 'time',)
    list_editable = ['state', 'category']
    resource_class = PostResouces

admin.site.register(Post, PostAdmin)

# Lige
class LigueResouces(resources.ModelResource):
    class Meta:
        model = Ligue

class LigueAdmin( ImportExportModelAdmin,admin.ModelAdmin):
    search_fields= ['name']
    list_display = ('name', 'state',)
    list_editable = ['state']
    resource_class = LigueResouces

admin.site.register(Ligue, LigueAdmin)

# Discipline
class DisciplineResouces(resources.ModelResource):
    class Meta:
        model = Discipline

class DisciplineAdmin( ImportExportModelAdmin,admin.ModelAdmin):
    search_fields= ['name']
    list_display = ('name', 'state',)
    list_editable = ['state']
    resource_class = DisciplineResouces

admin.site.register(Discipline, DisciplineAdmin)
