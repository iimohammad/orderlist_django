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
    
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def save(self, *args, **kwargs):
        # Calculate price based on membership and period
        if self.membership == self.MEMBERSHIP_FREE:
            if self.period == self.MONTHLY_PERIOD:
                self.price = 0
            elif self.period == self.QUARTERLY_PERIOD:
                self.price = 0
            elif self.period == self.ANNUALLY_PERIOD:
                self.price = 0
        elif self.membership == self.MEMBERSHIP_BRONZE:
            if self.period == self.MONTHLY_PERIOD:
                self.price = 10
            elif self.period == self.QUARTERLY_PERIOD:
                self.price = 25
            elif self.period == self.ANNUALLY_PERIOD:
                self.price = 90
        elif self.membership == self.MEMBERSHIP_SILVER:
            if self.period == self.MONTHLY_PERIOD:
                self.price = 20
            elif self.period == self.QUARTERLY_PERIOD:
                self.price = 50
            elif self.period == self.ANNUALLY_PERIOD:
                self.price = 180
        elif self.membership == self.MEMBERSHIP_GOLD:
            if self.period == self.MONTHLY_PERIOD:
                self.price = 30
            elif self.period == self.QUARTERLY_PERIOD:
                self.price = 75
            elif self.period == self.ANNUALLY_PERIOD:
                self.price = 270

        super().save(*args, **kwargs)
