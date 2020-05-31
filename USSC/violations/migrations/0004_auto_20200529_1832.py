# Generated by Django 3.0.3 on 2020-05-29 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('violations', '0003_auto_20200526_0037'),
    ]

    operations = [
        migrations.RenameField(
            model_name='violation',
            old_name='violatorFIO',
            new_name='violator_FIO',
        ),
        migrations.RemoveField(
            model_name='violation',
            name='comment',
        ),
        migrations.AddField(
            model_name='violation',
            name='object_name',
            field=models.CharField(default='Без объекта', max_length=100, verbose_name='Название объекта'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='violation',
            name='violator_profession',
            field=models.CharField(default='Без профессии', max_length=100, verbose_name='Профессия нарушителя'),
            preserve_default=False,
        ),
    ]
