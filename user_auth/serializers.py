from dj_rest_auth.serializers import LoginSerializer
from rest_framework import serializers


class CustomLoginSerializer(LoginSerializer):
    user_id = serializers.IntegerField(source='user.id', read_only=True)
    username = serializers.CharField(source='user.username', read_only=True)

    def to_representation(self, instance):
        response_data = super().to_representation(instance)
        response_data['user_id'] = self.user.id
        response_data['username'] = self.user.username
        return response_data
