# Generated by Django 2.2 on 2021-06-03 20:26

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
            name='ChatMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('text', models.TextField(blank=True, max_length=2000, null=True)),
                ('message_file', models.FileField(blank=True, null=True, upload_to='files/message_file')),
                ('message_type', models.CharField(choices=[('t', 'text'), ('i', 'image'), ('v', 'video'), ('a', 'audio')], default='t', max_length=1)),
                ('receiver', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='chatmessage_reciever', to=settings.AUTH_USER_MODEL, verbose_name='')),
                ('sender', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='chatmessage_sender', to=settings.AUTH_USER_MODEL, verbose_name='')),
            ],
            options={
                'verbose_name_plural': 'ChatMessages',
            },
        ),
        migrations.CreateModel(
            name='ChannelMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('text', models.TextField(blank=True, max_length=2000, null=True)),
                ('message_file', models.FileField(blank=True, null=True, upload_to='files/message_file')),
                ('message_type', models.CharField(choices=[('t', 'text'), ('i', 'image'), ('v', 'video'), ('a', 'audio')], default='t', max_length=1)),
                ('channel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='channel.Channel', verbose_name='')),
                ('creator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='')),
            ],
            options={
                'verbose_name_plural': 'ChannelMessages',
            },
        ),
    ]
