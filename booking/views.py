# from django.shortcuts import render, redirect, get_object_or_404
# from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.decorators import login_required
# from django.contrib import messages
# from django.contrib.auth.models import User
# from .models import Movie, Show, Booking

# def home(request):
#     if request.user.is_authenticated:
#         return redirect("movie-list")
#     return redirect("login")

# def signup(request):
#     if request.method == "POST":
#         username = request.POST.get("username")
#         password = request.POST.get("password")
#         if not username or not password:
#             messages.error(request, "All fields are required.")
#         elif User.objects.filter(username=username).exists():
#             messages.error(request, "Username already taken.")
#         else:
#             User.objects.create_user(username=username, password=password)
#             messages.success(request, "Signup successful. Please log in.")
#             return redirect("login")
#     return render(request, "signup.html")

# def login_view(request):
#     if request.method == "POST":
#         username = request.POST.get("username")
#         password = request.POST.get("password")
#         user = authenticate(request, username=username, password=password)
#         if user:
#             login(request, user)
#             return redirect("movie-list")
#         else:
#             messages.error(request, "Invalid credentials.")
#     return render(request, "login.html")

# @login_required
# def logout_view(request):
#     logout(request)
#     messages.success(request, "Logged out successfully.")
#     return redirect("login")

# @login_required
# def movie_list(request):
#     movies = Movie.objects.all()
#     return render(request, "movies.html", {"movies": movies})

# @login_required
# def show_list(request, id):
#     movie = get_object_or_404(Movie, id=id)
#     shows = Show.objects.filter(movie=movie)
#     return render(request, "shows.html", {"movie": movie, "shows": shows})

# @login_required
# def book_seat(request, id):
#     show = get_object_or_404(Show, id=id)
#     if request.method == "POST":
#         seat_number = request.POST.get("seat_number")
#         if not seat_number or not seat_number.isdigit():
#             messages.error(request, "Please enter a valid seat number.")
#         else:
#             seat_number = int(seat_number)
#             if seat_number < 1 or seat_number > show.total_seats:
#                 messages.error(request, "Seat number out of range.")
#             else:
#                 if Booking.objects.filter(show=show, seat_number=seat_number, status="booked").exists():
#                     messages.error(request, "Seat already booked.")
#                 else:
#                     Booking.objects.create(user=request.user, show=show, seat_number=seat_number, status="booked")
#                     messages.success(request, "Seat booked successfully.")
#                     return redirect("my-bookings")
#     return render(request, "book.html", {"show": show})

# @login_required
# def my_bookings(request):
#     bookings = Booking.objects.filter(user=request.user)
#     return render(request, "my_bookings.html", {"bookings": bookings})

# @login_required
# def cancel_booking(request, id):
#     booking = get_object_or_404(Booking, id=id, user=request.user)
#     if request.method == "POST":
#         if booking.status != "cancelled":
#             booking.status = "cancelled"
#             booking.save()
#             messages.success(request, "Booking cancelled.")
#         else:
#             messages.info(request, "Booking already cancelled.")
#     return redirect("my-bookings")


# from rest_framework import viewsets, permissions
# from .models import Movie
# from .serializers import MovieSerializer

# class MovieViewSet(viewsets.ModelViewSet):
#     queryset = Movie.objects.all()
#     serializer_class = MovieSerializer
#     permission_classes = [permissions.IsAuthenticated]


# from django.shortcuts import render
# from .models import Movie

# def home(request):
#     movies = Movie.objects.all()
#     return render(request, "home.html", {"movies": movies})


# from django.shortcuts import render, redirect, get_object_or_404
# from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.decorators import login_required
# from django.contrib import messages
# from django.contrib.auth.models import User
# from .models import Movie, Show, Booking
# from django.db import transaction, DatabaseError
# import time

# def home(request):
#     movies = Movie.objects.all()
#     return render(request, 'home.html', {'movies': movies})

# def signup(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         if not username or not password:
#             messages.error(request, 'All fields are required.')
#         elif User.objects.filter(username=username).exists():
#             messages.error(request, 'Username already taken.')
#         else:
#             User.objects.create_user(username=username, password=password)
#             messages.success(request, 'Signup successful. Please log in.')
#             return redirect('login')
#     return render(request, 'signup.html')

# def login_view(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user = authenticate(request, username=username, password=password)
#         if user:
#             login(request, user)
#             return redirect('home')
#         else:
#             messages.error(request, 'Invalid credentials.')
#     return render(request, 'login.html')

# @login_required
# def logout_view(request):
#     logout(request)
#     messages.success(request, 'Logged out successfully.')
#     return redirect('login')

# @login_required
# def movie_list(request):
#     movies = Movie.objects.all()
#     return render(request, 'movies.html', {'movies': movies})

# @login_required
# def show_list(request, id):
#     movie = get_object_or_404(Movie, pk=id)
#     shows = Show.objects.filter(movie=movie)
#     return render(request, 'shows.html', {'movie': movie, 'shows': shows})

# # Retry decorator utility
# def retry_on_error(max_tries=3, delay=1):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             for attempt in range(max_tries):
#                 try:
#                     return func(*args, **kwargs)
#                 except DatabaseError:
#                     if attempt == max_tries - 1:
#                         raise
#                     time.sleep(delay)
#         return wrapper
#     return decorator

# @retry_on_error()
# @transaction.atomic
# def book_seat_safe(user, show, seat_number):
#     if seat_number < 1 or seat_number > show.total_seats:
#         raise ValueError("Seat number out of range.")
#     if Booking.objects.select_for_update().filter(show=show, seat_number=seat_number, status='booked').exists():
#         raise ValueError("Seat already booked.")
#     return Booking.objects.create(user=user, show=show, seat_number=seat_number, status='booked')

