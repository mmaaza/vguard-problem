# Generated by Django 5.0.2 on 2024-02-14 17:45

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AgeGender',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('male_kids', models.IntegerField(default=0)),
                ('female_kids', models.IntegerField(default=0)),
                ('male_teens', models.IntegerField(default=0)),
                ('female_teens', models.IntegerField(default=0)),
                ('male_adults', models.IntegerField(default=0)),
                ('female_adults', models.IntegerField(default=0)),
                ('male_old', models.IntegerField(default=0)),
                ('female_old', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Camera',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('notes', models.CharField(max_length=50, null=True)),
                ('location', models.CharField(max_length=255, null=True)),
                ('latitude', models.FloatField(null=True, validators=[django.core.validators.MinValueValidator(-90), django.core.validators.MaxValueValidator(90)])),
                ('longitude', models.FloatField(null=True, validators=[django.core.validators.MinValueValidator(-180), django.core.validators.MaxValueValidator(180)])),
            ],
        ),
        migrations.CreateModel(
            name='FaceRecognition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(upload_to='')),
                ('camera', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='face', to='dashboard.camera')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FireSmokeWeaponDetection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('alarm_title', models.CharField(choices=[('fire', 'fire'), ('smoke', 'smoke'), ('weapon', 'weapon')], max_length=15)),
                ('severity', models.CharField(choices=[('low', 'low'), ('medium', 'medium'), ('high', 'high'), ('critical', 'critical')], max_length=15)),
                ('status', models.CharField(choices=[('need handling', 'need handling'), ('handled', 'handled'), ('in progress', 'in progress'), ('resolved', 'resolved')], max_length=15)),
                ('camera', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='detection', to='dashboard.camera')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='LicensePlateRecognition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('plate_number', models.CharField(max_length=10)),
                ('camera', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='plate', to='dashboard.camera')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
