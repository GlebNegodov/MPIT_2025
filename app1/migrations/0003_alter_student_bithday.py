# Generated by Django 3.2.25 on 2025-01-25 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_student'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='bithday',
            field=models.DateField(),
        ),
    ]
