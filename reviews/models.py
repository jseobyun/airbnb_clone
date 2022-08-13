from django.db import models
from core import models as core_models

# import users.models as users_models


class Review(core_models.TimeStampedModel):

    """Review model definition"""

    review = models.TextField()
    accuracy = models.IntegerField()
    communication = models.IntegerField()
    cleanliness = models.IntegerField()
    location = models.IntegerField()
    check_in = models.IntegerField()
    value = models.IntegerField()
    # users.User means users.models.User
    # user = models.ForeignKey(users_models.User, on_delete=models.CASCADE)
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    room = models.ForeignKey("rooms.Room", on_delete=models.CASCADE)

    def __str__(self):
        """
        room already has __str__ returning name.
        use self.room instead of self.room.name
        """
        return f"{self.review} - {self.room}"
