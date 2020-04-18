from django.db import models


class Company(models.Model):
    description = models.TextField(blank=True, null=False)

    def __str__(self):
        return f'{self.id}'

    class Meta:
        verbose_name = 'Компания'
        verbose_name_plural = 'Компании'


class PictureCompany(models.Model):
    photo = models.ImageField(upload_to='picture/')
    company = models.ForeignKey(Company, models.CASCADE)

    def __str__(self):
        return f'{self.id}'

    class Meta:
        verbose_name = 'Фото компании'
# Create your models here.
