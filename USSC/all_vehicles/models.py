from django.db import models


class Vehicle(models.Model):
    type = models.CharField('Тип транспорта', max_length=100)
    object_name = models.CharField('Название объекта', max_length=100)

    def __str__(self):
        return self.type

    class Meta:
        verbose_name = 'Транспортное средство'
        verbose_name_plural = 'Транспортные средства'
