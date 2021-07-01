from django.shortcuts import (
    render,
    redirect,
    reverse
)
from accounts.models import Profile
from blog.forms import PostForm


def get_author(user):
    qs = Profile.objects.filter(user=user)
    if qs.exists():
        return qs[0]
    return None


def post_create(request):
    title = 'create'
    form = PostForm(request.POST or None, request.FILES or None)
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
        'title': title,
    }
    return render(request, 'post_create.html', context)
