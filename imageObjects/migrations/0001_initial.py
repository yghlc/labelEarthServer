# Generated by Django 4.0.3 on 2022-05-11 16:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_name', models.CharField(max_length=200, unique=True)),
                ('image_path', models.FilePathField()),
                ('image_object_path', models.FilePathField()),
                ('image_bound_path', models.FilePathField(default=None)),
                ('concurrent_count', models.IntegerField(default=0)),
                ('image_valid_times', models.IntegerField(default=0)),
                ('image_cen_lat', models.FloatField(default=None)),
                ('image_cen_lon', models.FloatField(default=None)),
            ],
        ),
        migrations.CreateModel(
            name='UserInput',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_image_output', models.FilePathField(default=None, null=True)),
                ('init_time', models.DateTimeField(blank=True, default=None)),
                ('save_time', models.DateTimeField(blank=True, default=None, null=True)),
                ('possibility', models.CharField(default=None, max_length=20, null=True)),
                ('user_note', models.TextField(blank=True, null=True)),
                ('image_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='imageObjects.image')),
                ('user_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
