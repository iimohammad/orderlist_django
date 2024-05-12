# Generated by Django 4.2 on 2024-05-12 13:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userauths', '0006_alter_profile_membership'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='id',
            field=models.BigAutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='profile',
            name='membership',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='userauths.membership'),
        ),
    ]
