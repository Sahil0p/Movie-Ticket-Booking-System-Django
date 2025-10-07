from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class Movie(models.Model):
    title = models.CharField(max_length=255)
    duration_minutes = models.PositiveIntegerField()
    poster = models.ImageField(upload_to='movies/', blank=True, null=True)  # Add this line

    def __str__(self):
        return self.title
        
class Show(models.Model):
    movie = models.ForeignKey(Movie, related_name="shows", on_delete=models.CASCADE)
    screen_name = models.CharField(max_length=100)
    date_time = models.DateTimeField()
    total_seats = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.movie.title} - {self.screen_name} at {self.date_time}"

class Booking(models.Model):
    STATUS_CHOICES = [
        ("booked", "Booked"),
        ("cancelled", "Cancelled"),
    ]

    user = models.ForeignKey(User, related_name="bookings", on_delete=models.CASCADE)
    show = models.ForeignKey(Show, related_name="bookings", on_delete=models.CASCADE)
    seat_number = models.PositiveIntegerField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="booked")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("show", "seat_number")

    def clean(self):
        if self.seat_number < 1 or self.seat_number > self.show.total_seats:
            raise ValidationError(f"Seat number {self.seat_number} is out of range for this show.")

    def __str__(self):
        return f"Booking {self.id} for {self.user.username} - {self.show} Seat {self.seat_number} ({self.status})"
