from django.contrib import admin

from core import models

admin.site.register(models.FeedbackModel)
admin.site.register(models.VehicleModel)
admin.site.register(models.ServiceTypeModel)
admin.site.register(models.ServiceModel)
