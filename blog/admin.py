from django.contrib import admin
from django.utils.safestring import mark_safe


from blog.models import Post, Tag, Category, Review


class PostsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'category', 'created_date', 'updated_date', 'views', 'draft', 'get_photo')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'author')
    list_editable = ('draft',)
    list_filter = ('draft', 'category')
    readonly_fields = ('get_photo', 'created_date', 'updated_date', 'views')
    prepopulated_fields = {"url": ("title",)}

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="75">')

    get_photo.short_description = 'photo'


class TagsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'url')
    list_display_links = ('id', 'title', 'url')
    search_fields = ('title',)
    prepopulated_fields = {"url": ("title",)}


class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'url')
    list_display_links = ('id', 'title', 'url')
    search_fields = ('title',)
    prepopulated_fields = {"url": ("title",)}


class ReviewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_name', 'post')
    list_display_links = ('user_name', 'post')
    search_fields = ('user_name',)
    readonly_fields = ('post',)


admin.site.register(Post, PostsAdmin)
admin.site.register(Tag, TagsAdmin)
admin.site.register(Category, CategoriesAdmin)
admin.site.register(Review, ReviewsAdmin)
