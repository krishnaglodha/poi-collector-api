from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import serializers
from .models import AppUser
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

class CustomTokenSerializer(TokenObtainPairSerializer):
    """
    Customize JWT token creation response to add user category, username and whether user is supueruser or not.
    """
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username
        token['is_superuser'] = user.is_superuser
        token['category'] = user.category
        
        return token
    


class RegisterSerializer(serializers.ModelSerializer):
    """
    Serializer for user registration.
    """
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=AppUser.objects.all())]
            )

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = AppUser
        fields = ('email', 'password', 'password2')
      
    # validate password and confirm password
    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    # Create new user
    def create(self, validated_data):
        user = AppUser.objects.create(
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()

        return user