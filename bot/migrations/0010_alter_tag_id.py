# Generated by Django 3.2.11 on 2025-03-08 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0009_userchat_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='id',
            field=models.CharField(max_length=20, primary_key=True, serialize=False),
        ),
    ]
