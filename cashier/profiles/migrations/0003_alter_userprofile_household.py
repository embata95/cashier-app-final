# Generated by Django 3.2.5 on 2021-08-08 16:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('households', '0002_alter_householdprofile_apartment'),
        ('profiles', '0002_auto_20210808_1327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='household',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='households.householdprofile'),
        ),
    ]