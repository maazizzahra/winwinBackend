from django.db import models
from django.conf import settings

class BrandPartnership(models.Model):
    streamer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    brand_name = models.CharField(max_length=255)
    product_description = models.TextField()
    compensation = models.DecimalField(max_digits=8, decimal_places=2)
    agreement_signed = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.streamer} - {self.brand_name}'
