# Generated by Django 4.2.4 on 2023-09-15 10:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bio',
            name='profile_pic',
            field=models.FileField(blank=True, null=True, upload_to='profile_pics'),
        ),
        migrations.AlterField(
            model_name='bio',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, unique=True),
        ),
    ]
