from django.contrib import admin

# Register your models here.
from todoapp.models import Task


admin.site.register(Task)