# Generated by Django 3.1.7 on 2021-08-20 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0006_menu_descripcion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='codigo',
            field=models.CharField(max_length=10),
        ),
    ]
