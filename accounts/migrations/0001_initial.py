# Generated by Django 4.2.17 on 2024-12-09 18:46

import django.core.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.CharField(max_length=100, unique=True, verbose_name='Електронна пошта')),
                ('firstname', models.CharField(blank=True, max_length=50, verbose_name="Ім'я")),
                ('lastname', models.CharField(blank=True, max_length=50, verbose_name='Прізвище')),
                ('password', models.CharField(max_length=255, verbose_name='Пароль')),
                ('age', models.IntegerField(default=16, validators=[django.core.validators.MinValueValidator(16)], verbose_name='Вік')),
                ('is_staff', models.BooleanField(default=False, verbose_name='Персонал')),
                ('is_superuser', models.BooleanField(default=False, verbose_name='Суперкористувач')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активний')),
                ('is_vip', models.BooleanField(default=False, verbose_name='VIP користувач')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'користувач(а)',
                'verbose_name_plural': 'користувачі',
                'ordering': ['-id'],
            },
        ),
    ]
