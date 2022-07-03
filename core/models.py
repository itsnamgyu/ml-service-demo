from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Post(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    image = models.ImageField()

    CAT = "CAT"
    DOG = "DOG"
    PREDICTION_CHOICES = [
        (CAT, "Cat"),
        (DOG, "Dog"),
    ]
    prediction = models.CharField(choices=PREDICTION_CHOICES, max_length=3)

    public = models.BooleanField(default=True)
