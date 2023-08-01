from django.db import models

# Model for booking a session
class Booking(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    date_and_time = models.DateTimeField()
    project_type = models.CharField(max_length=50)
    project_details = models.TextField(max_length=250)
