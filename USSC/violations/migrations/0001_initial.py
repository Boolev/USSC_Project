# Generated by Django 3.0.3 on 2020-05-25 17:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=25, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=50, verbose_name='Фамилия')),
                ('patronymic', models.CharField(max_length=50, verbose_name='Отчество')),
            ],
        ),
        migrations.CreateModel(
            name='Violation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=100, verbose_name='Тип нарушения')),
                ('value', models.SmallIntegerField(verbose_name='Штрафные баллы')),
                ('date', models.DateTimeField(verbose_name='Дата нарушения')),
                ('violatorFIO', models.CharField(max_length=200, verbose_name='ФИО нарушителя')),
                ('Comment', models.CharField(max_length=100, verbose_name='Коментарий')),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=100, verbose_name='Фамилия')),
                ('patronymic', models.CharField(max_length=100, verbose_name='Отчество')),
                ('violation_points', models.SmallIntegerField(verbose_name='Количество баллов')),
                ('is_banned', models.BooleanField(verbose_name='Есть ли доступ')),
                ('violation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='violations.Violation')),
            ],
        ),
    ]
