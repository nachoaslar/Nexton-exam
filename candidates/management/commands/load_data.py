from django.core.management.base import BaseCommand
from candidates.utils import import_data


class Command(BaseCommand):
    help = "Import data from CSV files"

    def handle(self, *args, **options):
        import_data()
