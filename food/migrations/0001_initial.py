# Generated by Django 5.0.6 on 2024-07-08 09:43

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, validators=[django.core.validators.MinLengthValidator(3)])),
                ('recipe', models.CharField(max_length=500, unique=True, validators=[django.core.validators.MinLengthValidator(10)])),
                ('slug', models.SlugField(validators=[django.core.validators.MinLengthValidator(3)])),
                ('image', models.ImageField(null=True, upload_to='image/category/', validators=[django.core.validators.FileExtensionValidator(['jpg', 'jpeg', 'png'], 'Only jpg and jpeg along with png are allowed.')])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Food',
                'verbose_name_plural': 'Foods',
                'db_table': 'food',
            },
        ),
    ]
