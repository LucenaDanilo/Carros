# Generated by Django 4.2.6 on 2023-10-13 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0003_alter_car_brand_alter_car_model'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='cars/'),
        ),
        migrations.AddField(
            model_name='car',
            name='plate',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
