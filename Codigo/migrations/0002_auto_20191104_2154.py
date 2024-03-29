# Generated by Django 2.2.6 on 2019-11-05 02:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Codigo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cabecerapedido',
            name='monto',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='detallepedido',
            name='idCabeceraPedido',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='detalle', to='Codigo.CabeceraPedido'),
        ),
        migrations.AlterField(
            model_name='detallepedido',
            name='idProducto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='producto', to='Codigo.Producto'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='idCategoria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='productos', to='Codigo.Categoria'),
        ),
    ]
