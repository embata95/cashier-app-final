# Generated by Django 3.2.5 on 2021-08-12 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='IndividualPayment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('January', models.BooleanField(default=False)),
                ('February', models.BooleanField(default=False)),
                ('March', models.BooleanField(default=False)),
                ('April', models.BooleanField(default=False)),
                ('May', models.BooleanField(default=False)),
                ('June', models.BooleanField(default=False)),
                ('July', models.BooleanField(default=False)),
                ('August', models.BooleanField(default=False)),
                ('September', models.BooleanField(default=False)),
                ('October', models.BooleanField(default=False)),
                ('November', models.BooleanField(default=False)),
                ('December', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='IndividualTaxesPayed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('January', models.IntegerField(default=0)),
                ('February', models.IntegerField(default=0)),
                ('March', models.IntegerField(default=0)),
                ('April', models.IntegerField(default=0)),
                ('May', models.IntegerField(default=0)),
                ('June', models.IntegerField(default=0)),
                ('July', models.IntegerField(default=0)),
                ('August', models.IntegerField(default=0)),
                ('September', models.IntegerField(default=0)),
                ('October', models.IntegerField(default=0)),
                ('November', models.IntegerField(default=0)),
                ('December', models.IntegerField(default=0)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PaymentsAdmin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('individual_monthly_tax', models.IntegerField(default=0)),
                ('salaries', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='SalariesPayedPerMonth',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('January', models.IntegerField(default=0)),
                ('February', models.IntegerField(default=0)),
                ('March', models.IntegerField(default=0)),
                ('April', models.IntegerField(default=0)),
                ('May', models.IntegerField(default=0)),
                ('June', models.IntegerField(default=0)),
                ('July', models.IntegerField(default=0)),
                ('August', models.IntegerField(default=0)),
                ('September', models.IntegerField(default=0)),
                ('October', models.IntegerField(default=0)),
                ('November', models.IntegerField(default=0)),
                ('December', models.IntegerField(default=0)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SalariesPayment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('January', models.BooleanField(default=False)),
                ('February', models.BooleanField(default=False)),
                ('March', models.BooleanField(default=False)),
                ('April', models.BooleanField(default=False)),
                ('May', models.BooleanField(default=False)),
                ('June', models.BooleanField(default=False)),
                ('July', models.BooleanField(default=False)),
                ('August', models.BooleanField(default=False)),
                ('September', models.BooleanField(default=False)),
                ('October', models.BooleanField(default=False)),
                ('November', models.BooleanField(default=False)),
                ('December', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SalariesPerMonth',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('January', models.IntegerField(default=0)),
                ('February', models.IntegerField(default=0)),
                ('March', models.IntegerField(default=0)),
                ('April', models.IntegerField(default=0)),
                ('May', models.IntegerField(default=0)),
                ('June', models.IntegerField(default=0)),
                ('July', models.IntegerField(default=0)),
                ('August', models.IntegerField(default=0)),
                ('September', models.IntegerField(default=0)),
                ('October', models.IntegerField(default=0)),
                ('November', models.IntegerField(default=0)),
                ('December', models.IntegerField(default=0)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TaxesPerMonth',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('January', models.IntegerField(default=0)),
                ('February', models.IntegerField(default=0)),
                ('March', models.IntegerField(default=0)),
                ('April', models.IntegerField(default=0)),
                ('May', models.IntegerField(default=0)),
                ('June', models.IntegerField(default=0)),
                ('July', models.IntegerField(default=0)),
                ('August', models.IntegerField(default=0)),
                ('September', models.IntegerField(default=0)),
                ('October', models.IntegerField(default=0)),
                ('November', models.IntegerField(default=0)),
                ('December', models.IntegerField(default=0)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
