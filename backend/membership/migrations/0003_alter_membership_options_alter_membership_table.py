# Generated by Django 4.2 on 2024-05-15 21:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('membership', '0002_membership_price'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='membership',
            options={'verbose_name_plural': 'Memberships'},
        ),
        migrations.AlterModelTable(
            name='membership',
            table='Membership',
        ),
    ]
