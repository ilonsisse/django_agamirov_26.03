from django.db import models


class Place(models.Model):
    class Meta:
        verbose_name = 'Район'
        verbose_name_plural = 'Районы'

    name = models.CharField(max_length=100, verbose_name='Наименование')
    population = models.IntegerField(verbose_name='Население')
    id = models.AutoField(primary_key=True)
    objects = models.Manager()

    def __str__(self):
        return f'Район {self.name}'


class Shop(models.Model):
    class Meta:
        verbose_name = 'Магазин'
        verbose_name_plural = 'Магазины'

    name = models.CharField(max_length=100, verbose_name='Название')
    income_per_month = models.DecimalField(max_length=300, decimal_places=2, verbose_name='Месячная прибыль',
                                           max_digits=5)
    supervisor = models.CharField(max_length=64, verbose_name='Руководитель', blank=True, null=True)
    place = models.ForeignKey(to=Place, on_delete=models.PROTECT, verbose_name='Район')
    is_open = models.BooleanField(default=True, verbose_name='Открыт')
    objects = models.Manager()
    id = models.AutoField(primary_key=True)

    def __str__(self):
        return f'Магазин {self.name}'
