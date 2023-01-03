from django.contrib import admin
from .models import Blog, Category
from django.utils.safestring import mark_safe
# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    list_display = ("title", "is_active", "is_home", "slug", "selected_categories")
    list_editable = ("is_active", "is_home")
    search_fields = ("title", "description")
#    readonly_fields = ("description") description kismini sadece okunabilir olarak degistirdi
    readonly_fields=("slug",)
    list_filter = ("is_active", "is_home", "categories")
    
    def selected_categories(self, obj):
        html = ""
        for category in obj.categories.all():
            html += category.name + " "
            html += "</br>"
        return mark_safe(html)
    
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")

admin.site.register(Blog, BlogAdmin)
admin.site.register(Category, CategoryAdmin)
    
    