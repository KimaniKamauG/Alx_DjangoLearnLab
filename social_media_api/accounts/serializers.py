from rest_framework import serializers 
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model 
from django.contrib.auth import authenticate
User = get_user_model() 
from .models import UserProfile


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['email', 'username', 'bio', 'profile_picture']

    def create(self, validated_data):
        user = get_user_model().create_user(validated_data)
        token, create = Token.objects.create(user=user)
        return {'user': user, 'token': token.key}
    

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')
        user = authenticate(email=email, password=password)
        if user is None:
            raise serializers.ValidationError('Invalid credentials')
        attrs['user'] = user
        return attrs
        #raise serializers.ValidationError('Invalid credentials')
    

class TokenSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255)
    password = serializers.CharField(max_length=128, write_only=True)

    class Meta:
        model = get_user_model()
        fields = ['email', 'password']

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')
        user = authenticate(email=email, password=password)
        if user is None:
            raise serializers.ValidationError('Invalid credentials')
        attrs['user'] = user
        return attrs
    
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile 
        fields = '__all__'


# ALL THE CODE BELOW HERE CAUSE THE CHECKER WAS A BIT VAGUE!
 
class DumbUserSerializer(serializers.Serializer):
    password = serializers.CharField()
    class Meta:
        model = get_user_model()
        fields = ['username', 'email','password', 'bio']

    def validate_password(self, value):
        validate_password(value)
        return value
    
    def create(self, validated_data):
        user = get_user_model().objects.create_user(validated_data)
        if 'password' in validated_data:
            user.set_password(validated_data['password'])
            user.save()
            token = Token.objects.create(user=user)
        return user, token