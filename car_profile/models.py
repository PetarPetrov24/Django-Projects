from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from car_profile.car_profile_validators import CarUsernameValidator, CarUsernameContainsValidator


# Create your models here.
class CarProfile(models.Model):
    username = models.CharField(
        max_length=15,
        validators=[CarUsernameValidator, CarUsernameContainsValidator, MinLengthValidator(3)],
        blank=False,
    )

    email = models.EmailField(
        blank=False,
    )

    age = models.IntegerField(
        blank=False,
        validators=[MinValueValidator(21)],
        help_text="Age requirement: 21 years and above.",
    )

    password = models.CharField(
        blank=False,
        max_length=20,
    )

    first_name = models.CharField(
        blank=True,
        max_length=25,
    )

    last_name = models.CharField(
        blank=True,
        max_length=25,
    )

    profile_picture = models.URLField(
        blank=True,
    )
