# Generated by Django 5.0.6 on 2024-06-13 23:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0004_ciudad_remove_cliente_contrasena_cliente_id_ciudad'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ciudad',
            name='id_ciudad',
            field=models.IntegerField(db_column='idCiudad', primary_key=True, serialize=False),
        ),
    ]