# Generated by Django 4.2.4 on 2023-08-22 18:15

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_advertisements', '0005_alter_advertisement_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisement',
            name='title',
            field=models.CharField(max_length=128, validators=[django.core.validators.RegexValidator(code='invalid', inverse_match=True, message='Строка не может начинаться с "?"', regex='^[?]')], verbose_name='Заголовок'),
        ),
    ]
