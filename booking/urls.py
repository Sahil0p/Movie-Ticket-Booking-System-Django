# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.home, name='home'),
#     path('signup/', views.signup, name='signup'),
#     path('login/', views.login_view, name='login'),
#     path('logout/', views.logout_view, name='logout'),
#     path('movies/', views.movie_list, name='movie-list'),
#     path('movies/<int:id>/shows/', views.show_list, name='show-list'),
#     path('shows/<int:id>/book/', views.book_seat, name='book-seat'),
#     path('my-bookings/', views.my_bookings, name='my-bookings'),
#     path('bookings/<int:id>/cancel/', views.cancel_booking, name='cancel-booking'),
# ]

# from rest_framework.routers import DefaultRouter
# from .views import MovieViewSet

# router = DefaultRouter()
# router.register(r'movies', MovieViewSet, basename='movie')


# urlpatterns += router.urls


from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('movies/', views.movie_list, name='movie-list'),
    path('movies/<int:id>/shows/', views.show_list, name='show-list'),
    path('shows/<int:id>/book/', views.book_seat, name='book-seat'),
    path('my-bookings/', views.my_bookings, name='my-bookings'),
    path('bookings/<int:id>/cancel/', views.cancel_booking, name='cancel-booking'),
]
