from django.core.management.base import BaseCommand
from django_seed import Seed
from users import models as user_models


class Command(BaseCommand):
    help = "This command creates users"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number", type=int, default=2, help="How many users do you want to create"
        )

    def handle(self, *args, **options):
        number = options.get("number", 1)
        seeder = Seed.seeder()
        seeder.add_entity(
            user_models.User,
            number,
            {
                "is_staff": False,
                "is_superuser": False,
            },
        )
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f"{number} users are created!"))
