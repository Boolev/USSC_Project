# Generated by Django 3.0.3 on 2020-05-29 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=100, verbose_name='Фамилия')),
                ('patronymic', models.CharField(max_length=100, verbose_name='Отчество')),
                ('birth_date', models.DateTimeField(verbose_name='Дата рождения')),
                ('violation_points', models.SmallIntegerField(default=0, verbose_name='Количество баллов')),
                ('is_banned', models.BooleanField(default=False, verbose_name='Есть ли доступ')),
            ],
        ),
    ]
