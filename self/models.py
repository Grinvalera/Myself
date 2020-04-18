from django.db import models


class Valera(models.Model):
    first_name = models.CharField(max_length=64, blank=True, null=False)
    last_name = models.CharField(max_length=64, blank=True, null=False)
    about_me = models.TextField(blank=True, null=False)
    picture = models.ImageField(upload_to='picture/')

    def __str__(self):
        return f'{self.first_name}'

    class Meta:
        verbose_name = 'О себе'
        verbose_name_plural = 'О себе'


class Photo(models.Model):
    photo = models.ImageField(upload_to='picture/')

    def __str__(self):
        return f'{self.id}'

    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'
# Create your models here.
