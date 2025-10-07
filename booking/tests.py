from django.test import TestCase
from django.contrib.auth.models import User
from .models import Movie, Show, Booking
from .views import book_seat_safe
from django.utils import timezone
from datetime import timedelta

class BookingTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="pass")
        self.movie = Movie.objects.create(title="Test Movie", duration_minutes=120)
        self.show = Show.objects.create(
            movie=self.movie,
            screen_name="Screen 1",
            date_time=timezone.now() + timedelta(days=1),
            total_seats=10
        )

    def test_successful_booking(self):
        booking = book_seat_safe(self.user, self.show, 1)
        self.assertEqual(booking.seat_number, 1)
        self.assertEqual(booking.status, "booked")

    def test_double_booking(self):
        book_seat_safe(self.user, self.show, 2)
        with self.assertRaises(ValueError):
            book_seat_safe(self.user, self.show, 2)

    def test_out_of_range_seat(self):
        with self.assertRaises(ValueError):
            book_seat_safe(self.user, self.show, 20)
