from django.contrib import admin
from .models import Tasks

# Register your models here.
class Task_admin(admin.ModelAdmin):
    readonly_fields = ['created_at'] #solo para leer

admin.site.register(Tasks, Task_admin)
