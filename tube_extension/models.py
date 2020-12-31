from django.db import models
from django.urls import reverse_lazy
from django_mysql.models import ListCharField
from django.contrib.auth.models import User

# Create your models here.



class Video(models.Model):
    title = models.CharField(
        max_length=255,
        blank=False,
        null=False)
    link = models.CharField(
        max_length=255,
        blank=False,
        null=False)
    durations = ListCharField(
        base_field=models.IntegerField(
                blank = False,
                null = False
            ),
        max_length=225
        )
    user = models.ForeignKey(
        User, 
        default=1,
        on_delete=models.CASCADE
        )
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse_lazy("detail", args=[self.id])