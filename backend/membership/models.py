from django.db import models


# Create your models here.

class Membership(models.Model):

    """Represents a membership plan"""
    
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

    # Membership Period
    MONTHLY_PERIOD = 'M'
    QUARTERLY_PERIOD = 'Q'
    ANNUALLY_PERIOD = 'A'
    MEMBERSHIP_PERIOD_CHOICES = [
        (MONTHLY_PERIOD, 'monthly'),
        (QUARTERLY_PERIOD, 'quarterly'),
        (ANNUALLY_PERIOD, 'annually')
    ]
    
    membership = models.CharField(
        max_length=1,
        choices=MEMBERSHIP_CHOICES,
        default=MEMBERSHIP_FREE)
    
    period = models.CharField(
        max_length=1,
        choices=MEMBERSHIP_PERIOD_CHOICES,
        default=MONTHLY_PERIOD)
