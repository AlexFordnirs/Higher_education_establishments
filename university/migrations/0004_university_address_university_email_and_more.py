# Generated by Django 5.0 on 2024-01-04 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('university', '0003_alter_university_image_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='university',
            name='address',
            field=models.TextField(blank=True, verbose_name='Address'),
        ),
        migrations.AddField(
            model_name='university',
            name='email',
            field=models.TextField(blank=True, verbose_name='Email'),
        ),
        migrations.AddField(
            model_name='university',
            name='telephone',
            field=models.TextField(blank=True, verbose_name='Telephone'),
        ),
        migrations.AddField(
            model_name='university',
            name='website',
            field=models.TextField(blank=True, verbose_name='Website'),
        ),
    ]
