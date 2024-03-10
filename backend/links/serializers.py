from rest_framework import serializers
from .models import URL, Redirect
from django.contrib.auth.models import User


class URLSerializer(serializers.ModelSerializer):
    class Meta:
        model = URL
        fields = ['tinyurl', 'originalUrl', 'author', 'createDatetime', 'numberOfRedirects']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class RedirectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Redirect
        fields = ['ip_address', 'datetime', 'country', 'city']
