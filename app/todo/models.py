from django.conf import settings
from django.db import models
from django.utils import timezone

class Folder(models.Model):
    title = models.CharField(max_length = 200)
    created_at = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.title

# Create your models here.
