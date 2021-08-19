import csv

import requests
from django.core.management.base import BaseCommand

from api.models import Shop


class Command(BaseCommand):
    help = 'Loading data from csv via url'

    def add_arguments(self, parser):
        parser.add_argument('link', type=str)

    def handle(self, link: str, *args, **options):
        response = requests.get(link)
        reader = csv.DictReader(response.text.splitlines())
        Shop.objects.bulk_create(
            [Shop(**{k.lower(): v for k, v in data.items()})for data in reader]
        )
        self.stdout.write(self.style.SUCCESS('Your base is ready!'))
