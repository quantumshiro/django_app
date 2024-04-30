from django.contrib import admin
from .models import Folder, Task

# Register your models here.
admin.site.register(Folder)
admin.site.register(Task)