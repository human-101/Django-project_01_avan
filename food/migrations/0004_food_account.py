# Generated by Django 5.0.6 on 2024-07-17 16:43

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0003_food_is_nonveg_food_is_veg_alter_food_slug'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='account',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
