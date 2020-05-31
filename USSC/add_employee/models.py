from django.db import models


class Person(models.Model):
    first_name = models.CharField('Имя', max_length=100)
    last_name = models.CharField('Фамилия', max_length=100)
    patronymic = models.CharField('Отчество', max_length=100)
    birth_date = models.DateTimeField('Дата рождения')
    violation_points = models.SmallIntegerField('Количество баллов', default=0)
    is_banned = models.BooleanField('Есть ли доступ', default=False)
