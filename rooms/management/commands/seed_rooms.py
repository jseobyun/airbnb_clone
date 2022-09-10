import random
from django.core.management.base import BaseCommand
from django.contrib.admin.utils import flatten
from django_seed import Seed
from rooms import models as room_models
from users import models as user_models


class Command(BaseCommand):
    help = "This command creates rooms"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number", type=int, default=4, help="How many rooms you want to create"
        )

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()
        # seeder does not support foreign key automatically.
        all_users = user_models.User.objects.all()  # not recommended when DB is huge.
        all_room_types = room_models.RoomType.objects.all()
        seeder.add_entity(
            room_models.Room,
            number,
            {
                "name": seeder.faker.address(),
                "host": lambda x: random.choice(all_users),
                "room_type": lambda x: random.choice(all_room_types),
                "price": lambda x: random.randint(1, 1000),
                "beds": lambda x: random.randint(1, 5),
                "guests": lambda x: random.randint(1, 20),
                "bedrooms": lambda x: random.randint(1, 5),
                "baths": lambda x: random.randint(1, 5),
            },
        )
        created_rooms = seeder.execute()
        created_clean = flatten(list(created_rooms.values()))
        amenities = room_models.Amenity.objects.all()
        facilities = room_models.Facility.objects.all()
        house_rules = room_models.HouseRule.objects.all()

        for pk in created_clean:
            picked_room = room_models.Room.objects.get(pk=pk)
            for i in range(3, random.randint(8, 11)):
                room_models.Photo.objects.create(
                    caption=seeder.faker.sentence(),
                    room=picked_room,
                    file=f"room_photos/{random.randint(1,31)}.webp",
                )
            for a in amenities:  # many-to-many field
                if random.random() > 0.6:
                    picked_room.amenities.add(a)
            for f in facilities:
                if random.random() > 0.6:
                    picked_room.facilities.add(f)
            for r in house_rules:
                if random.random() > 0.6:
                    picked_room.house_rules.add(r)

        self.stdout.write(self.style.SUCCESS(f"{number} rooms are created!"))
