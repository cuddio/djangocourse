from django.db import models

class Tour(models.Model):
    title = models.CharField('Название', max_length=32)
    description = models.TextField('Описание')
    price = models.FloatField('Цена')
    photo = models.ImageField('Фото', upload_to='static/images')
    date = models.DateField('Дата')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Туры'
        verbose_name = 'тур'

