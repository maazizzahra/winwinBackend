# Generated by Django 5.0.3 on 2024-03-20 00:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('winwin', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='phone_number',
            field=models.CharField(default='', max_length=15, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
