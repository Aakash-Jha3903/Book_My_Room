# Generated by Django 5.2.3 on 2025-06-21 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_hotelvendor_business_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ameneties',
            name='icon',
            field=models.ImageField(upload_to='amenities'),
        ),
    ]
