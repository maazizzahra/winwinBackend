# authentication/models.py
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class User(AbstractUser):
    # Ajoutez les champs spécifiques à votre application utilisateur ici
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    is_streamer = models.BooleanField(default=False)
    is_user_sponsor = models.BooleanField(default=False)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, unique=True, default='')
    # Spécifiez des noms inverses personnalisés pour éviter les conflits
    groups = models.ManyToManyField(Group, verbose_name='groups', blank=True, related_name='user_groups')
    user_permissions = models.ManyToManyField(Permission, verbose_name='user permissions', blank=True, related_name='user_permissions')

    def __str__(self):
        return self.username
