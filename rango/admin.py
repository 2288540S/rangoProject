from django.contrib import admin

from rango.models import Page, Category, UserProfile


class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url')

# Added in this class to customise the Admin Interface.
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

# Updated the registration to include this customised interface.
admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)


