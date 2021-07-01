from django.shortcuts import (
    redirect,
    get_object_or_404
)
from blog.models.post import Post


def post_delete(request, id):
    post = get_object_or_404(Post, id=id)
    post.delete()
    return redirect('blog-view')