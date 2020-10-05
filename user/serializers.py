from django.db import transaction
from rest_framework import serializers

from user.models import User


class UserLoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True, write_only=True)

    class Meta:
        model = User
        fields = ('email', 'password')

    @transaction.atomic()
    def create(self, validated_data):
        email = validated_data['email']
        password = validated_data['password']

        # checking for existing users
        if User.objects.filter(email=email).exists():
            user = User.objects.get(email=email)
            # authenticating user
            if user.check_password(raw_password=password):
                return user
            else:
                raise serializers.ValidationError({'password': 'Invalid password. Please try a different password.'})
        # creating new user
        user = User.objects.create_user(email=email, password=password)
        return user
