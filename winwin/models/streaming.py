from django.db import models
from django.conf import settings

class LiveSession(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    theme = models.CharField(max_length=50, choices=[('education', 'Education'), ('business', 'Business'), ('health', 'Health'), ('technology', 'Technology'), ('other', 'Other')])
    is_private = models.BooleanField(default=False)
    start_time = models.DateTimeField()
    streamer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
