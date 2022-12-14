# Generated by Django 4.1 on 2022-08-10 00:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("rooms", "0002_roomtype_room_room_type"),
    ]

    operations = [
        migrations.CreateModel(
            name="Amenity",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created", models.DateField(auto_now_add=True)),
                ("updated", models.DateField(auto_now=True)),
                ("name", models.CharField(max_length=80)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Facility",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created", models.DateField(auto_now_add=True)),
                ("updated", models.DateField(auto_now=True)),
                ("name", models.CharField(max_length=80)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="HouseRule",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created", models.DateField(auto_now_add=True)),
                ("updated", models.DateField(auto_now=True)),
                ("name", models.CharField(max_length=80)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.RemoveField(
            model_name="room",
            name="room_type",
        ),
        migrations.AddField(
            model_name="room",
            name="amenity",
            field=models.ManyToManyField(to="rooms.amenity"),
        ),
        migrations.AddField(
            model_name="room",
            name="facility",
            field=models.ManyToManyField(to="rooms.facility"),
        ),
        migrations.AddField(
            model_name="room",
            name="house_rules",
            field=models.ManyToManyField(to="rooms.houserule"),
        ),
        migrations.AddField(
            model_name="room",
            name="room_type",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="rooms.roomtype",
            ),
        ),
    ]
