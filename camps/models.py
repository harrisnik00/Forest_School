from django.db import models


class Camp(models.Model):
    name = models.CharField(max_length=200)
    age_range = models.CharField(max_length=50)  # e.g. "Ages 4–9"
    daily_hours = models.CharField(max_length=100)  # e.g. "Weekdays 9:00 – 14:00"

    week_price = models.DecimalField(max_digits=8, decimal_places=2)  # e.g. 275.00


    description = models.TextField()  # detailed info about activities, staff, etc.

    start_date = models.DateField()
    end_date = models.DateField()

    sleepover_option = models.BooleanField(default=False)
    sleepover_limit = models.PositiveIntegerField(blank=True, null=True)

    registration_open = models.DateField(blank=True, null=True)
    capacity = models.PositiveIntegerField(blank=True, null=True)  # max campers

    is_active = models.BooleanField(default=True)  # toggle visibility
    order = models.PositiveIntegerField(default=0)  # control display order

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["order", "start_date"]

    def __str__(self):
        return f"{self.name} ({self.start_date} – {self.end_date})"