# Generated by Django 2.2 on 2021-06-03 20:26

import channel.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('User', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Channel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(blank=True, max_length=500)),
                ('invite_link', models.CharField(max_length=32, unique=True)),
                ('avatar', models.FileField(blank=True, null=True, upload_to='files/channel_avatar/', validators=[channel.models.validate_avatar_extension])),
                ('consultant', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='User.ConsultantProfile', verbose_name='channel owner')),
            ],
            options={
                'verbose_name_plural': 'Channel',
            },
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now)),
                ('channel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='channel.Channel', verbose_name='')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='')),
            ],
            options={
                'verbose_name_plural': 'Subscription',
                'unique_together': {('channel', 'user')},
            },
        ),
        migrations.AddField(
            model_name='channel',
            name='subscribers',
            field=models.ManyToManyField(through='channel.Subscription', to=settings.AUTH_USER_MODEL, verbose_name=''),
        ),
    ]
