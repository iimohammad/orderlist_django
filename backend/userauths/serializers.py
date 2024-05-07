from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import Token
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from userauths.models import Profile, User
from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer
from djoser.serializers import UserSerializer as BaseUserSerializer

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token= super().get_token(user)

        token['full_name'] = user.full_name
        token['email'] = user.email
        token['username'] = user.username

        try:
            token['vendor_id'] = user.vendor.id
        except AttributeError:
            token['vendor_id'] = 0

        return token
    

class RegisterSerializer(BaseUserCreateSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta(BaseUserCreateSerializer.Meta):
        model = User
        fields = [ 'full_name', 'email', 'phone', 'password', 'password2']

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password does not match"})
        return attrs
    
    def create(self, validated_data):
        validated_data.pop('password2')
        email = validated_data.get('email', '')

        if '@' not in email:
            raise ValidationError("Invalid email format")

        user = User.objects.create(
            full_name=validated_data['full_name'],
            email=email,
            phone=validated_data['phone'],
        )

        user.set_password(validated_data['password'])
        user.save()
        return user

class UserSerializer(BaseUserSerializer):
    
    class Meta(BaseUserSerializer.Meta):
        model = User
        fields = ['id', 'username', 'email', 'full_name', 'phone']


class EmailVerificationUserSerializer(BaseUserSerializer):
    class Meta:
        model = User
        fields = '__all__'


class ProfileSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(read_only=True)
    full_name = serializers.CharField(read_only=True)

    class Meta:
        model = Profile
        fields = [
            'user_id', 'full_name', 'about', 'gender', 'country',
            'state', 'city', 'address', 'date', 'company_name',
            'company_phone_number', 'company_email',
            'membership', 'formal_status']

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['user'] = UserSerializer(instance.user).data
        return response