# @login_required
# def book_seat(request, id):
#     show = get_object_or_404(Show, pk=id)
#     if request.method == 'POST':
#         seat_number = request.POST.get('seat_number')
#         try:
#             if seat_number is None or not seat_number.isdigit():
#                 raise ValueError('Please enter a valid seat number.')
#             seat_number = int(seat_number)
#             book_seat_safe(request.user, show, seat_number)
#             messages.success(request, 'Seat booked successfully.')
#             return redirect('my-bookings')
#         except ValueError as e:
#             messages.error(request, str(e))
#         except Exception:
#             messages.error(request, 'An unexpected error occurred.')
#     return render(request, 'book.html', {'show': show})

# @login_required
# def my_bookings(request):
#     bookings = Booking.objects.filter(user=request.user)
#     return render(request, 'my_bookings.html', {'bookings': bookings})

# @login_required
# def cancel_booking(request, id):
#     booking = get_object_or_404(Booking, id=id, user=request.user)
#     if request.method == 'POST':
#         if booking.status != 'cancelled':
#             booking.status = 'cancelled'
#             booking.save()
#             messages.success(request, 'Booking cancelled.')
#         else:
#             messages.info(request, 'Booking already cancelled.')
#     return redirect('my-bookings')


from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Movie, Show, Booking
from django.db import transaction, DatabaseError
import time

def home(request):
    movies = Movie.objects.all()
    return render(request, 'home.html', {'movies': movies})

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if not username or not password:
            messages.error(request, 'All fields are required.')
        elif User.objects.filter(username=username).exists():
            messages.error(request, 'Username already taken.')
        else:
            User.objects.create_user(username=username, password=password)
            messages.success(request, 'Signup successful. Please log in.')
            return redirect('login')
    return render(request, 'signup.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid credentials.')
    return render(request, 'login.html')

@login_required
def logout_view(request):
    logout(request)
    messages.success(request, 'Logged out successfully.')
    return redirect('login')

@login_required
def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'movies.html', {'movies': movies})

@login_required
def show_list(request, id):
    movie = get_object_or_404(Movie, pk=id)
    shows = Show.objects.filter(movie=movie)
    return render(request, 'shows.html', {'movie': movie, 'shows': shows})

# Retry decorator utility
def retry_on_error(max_tries=3, delay=1):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for attempt in range(max_tries):
                try:
                    return func(*args, **kwargs)
                except DatabaseError:
                    if attempt == max_tries - 1:
                        raise
                    time.sleep(delay)
        return wrapper
    return decorator

@retry_on_error()
@transaction.atomic
def book_seat_safe(user, show, seat_number):
    if seat_number < 1 or seat_number > show.total_seats:
        raise ValueError("Seat number out of range.")
    if Booking.objects.select_for_update().filter(show=show, seat_number=seat_number, status='booked').exists():
        raise ValueError("Seat already booked.")
    return Booking.objects.create(user=user, show=show, seat_number=seat_number, status='booked')

@login_required
def book_seat(request, id):
    show = get_object_or_404(Show, pk=id)
    occupied_seats = list(Booking.objects.filter(show=show, status='booked').values_list('seat_number', flat=True))

    if request.method == 'POST':
        seat_numbers_str = request.POST.get('seat_numbers', '')
        if not seat_numbers_str:
            messages.error(request, 'Please select at least one seat.')
            return render(request, 'book.html', {'show': show, 'occupied_seats': occupied_seats})

        seat_numbers = seat_numbers_str.split(',')
        try:
            with transaction.atomic():
                for seat_str in seat_numbers:
                    seat = int(seat_str)
                    if seat < 1 or seat > show.total_seats:
                        raise ValueError(f'Seat number {seat} out of range.')
                    if Booking.objects.filter(show=show, seat_number=seat, status='booked').exists():
                        raise ValueError(f'Seat number {seat} is already booked.')
                    Booking.objects.create(user=request.user, show=show, seat_number=seat, status='booked')
            messages.success(request, f'Successfully booked seats: {", ".join(seat_numbers)}.')
            return redirect('my-bookings')
        except ValueError as e:
            messages.error(request, str(e))
        except Exception:
            messages.error(request, f'Unexpected error occurred.')
            # Optional: log exception
    return render(request, 'book.html', {'show': show, 'occupied_seats': occupied_seats})


# @login_required
# def my_bookings(request):
#     # bookings = Booking.objects.filter(user=request.user)
#     bookings = Booking.objects.filter(user=request.user).order_by('-created_at')
#     return render(request, 'my_bookings.html', {'bookings': bookings})

@login_required
def my_bookings(request):
    bookings = Booking.objects.all()
    print(f"All bookings count: {bookings.count()}")  # Should be all bookings (likely > user)
    filtered = Booking.objects.filter(user=request.user)  # Or alternative field
    print(f"Filtered bookings count: {filtered.count()}")
    return render(request, 'my_bookings.html', {'bookings': filtered})


@login_required
def cancel_booking(request, id):
    booking = get_object_or_404(Booking, id=id, user=request.user)
    if request.method == 'POST':
        if booking.status != 'cancelled':
            booking.status = 'cancelled'
            booking.save()
            messages.success(request, 'Booking cancelled.')
        else:
            messages.info(request, 'Booking already cancelled.')
    return redirect('my-bookings')
