# Generated by Django 4.0.5 on 2022-06-17 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Familiar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30, verbose_name='NOMBRE')),
                ('apellido', models.CharField(max_length=30, verbose_name='APELLIDO')),
                ('nacimiento', models.DateField(verbose_name='FECHA DE NACIMIENTO')),
            ],
        ),
    ]
