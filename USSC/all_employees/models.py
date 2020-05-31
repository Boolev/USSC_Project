from django.db import models

class Person(models.Model):
    first_name = models.CharField('Имя', max_length=100)
    last_name = models.CharField('Фамилия', max_length=100)
    patronymic = models.CharField('Отчество', max_length=100)
    violation_points = models.SmallIntegerField('Количество баллов', default=0)
    is_banned = models.BooleanField('Есть ли доступ', default=False)
    profession = models.CharField('Профессия', max_length=100)
    object_name = models.CharField('Название объекта', max_length=100)

    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'