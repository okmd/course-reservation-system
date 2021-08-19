from django.db import models
from django.contrib.auth.models import User, AbstractUser
from .CustomManager import CustomUserManager


class CustomUser(AbstractUser):

    username = None
    is_student = models.BooleanField(blank=True)
    email = models.EmailField(unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    def __str__(self):
        return self.email
        
