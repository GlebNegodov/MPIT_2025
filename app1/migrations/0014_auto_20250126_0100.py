# Generated by Django 3.2.25 on 2025-01-25 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0013_auto_20250126_0040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='dostyshenia',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='student',
            name='dostyshenia_win',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
    ]
