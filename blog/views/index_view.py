from django.shortcuts import render
from blog.models import Post
from emails.models import Signup


def indexView(request):
    featured = Post.objects.filter(featured=True)
    latest = Post.objects.order_by('-timestamp')[0:6]
    latest3 = Post.objects.order_by('-timestamp')[0:3]

    if request.method == 'POST':
        email = request.POST['email']
        new_signup = Signup()
        new_signup.email = email
        new_signup.save()

    context = {
        'object_list': featured,
        'latest': latest,
        'latest3': latest3,
    }
    return render(request, 'index.html', context)