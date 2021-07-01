from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

from blog.views import (
    indexView,
    blogView,
    postView,
    post_create,
    post_update,
    post_delete,
)
from accounts.views import (
    SignUpView,
    password_reset_request,
    ProfileView,
    ProfileUpdateView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ckeditor', include('ckeditor_uploader.urls')),

    # Blog urls
    path('', indexView, name='home-view'),
    path('blog/', blogView, name='blog-view'),
    path('create/', post_create, name='post-create'),
    path('post/<id>/', postView, name='post-view'),
    path('post/<id>/update/', post_update, name='post-update'),
    path('post/<id>/delete/', post_delete, name='post-delete'),

    # User Signup, Login, Logout, Password Reset
    path('signup/', SignUpView.as_view(), name='signup'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('profile_update', ProfileUpdateView, name='profile-update'),
    path('login/', auth_views.LoginView.as_view(
        template_name='accounts/login.html'
    ), name='login'),
    path('logout/', auth_views.LogoutView.as_view(
        next_page='home-view'
    ), name='logout'),
    path('change-password/',
         auth_views.PasswordChangeView.as_view(
            template_name='accounts/change-password.html',
            success_url='/login'
        ),
        name='change_password'
    ),

    # password reset
    path('password_reset', password_reset_request, name="password_reset"),
    path('password_reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='accounts/password/password_reset_done.html'),
         name='password_reset_done'
         ),
    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name="accounts/password/password_reset_confirm.html"),
         name='password_reset_confirm'),
    path('reset/done/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='accounts/password/password_reset_complete.html'),
         name='password_reset_complete'),


]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)