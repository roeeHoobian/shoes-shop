# Generated by Django 5.1.4 on 2024-12-14 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoes', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shoe',
            name='image_url',
        ),
        migrations.AddField(
            model_name='shoe',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]