from django.db import models


class Cat(models.Model):
    description = models.TextField(max_length=512, blank=True, null=False)

    def __str__(self):
        return f'{self.id}'

    class Meta:
        verbose_name = 'Кот'
        verbose_name_plural = 'Коты'


class PhotoCat(models.Model):
    photo = models.ImageField(upload_to='picture/')
    cat = models.ForeignKey(Cat, models.CASCADE)

    def __str__(self):
        return f'{self.id}'

    class Meta:
        verbose_name = 'Фото кота'
# Create your models here.
