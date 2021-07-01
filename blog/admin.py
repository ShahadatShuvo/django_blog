from django.contrib import admin
from .models.category import Category
from .models.post import Post
from .models.post import Comment
# Register your models here.


class PostAdmin(admin.ModelAdmin):

    list_display = [
        'admin_photo',
        'title',
        'timestamp',
        'comment_count',
        'view_count',
        'featured'
    ]


admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Post, PostAdmin)