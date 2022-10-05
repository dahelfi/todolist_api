from email.policy import default
from tkinter import CASCADE
from django.db import models
import datetime
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length = 30)
    description = models.CharField(max_length = 30)
    created_at = models.DateField(default = datetime.date.today)
    user = models.ForeignKey(
        User,
        on_delete = models.CASCADE, default = None
    )