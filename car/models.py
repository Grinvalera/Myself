from django.db import models


class Car(models.Model):
    description = models.TextField(max_length=512, blank=True, null=False)

    def __str__(self):
        return f'{self.id}'

    class Meta:
        verbose_name = 'Машина'
        verbose_name_plural = 'Машины'


class Picture(models.Model):
    photo = models.ImageField(upload_to='picture/')
    car = models.ForeignKey(Car, models.CASCADE)

    def __str__(self):
        return f'{self.id}'

    class Meta:
        verbose_name = 'Фото машины'
        verbose_name_plural = 'Фото машин'
# Create your models here.
