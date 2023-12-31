# Generated by Django 4.0.5 on 2022-07-15 21:23

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clients',
            fields=[
                ('id', models.UUIDField(auto_created=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=250, null=True)),
                ('phoneNumber', models.CharField(error_messages={'unique': 'A user with that phone number already exists.'}, max_length=11, unique=True, validators=[django.core.validators.MinLengthValidator(limit_value=11, message='Phone Number must be 11 number'), django.core.validators.RegexValidator(message='must be valid Egyption Number', regex='01[1,2,5,0]{1}[0-9]{8}')])),
                ('has_whatsapp', models.BooleanField(default=False, help_text='whether the user has whatsapp or not.')),
            ],
        ),
        migrations.CreateModel(
            name='Programs',
            fields=[
                ('id', models.UUIDField(auto_created=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('title', models.CharField(max_length=150)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='License',
            fields=[
                ('id', models.UUIDField(auto_created=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('client_mac_id', models.CharField(default='Null', max_length=150)),
                ('is_active', models.BooleanField(default=False, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('running_time', models.IntegerField(default=0)),
                ('client', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='licenses', to='license_api.clients')),
                ('program', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='programs', to='license_api.programs')),
            ],
        ),
    ]
