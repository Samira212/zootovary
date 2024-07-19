from django.db import models


class Cat(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Имя')
    breed = models.CharField(max_length=50, unique=True, verbose_name='Порода')
    age = models.IntegerField(default=0, verbose_name='Возраст')
    color = models.CharField(max_length=32, unique=True, verbose_name='Цвет')
    photo = models.ImageField(upload_to='img/', blank=True, null=True, verbose_name='Фото')
    POL_CHOICES = (
        ('Девочка', 'Девочка'),
        ('Мальчик', 'Мальчик'),
    )

    pol = models.CharField(max_length=50, choices=POL_CHOICES, verbose_name='Пол'),

    description = models.TextField(verbose_name='Описания')

    def __str__(self):
        return self.name


class Product(models.Model):
    filler = models.CharField(max_length=16, unique=True,  verbose_name='Наполнитель')
    carrier = models.CharField(max_length=16, unique=True,  verbose_name='Переноска')
    FEED_CHOICES = (
        ('Сухой корм', 'Сухой корм'),
        ('Жидкий корм', 'Жидкий корм'),
    )
    feed = models.CharField(max_length=50, choices=FEED_CHOICES,  verbose_name='Корм')

    def __str__(self):
        return f'{self.filler} - {self.feed}'
