import csv

from django.core.management import BaseCommand
from django.utils import timezone

from main.models import Blackbox


class Command(BaseCommand):
    help = "Loads Blackbox details from CSV file."

    def add_arguments(self, parser):
        parser.add_argument("file_path", type=str)

    def handle(self, *args, **options):
        start_time = timezone.now()
        file_path = options["file_path"]
        with open(file_path, "r") as csv_file:
            data = csv.reader(csv_file, delimiter=",")
            items = []
            next(data)
            for row in data:
                print(row)  # to pass header at CSV file
                item = Blackbox(
                    type=row[1],
                    aircraft=row[2],
                    status=row[3],
                    errors_count=row[4],
                    info_count=row[5]
                )
                items.append(item)
                if len(items) > 5000:
                    Blackbox.objects.bulk_create(items)
                    products = []
            if items:
                Blackbox.objects.bulk_create(items)
        end_time = timezone.now()
        self.stdout.write(
            self.style.SUCCESS(
                f"Loading CSV took: {(end_time-start_time).total_seconds()} seconds."
            )
        )