# backend/api/models.py

from django.db import models

class MediaLiveChannel(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    arn = models.CharField(max_length=255)
    # Ajoutez d'autres champs selon vos besoins, tels que le nom de la chaîne, les paramètres de configuration, etc.
