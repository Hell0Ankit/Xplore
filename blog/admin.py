from django.contrib import admin
from .models import Category, Blog


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "category_name", "update_at", "update_at")


class BlogAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "category",
        "author",
        "blog_image",
        "status",
        "create_at",
        "is_featured",
    )  # display karega table view me
    search_fields = (
        "id",
        "title",
        "category__category_name",
        "status",
    )  # Search option show  karega
    prepopulated_fields = {"slug": ("title",)}  #  Auto slug in admin
    list_editable = ("is_featured",)


# Register your models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register(Blog, BlogAdmin)
