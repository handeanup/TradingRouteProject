from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import ugettext_lazy as _
from django.conf import settings


class User(AbstractUser):
    phone = PhoneNumberField(null=False, blank=False, unique=True)
    email = models.EmailField(null=False, blank=False, unique=True)

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def get_full_name(self):
        return '%s %s' % (self.first_name, self.last_name)

    def get_short_name(self):
        return self.first_name

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE,
                                related_name='profile')
    dob = models.DateField()
    address = models.CharField(max_length=255, blank=True,
                               default='')
    country = models.CharField(max_length=50, blank=True)
    city = models.CharField(max_length=50, blank=True)
    zip = models.CharField(max_length=5, blank=True)
    photo = models.ImageField(upload_to='uploads', blank=True)
