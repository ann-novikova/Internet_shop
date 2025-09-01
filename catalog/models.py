from django.db import models



class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='Наименование категории')
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ['name']

class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name='Имя')
    description = models.TextField(verbose_name='Описание')
    photo = models.ImageField(upload_to='catalog/photo', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, max_length=150, verbose_name='Категория', related_name='products')
    price = models.FloatField(verbose_name='цена за покупку')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'
        ordering = ['category', 'name']