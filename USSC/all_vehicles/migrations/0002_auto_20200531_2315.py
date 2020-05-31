# Generated by Django 3.0.3 on 2020-05-31 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('all_vehicles', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='vehicle',
            options={'verbose_name': 'Транспортное средство', 'verbose_name_plural': 'Транспортные средства'},
        ),
        migrations.RemoveField(
            model_name='vehicle',
            name='number',
        ),
        migrations.RemoveField(
            model_name='vehicle',
            name='owner',
        ),
        migrations.AddField(
            model_name='vehicle',
            name='object_name',
            field=models.CharField(default='', max_length=100, verbose_name='Название объекта'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vehicle',
            name='type',
            field=models.CharField(default='', max_length=100, verbose_name='Тип транспорта'),
            preserve_default=False,
        ),
    ]