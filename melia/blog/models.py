from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class News(models.Model):
    title = models.CharField('Название статьи', max_length=100, unique=True)
    #текс НЕ ограничем 250 символами
    text = models.TextField('Текст статьи')
    #текущее время по дефолту
    date = models.DateTimeField('Дата',default=timezone.now)
    #если удаляется пользователь то удалаяются все его статьи(зависит от другой таблицы)
    autor = models.ForeignKey(User, verbose_name='Автор', on_delete=models.CASCADE)

    views = models.IntegerField('Просмотры', default=1)

    # sizes = (
    #     ('s', 'small'),
    #     ('m', 'medium'),
    #     ('l', 'large'),
    #     ('xl', 'extra large')
    # )
    #
    # shop_sizes = models.CharField(max_length=2, choices=sizes, default='s')
    def get_absolute_url(self):
        return reverse('news_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return f'Новость: {self.title}'

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural ='Новости'


class Tasks(models.Model):
    title = models.CharField('Задание', max_length=50)
    text = models.TextField('Суть задания')
    date = models.DateField('Дата', default=timezone.now)
    level=models.FloatField('Уровень сложности', default=0.5)

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural ='Задачи'
