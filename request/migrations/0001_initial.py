# Generated by Django 2.2 on 2021-06-09 13:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('channel', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SecretaryRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request_text', models.CharField(blank=True, max_length=2000, null=True)),
                ('answer_text', models.CharField(blank=True, max_length=2000, null=True)),
                ('request_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('answer_date', models.DateTimeField(null=True)),
                ('accept', models.BooleanField(default=False)),
                ('request_type', models.CharField(choices=[('secretary', 'secretary'), ('join_channel', 'join_channel')], default='join_channel', max_length=64)),
                ('channel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='channel.Channel', verbose_name='Channel')),
                ('target_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Target User')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='JoinChannelRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request_text', models.CharField(blank=True, max_length=2000, null=True)),
                ('answer_text', models.CharField(blank=True, max_length=2000, null=True)),
                ('request_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('answer_date', models.DateTimeField(null=True)),
                ('accept', models.BooleanField(default=False)),
                ('request_type', models.CharField(choices=[('secretary', 'secretary'), ('join_channel', 'join_channel')], default='join_channel', max_length=64)),
                ('channel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='channel.Channel', verbose_name='Channel')),
                ('target_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Target User')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
