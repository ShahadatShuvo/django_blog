from django.shortcuts import (
    render,
    redirect,
    reverse,
    get_object_or_404
)
from blog.forms import PostForm
from blog.models.post import Post
from .post_create_view import get_author


def post_update(request, id):
    title = 'update'
    post = get_object_or_404(Post, id=id)
    form = PostForm(request.POST or None, request.FILES or None, instance=post)
    author = get_author(request.user)
    if request.method == 'POST':
        if form.is_valid():
            form.instance.user = author
            form.save()
            return redirect(reverse('post-view', kwargs={
                'id': form.instance.id
            }))

    context = {
        'form': form,
        'title': title
    }
    return render(request, 'post_create.html', context)
