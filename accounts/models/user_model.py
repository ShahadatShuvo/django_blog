from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator


from accounts.managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), blank=True)
    phone = models.CharField(
        _('Mobile Phone'), max_length=12, unique=True,
        validators=[RegexValidator(r'^[\d]{10,12}$',
                                   message='Format (ex: 01234567890)'
                                   )])
    first_name = models.CharField(
        _('First Name'), max_length=255, blank=True, null=True
    )

    last_name = models.CharField(
        _('Last Name'), max_length=255, blank=True, null=True
    )
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    admin = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def get_full_name(self):
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        return self.first_name

    def __str__(self):
        return self.phone
