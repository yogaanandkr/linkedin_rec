# Generated by Django 4.2.4 on 2023-09-16 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_alter_recommendations_recommended_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recommendations',
            name='recommended_by',
            field=models.CharField(max_length=100, null=True),
        ),
    ]