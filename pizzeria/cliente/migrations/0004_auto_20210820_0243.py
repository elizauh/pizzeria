# Generated by Django 3.1.7 on 2021-08-20 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0003_remove_cuenta_estado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='cedula',
            field=models.CharField(max_length=10),
        ),
    ]