from typing import Iterable
from django.db import models


# Create your models here.
class feedback(models.Model):
    Name = models.CharField(max_length=20)
    Email = models.EmailField()
    feed = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.name