# Generated by Django 4.2 on 2024-05-15 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('membership', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='membership',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
