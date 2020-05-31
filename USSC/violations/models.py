from django.db import models


class Cop(models.Model):
    first_name = models.CharField('Имя', max_length=25)
    last_name = models.CharField('Фамилия', max_length=50)
    patronymic = models.CharField('Отчество', max_length=50)

    def __str__(self):
        return self.first_name


class Person(models.Model):
    first_name = models.CharField('Имя', max_length=100)
    last_name = models.CharField('Фамилия', max_length=100)
    patronymic = models.CharField('Отчество', max_length=100)
    violation_points = models.SmallIntegerField('Количество баллов')
    is_banned = models.BooleanField('Есть ли доступ')

    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'

class ViolationType(models.Model):
    name = models.CharField('Наименование типа нарушения', max_length=100)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Тип Нарушения'
        verbose_name_plural = 'Типы Нарушений'

class Profession(models.Model):
    name = models.CharField('Название профессии', max_length=100)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Профессия'
        verbose_name_plural = 'Профессии'

class Object(models.Model):
    name = models.CharField('Название объекта', max_length=100)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Объект'
        verbose_name_plural = 'Объекты'


class Violation(models.Model):
    type = models.ForeignKey(ViolationType, on_delete=models.CASCADE)
    value = models.SmallIntegerField('Штрафные баллы')
    date = models.DateTimeField('Дата нарушения')
    violator_FIO = models.CharField('ФИО нарушителя', max_length=100)
    violator_profession = models.ForeignKey(Profession, on_delete=models.CASCADE)
    object_name = models.ForeignKey(Object, on_delete=models.CASCADE)

    def __str__(self):
        return self.type.name

    class Meta:
        verbose_name = 'Нарушение'
        verbose_name_plural = 'Нарушения'