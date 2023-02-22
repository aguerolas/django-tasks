from django.db import models
from django.contrib.auth.models import User

class Tasks (models.Model):
    title = models.CharField(max_length=290)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    date_done= models.DateTimeField(null=True, blank=True)
    important = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) :
        return f' {self.title} - project: {self.user.username} '