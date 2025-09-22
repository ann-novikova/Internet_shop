from django.db import models


class Article(models.Model):
    """Класс для блоговой записи"""

    title = models.CharField(max_length=150, verbose_name="Название")
    description = models.TextField(verbose_name="Содержимое")
    preview = models.ImageField(upload_to="blog/photo", verbose_name="Изображение", blank=True, null=True)
    is_published = models.BooleanField(verbose_name="Признак публикации")
    created_at = models.DateTimeField(auto_now_add=True)
    views_count = models.PositiveIntegerField(verbose_name="Счетчик просмотров", default=0)

    def __str__(self):
        """Метод для строкового отображения"""
        return self.title

    class Meta:
        verbose_name = "статья"
        verbose_name_plural = "статьи"
        ordering = ["title"]

