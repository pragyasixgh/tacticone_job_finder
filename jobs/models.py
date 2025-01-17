# jobs/models.py
from django.db import models

class Job(models.Model):
    title = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    description = models.TextField()
    skills = models.CharField(max_length=255)  # Add this field

    def __str__(self):
        return self.title

