from django.core.management import BaseCommand

from blog.models import Article


class Command(BaseCommand):

    def handle(self, *args, **options):

        articles = [
            {"title": "Article one", "body": "About work", "is_published": True},
            {"title": "Article two", "body": "About family", "is_published": True},
            {"title": "Article three", "body": "About travelling", "is_published": False},
        ]
        for item in articles:
            Article.objects.create(title=item["title"], description=item["body"], is_published=item["is_published"])
