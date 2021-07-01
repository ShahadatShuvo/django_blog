from django.db import models
from django.utils.translation import gettext_lazy as _
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.safestring import mark_safe
from .user_model import User


class Profile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True, unique=True
    )
    image = models.ImageField(upload_to='media/profile', default='no_pic.jpg', blank=True)

    bio = models.TextField(
        _('Bio'), blank=True, null=True
    )
    location = models.CharField(max_length=50, null=True, blank=True)
    birth_date = models.DateField(
        _('Date of Birth'), blank=True, null=True
    )
    gender = models.CharField(
        _('Gender'), max_length=1, blank=True, null=True,
        choices=[('M', 'Male'), ('F', 'Female')]
    )

    is_active = models.BooleanField(
        _('Active'), default=True, null=True
    )
    created_at = models.DateTimeField(
        _('Created At'), auto_now_add=True, null=True
    )
    last_updated = models.DateTimeField(
        _('Last Updated'), auto_now=True, null=True
    )

    def __str__(self):
        return str(self.user)

    @receiver(post_save, sender=User)
    def create_or_update_profile(sender, instance, created, **kwargs):
        """Creates or updates profile, when User object changes"""
        if created:
            Profile.objects.get_or_create(user=instance)
        instance.profile.save()

    def admin_photo(self):
        return mark_safe('<img src="{}" width="100" />'.format(self.image.url))

    admin_photo.short_description = 'Image'
    admin_photo.allow_tags = True
