# Generated by Django 4.2.7 on 2023-11-10 20:01

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_user_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='PhoneNo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country_code', models.CharField(max_length=3)),
                ('number', models.IntegerField(max_length=11, validators=[django.core.validators.MinLengthValidator(4)])),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user')),
            ],
        ),
    ]
