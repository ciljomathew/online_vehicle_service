from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse

from core.models import TimeStamp


class CustomUser(AbstractUser):
    pass


USER = settings.AUTH_USER_MODEL

# Location model
class LocationModel(models.Model):
    lattitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self) -> str:
        return f"{self.lattitude},{self.longitude}"


# Address Model
class AddressModel(TimeStamp, models.Model):
    building_name = models.CharField(max_length=64)
    street = models.CharField(max_length=64)
    place = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    district = models.CharField(max_length=64)
    country = models.CharField(max_length=64)
    post_office = models.CharField(max_length=64)
    post_code = models.CharField(max_length=8)
    location = models.ForeignKey(
        LocationModel,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    def __str__(self) -> str:
        return f"{self.building_name} {self.place} {self.district} {self.post_code}"


# Profile Model for user
class ProfileModel(TimeStamp, models.Model):
    class GenderType(models.TextChoices):
        MALE = "m", "Male"
        FEMALE = "f", "Female"
        TRANSGENDER = "t", "Transgender"

    first_name = models.CharField(max_length=24)
    last_name = models.CharField(max_length=24)
    gender = models.CharField(max_length=15, choices=GenderType.choices)
    address = models.ManyToManyField(AddressModel, blank=True)
    phone = models.CharField(max_length=15,default=None)
    image = models.ImageField(
        upload_to="user/profile/image/",
        default="default/user.png",
    )
    user = models.OneToOneField(USER, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"

    def get_absolute_url(self):
        return reverse("user:profile_detail", kwargs={"pk":self.id})
