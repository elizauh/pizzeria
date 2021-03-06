# Generated by Django 3.1.7 on 2021-08-17 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('cedula', models.CharField(max_length=10, unique=True)),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('direccion', models.CharField(max_length=50)),
                ('telefono', models.CharField(max_length=10)),
                ('celular', models.CharField(max_length=10)),
                ('correo', models.CharField(max_length=50)),
                ('estado', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Cuenta',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('persona', models.CharField(max_length=10)),
                ('username', models.CharField(max_length=10)),
                ('password', models.CharField(max_length=10)),
                ('estado', models.CharField(max_length=10)),
            ],
        ),
    ]
