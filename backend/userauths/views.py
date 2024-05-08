from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.mixins import RetrieveModelMixin, UpdateModelMixin
from rest_framework.viewsets import GenericViewSet
from rest_framework.decorators import action
from userauths.models import User, Profile
from userauths.serializers import (
    MyTokenObtainPairSerializer, 
    RegisterSerializer,
    UserSerializer,
    ProfileSerializer,
    EmailVerificationUserSerializer,
    verifyPhoneSerializers,
)
from django.shortcuts import get_object_or_404
from django.conf import settings
import random
import shortuuid
from kavenegar import *
from kavenegar import *

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


def generate_otp_email():
    uuid_key = shortuuid.uuid()
    unique_key = uuid_key[:6]
    return unique_key


def generate_otp_sms():
    otp = ''.join(random.choices('0123456789', k=6))
    return otp


class Email_Verification(generics.RetrieveAPIView):
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer
    def get_object(self):
        email = self.kwargs['email']
        user = User.objects.get(email=email)

        if user:
            user.otp = generate_otp_email()
            user.save()

            uidb64=user.pk
            otp = user.otp

            link = f"http://localhost:8000/email-verification?otp={otp}&uidb64={uidb64}"

            print("link====",link)
        return user


class Phone_Verification_send_sms(generics.RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer
    def get_object(self):
        user = self.request.user
        

        if user and user.is_verify_phone==False:
            user.otp = generate_otp_sms()
            user.save()
            message = f"سلام کد تایید شما {user.otp} می باشد."
            self.send_sms(user.phone, message)

        return user

    def send_sms(self, receivers, message):
        api_key = settings.KAVENEGAR_API_KEY
        try:
            api = KavenegarAPI(api_key)
            params = {
                'sender': '10006926',
                'receptor': str(receivers),
                'message': message,
            } 
            response = api.sms_send(params)
            print(response)
        except APIException as e: 
            print(e)
        except HTTPException as e: 
            print(e)


class Phone_Verification(generics.UpdateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = verifyPhoneSerializers

    def get_object(self):
        user = self.request.user
        return user
    
    def post(self, request, *args, **kwargs):
        user = self.get_object()
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        if user.otp == serializer.validated_data.get('otp'):
            user.is_verify_phone = True
            user.save()

            return Response(serializer.data)
        else:
            return Response({'detail': 'Invalid OTP or unauthorized user.'}, status=status.HTTP_400_BAD_REQUEST)

class PasswordResetEmailVerify(generics.RetrieveAPIView):
    permission_classes = (AllowAny,)
    serializer_class = EmailVerificationUserSerializer

    def get_object(self):
        email = self.kwargs['email']
        user = User.objects.get(email=email)

        if user:
            user.otp = generate_otp_email()
            user.save()

            uidb64=user.pk
            otp = user.otp
            
            link = f"http://localhost:5173/create-new-password?otp={otp}&uidb64={uidb64}"

            print("link====",link)
        return user
    


class PasswordChangedView(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer
    
    def create(self, request, *args, **kwargs):
        payload = request.data

        otp = payload['otp']
        uidb64 = payload['uidb64']

        # Debugging: Print uidb64 value
        print("Received uidb64:", uidb64)
        print("Received otp:", otp)

        try:
            user_id = int(uidb64)

            user = User.objects.get(otp=otp, id=user_id)

            # Change user's password
            password = payload['password']
            user.set_password(password)
            user.otp = ""
            user.save()

            message = {"message": "Password changed successfully"}
            return Response(message, status=status.HTTP_201_CREATED)

        except (User.DoesNotExist, ValueError) as e:
            message = {"message": "User does not exist or invalid identifier"}
            return Response(message, status=status.HTTP_404_NOT_FOUND)
        
        
class ProfileViewSet(RetrieveModelMixin, UpdateModelMixin, GenericViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    
    @action(detail=False, methods=['GET', 'PUT'])
    def me(self, request):
        profile = Profile.objects.get(user_id=request.user.id)
        if request.method == 'GET':
            serializer = ProfileSerializer(profile)
            return Response(serializer.data)
        elif request.method == 'PUT':
            serializer = ProfileSerializer(profile, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
        

# async def sending_sms(receivers,message):
#     print(receivers,message)
#     api_key = 
#     try:
#         api = KavenegarAPI(api_key, timeout=20)
#         params = {
#             'sender': '10006926',
#             'receptor': str(receivers),
#             'message': message,
#         } 
#         response = api.sms_send(params)
#         print(response)
#     except APIException as e: 
#         print(e)
#     except HTTPException as e: 
#         print(e)


