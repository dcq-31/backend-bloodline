# Generated by Django 4.0.1 on 2022-01-18 18:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bloodline_api', '0005_remove_dog_user_dog_litters_dog_owner_dog_siblings_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dog',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='dogs', to=settings.AUTH_USER_MODEL, verbose_name='related user'),
        ),
    ]
