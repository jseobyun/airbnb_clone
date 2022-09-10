from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "This command is for the test."

    def add_arguments(self, parser):
        parser.add_argument("--times", type=int)

    def handle(self, *args, **options):
        print(args, options)
