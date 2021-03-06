# Generated by Django 4.0.1 on 2022-01-16 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bloodline_api', '0003_alter_dog_partners'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dog',
            name='partners',
        ),
        migrations.AddField(
            model_name='dog',
            name='partners',
            field=models.ManyToManyField(blank=True, to='bloodline_api.Dog', verbose_name='related partners'),
        ),
    ]
