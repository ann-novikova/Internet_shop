from django.db import models

from users.models import CustomUser


class Category(models.Model):
    """Класс для категории товаров"""

    name = models.CharField(max_length=150, verbose_name="Наименование категории")
    description = models.TextField(verbose_name="Описание")

    def __str__(self):
        """Метод для строкового отображения"""
        return self.name

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "категории"
        ordering = ["name"]


class Product(models.Model):
    """Класс для товаров"""

    name = models.CharField(max_length=150, verbose_name="Имя")
    description = models.TextField(verbose_name="Описание")
    photo = models.ImageField(upload_to="catalog/photo", verbose_name="Изображение", blank=True, null=True)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, max_length=150, verbose_name="Категория", related_name="products"
    )
    price = models.FloatField(verbose_name="цена за покупку")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(verbose_name="Статус публикации", default=False)
    owner = models.ForeignKey(CustomUser, verbose_name="Владелец", blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        """Метод для строкового отображения"""
        return self.name

    class Meta:
        verbose_name = "товар"
        verbose_name_plural = "товары"
        ordering = [
            "category",
            "name",
        ]
        permissions = [
            ('can_unpublish_product', 'Can unpublish product'),
        ]

class ContactInfo(models.Model):
    """Класс для создания экземпляров контактной информации"""

    name = models.CharField(max_length=100, verbose_name="Имя")
    phone = models.CharField(max_length=20, verbose_name="Телефон")
    message = models.TextField(verbose_name="Сообщение")

    class Meta:
        verbose_name = "Контактная информация"
        verbose_name_plural = "Контактная информация"

    def __str__(self):
        """Метод для строкового отображения"""
        return self.name
