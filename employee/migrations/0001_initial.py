# Generated by Django 2.0 on 2020-08-20 16:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('designation', models.CharField(max_length=20)),
                ('salary', models.IntegerField(blank=True, null=True)),
                ('picture', models.ImageField(blank=True, max_length=255, null=True, upload_to='pictures/%Y/%m/%d/')),
            ],
            options={
                'ordering': ('-salary',),
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
            ],
            options={
                'ordering': ('username',),
                'proxy': True,
                'indexes': [],
            },
            bases=('auth.user',),
        ),
        migrations.AddField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
