from django.db import models
from django.contrib.auth.models import AbstractUser
from shortuuid.django_fields import ShortUUIDField
from django.db.models.signals import post_save


class User(AbstractUser):
    username = models.CharField(unique=True, max_length=100)
    email = models.EmailField(unique=True, null=False, blank=False)
    is_verify_email = models.BooleanField(default=False)
    full_name = models.CharField(max_length=100, null=False, blank=False)
    phone = models.CharField(max_length=100,unique=True, null=False, blank=False)
    is_verify_phone = models.BooleanField(default=False)
    otp = models.CharField(max_length=100, null=True, blank=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email
    
    def save(self, *args, **kwargs):
        email_username, _ = self.email.split("@")
        if not self.full_name:
            self.full_name = email_username
        if not self.username:
            self.username = email_username

        super().save(*args, **kwargs)
        
        
class Membership(models.Model):
    
    # Types of Membership
    MEMBERSHIP_FREE = 'F'
    MEMBERSHIP_BRONZE = 'B'
    MEMBERSHIP_SILVER = 'S'
    MEMBERSHIP_GOLD = 'G'
    MEMBERSHIP_CHOICES = [
        (MEMBERSHIP_FREE, 'Free'),
        (MEMBERSHIP_BRONZE, 'Bronze'),
        (MEMBERSHIP_SILVER, 'Silver'),
        (MEMBERSHIP_GOLD, 'Gold')
    ]
    
    membership = models.CharField(
        max_length=1,
        choices=MEMBERSHIP_CHOICES,
        default=MEMBERSHIP_FREE)
    
    class Meta:
        db_table = 'Membership'


class Profile(models.Model):
    
    
    
    #Types of formal status
    STATUS_PERSONAL = 'P'
    STATUS_COMPANY = 'C'
    FORMAL_STATUS_CHOICES = [
        (STATUS_PERSONAL, 'I am using this app for personal application'),
        (STATUS_COMPANY, 'I am using this app on behalf of my company')
    ]
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.FileField(upload_to="image", default="default/default-user.jpg", null=True, blank=True)
    full_name = models.CharField(max_length=100, null=True, blank=True)
    about = models.TextField(null=True, blank=True)
    gender = models.CharField(max_length=100, null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)
    state = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    membership = models.OneToOneField(
        Membership,
        on_delete=models.SET_DEFAULT,
        default='F',
        primary_key=True)
    pid = ShortUUIDField(unique=True, length=10, max_length=20, alphabet ="abcdefghijk")  
    company_name = models.CharField(
        max_length=255,
        blank=True,
        null=True)
    company_phone_number = models.CharField(
        max_length=100,
        blank=True,
        null=True)
    company_email = models.EmailField(blank=True, null=True)
    formal_status = models.CharField(
        max_length=1,
        choices=FORMAL_STATUS_CHOICES,
        default=STATUS_PERSONAL
    )

    def __str__(self):
        return self.full_name or str(self.user.full_name)

    def save(self, *args, **kwargs):
        if not self.full_name:
            self.full_name = self.user.full_name

        super(Profile, self).save(*args, **kwargs)


def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

post_save.connect(create_user_profile, sender=User)
post_save.connect(save_user_profile, sender=User)