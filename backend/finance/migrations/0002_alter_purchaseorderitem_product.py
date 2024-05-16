# Generated by Django 4.2 on 2024-05-16 17:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('membership', '0005_alter_membership_options_alter_membership_table'),
        ('finance', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchaseorderitem',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='membership.membership'),
        ),
    ]