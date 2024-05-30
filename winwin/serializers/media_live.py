# backend/api/serializers.py

from rest_framework import serializers
from winwin.models.media_live import MediaLiveChannel

class MediaLiveChannelSerializer(serializers.ModelSerializer):
    class Meta:
        model = MediaLiveChannel
        fields = '__all__'
