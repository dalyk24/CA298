# Generated by Django 5.0.1 on 2024-02-18 07:27

import django.contrib.auth.validators
import django.db.models.deletion
import django.utils.timezone
import templates.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cheese',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Crust',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sauce',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Email')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', templates.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Chicken', models.BooleanField(default=False)),
                ('Pepperoni', models.BooleanField(default=False)),
                ('Mushroom', models.BooleanField(default=False)),
                ('Olives', models.BooleanField(default=False)),
                ('Ham', models.BooleanField(default=False)),
                ('Pineapple', models.BooleanField(default=False)),
                ('Peppers', models.BooleanField(default=False)),
                ('Onion', models.BooleanField(default=False)),
                ('Sweetcorn', models.BooleanField(default=False)),
                ('Pesto', models.BooleanField(default=False)),
                ('Anchovies', models.BooleanField(default=False)),
                ('Jalapeno', models.BooleanField(default=False)),
                ('completed', models.BooleanField(default=False)),
                ('cheese', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='templates.cheese')),
                ('crust', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='templates.crust')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('sauce', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='templates.sauce')),
                ('size', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='templates.size')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=40)),
                ('address', models.CharField(max_length=80)),
                ('card_number', models.CharField(max_length=16)),
                ('card_expiry', models.DateTimeField(null=True)),
                ('card_cvv', models.CharField(max_length=4)),
                ('order_time', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('pizza', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='templates.pizza')),
            ],
        ),
    ]
