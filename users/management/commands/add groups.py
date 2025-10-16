from django.contrib.auth.models import Group
from django.core.management import call_command
from django.core.management.base import BaseCommand


class GroupCommand(BaseCommand):
    """Кастомная команда для козаполнения групп с настроенными правами в БД"""

    help = "Load test data from fixture"

    def handle(self, *args, **kwargs):
        """Удаление записей и загрузка из файла"""
        # Удаляем существующие записи
        Group.objects.all().delete()
        self.stdout.write(self.style.SUCCESS("Existing data deleted."))

        call_command("loaddata", "group.json")
        self.stdout.write(self.style.SUCCESS("Successfully loaded data from fixture"))
