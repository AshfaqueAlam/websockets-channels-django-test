# Generated by Django 3.2.16 on 2023-01-15 13:59

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
            name='Logs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(blank=True, choices=[('pending', 'Pending'), ('successful', 'Successful'), ('failed', 'Failed')], default='pending', max_length=250, null=True)),
                ('percent_completed', models.FloatField(blank=True, default=0.0, null=True)),
                ('error_msg', models.TextField(blank=True, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='u_logs', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'logs',
            },
        ),
    ]