# Generated by Django 4.0.1 on 2022-01-16 07:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bloodline_api', '0002_dog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dog',
            name='partners',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='bloodline_api.dog', verbose_name='related partners'),
        ),
    ]
