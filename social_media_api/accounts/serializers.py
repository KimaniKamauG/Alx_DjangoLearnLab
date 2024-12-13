from rest_framework import serializers 
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model 
from django.contrib.auth import authenticate
User = get_user_model() 


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'username', 'bio', 'profile_picture']

    def create(self, validated_data):
        user = get_user_model().create_user(**validated_data)
        token, create = Token.objects.create(user=user)
        return {'user': user, 'token': token.key}
    

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')
        user = authenticate(email=email, password=password)
        if user:
            attrs['email'] = email
            return attrs
        raise serializers.ValidationError('Invalid credentials')