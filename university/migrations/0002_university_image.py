# Generated by Django 5.0 on 2024-01-04 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('university', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='university',
            name='image_url',
            field=models.ImageField(blank=True, null=True, upload_to='university_images/'),
        ),
    ]
