from django.core.management import call_command
from django.core.management.base import BaseCommand

from catalog.models import Category, Product


class Command(BaseCommand):
    """Кастомная команда для удаления существующих записей и загрузки фикстуры"""

    help = "Load test data from fixture"

    def handle(self, *args, **kwargs):
        """Удаление записей и загрузка из файла"""
        # Удаляем существующие записи
        Product.objects.all().delete()
        Category.objects.all().delete()
        self.stdout.write(self.style.SUCCESS("Existing data deleted."))

        call_command("loaddata", "catalog_fixture.json")
        self.stdout.write(self.style.SUCCESS("Successfully loaded data from fixture"))
