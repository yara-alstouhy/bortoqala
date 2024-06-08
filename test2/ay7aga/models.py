from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User_acc(AbstractUser):
    username = models.CharField(max_length=150, unique=True)
    role = models.CharField(max_length=20)


class test_data(models.Model):
    title = models.CharField(max_length=50)
    name = models.CharField(max_length=30)
