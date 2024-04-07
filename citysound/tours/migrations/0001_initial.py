# Generated by Django 4.2.11 on 2024-04-07 20:12

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
            name='Tour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('duration', models.PositiveSmallIntegerField(default=1)),
                ('description', models.TextField(blank=True)),
                ('photo', models.ImageField(upload_to='photos/')),
                ('audio', models.FileField(upload_to='audio/')),
                ('location', models.CharField(max_length=255)),
                ('is_active', models.BooleanField(default=True, help_text='Used for disabling the ride or marking it finished', verbose_name='active status')),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
