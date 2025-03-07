# Generated by Django 5.1 on 2025-03-06 17:38

import car_type.car_type_validators
import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('car_profile', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('Rally', 'Rally'), ('Open-wheel', 'Open-wheel'), ('Kart', 'Kart'), ('Drag', 'Drag'), ('Other', 'Other')], max_length=10)),
                ('model', models.CharField(validators=[django.core.validators.MinLengthValidator(1), django.core.validators.MaxLengthValidator(15)])),
                ('year', models.IntegerField(validators=[car_type.car_type_validators.CarTypeYearValidator])),
                ('image_url', models.URLField(unique=True, verbose_name='Image URL')),
                ('price', models.FloatField(validators=[django.core.validators.MinValueValidator(1.0)])),
                ('owner', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='car_profile.carprofile')),
            ],
        ),
    ]
