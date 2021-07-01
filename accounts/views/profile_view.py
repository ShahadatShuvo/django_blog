from django.urls import reverse_lazy
from django.views.generic import TemplateView
from accounts.forms import ProfileForm, UserForm
from accounts.models import Profile
from django.shortcuts import redirect, render, HttpResponseRedirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin


# Edit Profile View
class ProfileView(TemplateView):
    model = Profile
    form_class = ProfileForm
    success_url = reverse_lazy('home')
    template_name = 'accounts/profile.html'


def ProfileUpdateView(request):
    if request.method == 'POST':
        u_form = UserForm(request.POST, instance=request.user)
        p_form = ProfileForm(
            request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('profile')
    else:
        u_form = UserForm(instance=request.user)
        p_form = ProfileForm(instance=request.user.profile)

    context = {
        'user_form': u_form,
        'profile_form': p_form,
    }
    return render(request, 'accounts/profile-update.html', context)


