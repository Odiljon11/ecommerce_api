from django.core.management.base import BaseCommand, CommandError
from common import models as common_models
from products import models as products_models


class Command(BaseCommand):
    def handle(self, *args, **options):
        old_cats = products_models.Product.objects.all()
        for cat in old_cats:
            common_models.Category.objects.create(title=cat.title, position=cat.position, parent=cat.parent)
        self.stdout.write(self.style.SUCCESS('Successfully migrated %s categories.' % old_cats.count()))