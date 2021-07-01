from django.shortcuts import (
    render,
    get_object_or_404,
    redirect
)
from blog.models.post import Post
from .category_count_view import get_category_count
from blog.forms import CommentForm


def postView(request, id):
    category_count = get_category_count()
    latest_post = Post.objects.order_by('-timestamp')[0:3]
    post = get_object_or_404(Post, id=id)
    form = CommentForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.instance.user = request.user
            form.instance.post = post
            form.save()
            return redirect(post, id=id)
    context = {
        'post': post,
        'category_count': category_count,
        'latest_post': latest_post,
        'form': form,
    }
    return render(request, 'post.html', context)
