# Generated by Django 5.0.1 on 2024-02-18 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('templates', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='card_cvv',
            field=models.CharField(max_length=3),
        ),
    ]
