from django.db import models

class HealthData(models.Model):
    username = models.CharField(max_length=150, unique=True, primary_key=True)  # Set username as primary key
    gender = models.CharField(max_length=10)
    age = models.IntegerField()
    weight = models.FloatField()
    height = models.FloatField()
    sleep_hours = models.FloatField()
    water_intake = models.FloatField()
    activity_level = models.CharField(max_length=50)
    daily_steps = models.IntegerField()
    stress_level = models.CharField(max_length=20)
    health_conditions = models.TextField(blank=True, null=True)
    medications = models.TextField(blank=True, null=True)
    bad_habits = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField()

    def __str__(self):
        return self.username
