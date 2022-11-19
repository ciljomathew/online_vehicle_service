# Generated by Django 4.1.2 on 2022-11-16 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0003_profilemodel_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profilemodel",
            name="address",
            field=models.ManyToManyField(blank=True, to="user.addressmodel"),
        ),
        migrations.AlterField(
            model_name="profilemodel",
            name="phone",
            field=models.IntegerField(max_length=15),
        ),
    ]