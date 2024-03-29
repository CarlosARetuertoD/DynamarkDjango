# Generated by Django 2.2.6 on 2019-11-14 00:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Codigo', '0002_auto_20191104_2154'),
    ]

    operations = [
        migrations.AddField(
            model_name='coordenada',
            name='idZona',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='coordenadas', to='Codigo.Zona'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='detallepedido',
            name='idProducto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Codigo.Producto'),
        ),
        migrations.DeleteModel(
            name='ZonaCoordenada',
        ),
    ]
