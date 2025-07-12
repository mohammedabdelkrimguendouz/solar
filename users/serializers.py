# accounts/serializers.py
from rest_framework import serializers
from .models import User
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'user_type', 'is_active', 'phone', 'email', 'first_name', 'last_name')
        read_only_fields = ('id', 'is_active', 'phone', 'email', 'first_name', 'last_name')

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            user_type=validated_data['user_type']
        )
        return user


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):

    def validate(self, attrs):
        data = super().validate(attrs)
        data['user_type'] = self.user.user_type
        return data


class UserSerializer(serializers.ModelSerializer):
    photo = serializers.ImageField(required=False, allow_null=True)
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'user_type', 'phone', 'photo', 'is_active','first_name','last_name')
        

    def get_photo(self, obj):
        if obj.photo:
            return obj.photo.url
        return None
        
        


        
        
        
