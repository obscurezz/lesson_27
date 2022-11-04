from django.db import models


class BaseModel(models.Model):
    objects = models.Manager()

    class Meta:
        abstract = True


class Ad(BaseModel):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=200)
    price = models.PositiveIntegerField
    description = models.CharField(max_length=4000)
    address = models.CharField(max_length=1000)
    models.CharField(max_length=1000)


class Category(BaseModel):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
