from django.db import models
from datetime import date

# Model for booking a session
class Booking(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    date = models.DateField(default=date.today)
    time = models.TimeField(default='09:00')
    project_type = models.CharField(max_length=50)
    project_details = models.TextField()
