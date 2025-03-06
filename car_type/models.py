from django.core.validators import MinLengthValidator, MaxLengthValidator, MinValueValidator
from django.db import models

from car_profile.models import CarProfile
from car_type.car_type_validators import CarTypeYearValidator


# Create your models here.
class CarType(models.Model):
    TYPE_CHOICES = (
        ('Rally', 'Rally'),
        ('Open-wheel', 'Open-wheel'),
        ('Kart', 'Kart'),
        ('Drag', 'Drag'),
        ('Other', 'Other'),
    )

    type = models.CharField(
        max_length=10,
        choices=TYPE_CHOICES,
        blank=False,
    )

    model = models.CharField(
        blank=False,
        validators=[MinLengthValidator(1), MaxLengthValidator(15)],
    )

    year = models.IntegerField(
        blank=False,
        validators=[CarTypeYearValidator],
    )

    image_url = models.URLField(
        blank=False,
        unique=True,
        null=False,
        verbose_name='Image URL'
    )

    price = models.FloatField(
        blank=False,
        null=False,
        validators=[MinValueValidator(1.0)],
    )

    owner = models.ForeignKey(
        to=CarProfile,
        on_delete=models.CASCADE,
        blank=True,
        null=False,
    )