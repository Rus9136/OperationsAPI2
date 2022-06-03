from django.db import models


class Costs(models.Model):
    title = models.CharField('Наименования', max_length=300)
    time_create = models.DateTimeField('Дата', auto_now_add=True)
    amount = models.IntegerField('Сумма')
    AmoundView = models.ForeignKey('Types', on_delete=models.PROTECT, null=True)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Расход'
        verbose_name_plural = 'Расходы'



class Types(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Вид события'
        verbose_name_plural = 'Виды события'



class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория расхода'
        verbose_name_plural = 'Категории расходов'


