import datetime
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.db import models


class TimeStamp(models.Model):
    status = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class FeedbackModel(TimeStamp, models.Model):
    name = models.CharField(max_length=64)
    email = models.EmailField()
    subject = models.CharField(max_length=120)
    message = models.TextField(max_length=500)

    def __str__(self):
        return f"{self.name}"


# Vehicle Model
class VehicleModel(TimeStamp, models.Model):
    class VehicleType(models.TextChoices):
        MOTOR_CYCLE = "mc", "Motor Cycle"
        CAR = "cr", "Car"
        HEAVY_VEHICLE = "hv", "Heavy Vehicle"

    name = models.CharField(max_length=120)

    model = models.CharField(max_length=64)
    type = models.CharField(max_length=18, choices=VehicleType.choices)

    def __str__(self):
        return f"{self.name}"


# Service Type
class ServiceTypeModel(TimeStamp, models.Model):
    name = models.CharField(max_length=64)
    cost = models.FloatField(default=0.0)

    def __str__(self):
        return f"{self.name}"


# Service Model
class ServiceModel(TimeStamp, models.Model):
    USER = get_user_model()
    user = models.ForeignKey(USER, on_delete=models.CASCADE)
    type = models.ForeignKey(ServiceTypeModel, on_delete=models.CASCADE)
    vehicle = models.ForeignKey(VehicleModel, on_delete=models.CASCADE)

    cost = models.FloatField(default=0.0)
    date = models.DateTimeField()
    delivery_time = models.DateTimeField(default=timezone.now)
    is_delivered = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.vehicle}-{self.type}"

    def save(self, *args, **kwargs):
        id = self.id
        if id is None:
            self.cost = self.type.cost
        return super().save(*args, **kwargs)