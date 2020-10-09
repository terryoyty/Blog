from django.contrib import admin

from .models import Post, Category, Tag


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'author', 'created_time', 'modified_time']
    fields = ['title', 'body', 'excerpt', 'category', 'tags']

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        super().save_model(request, obj, form, change)


admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Tag)


# 修改网页title和站点header。
admin.site.site_title = "Terry's Arsenal Manage"
admin.site.site_header = "Arsenal Manage"
