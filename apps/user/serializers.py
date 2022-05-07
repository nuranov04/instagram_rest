from rest_framework import serializers
from apps.user.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('profile_image', 'nickname', 'first_name', 'last_name', 'bio', 'phone_number', 'email', 'password')

    def create(self, validated_data):
        password = validated_data['password']
        user = super().create(validated_data)
        user.set_password(password)
        user.save()
        return user


class UserSerializerList(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('profile_image', 'nickname', 'first_name', 'last_name', 'bio', 'phone_number', 'email')