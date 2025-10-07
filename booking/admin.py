# from django.contrib import admin
# from .models import Movie, Show, Booking

# admin.site.register(Movie)
# admin.site.register(Show)
# admin.site.register(Booking)
from django.contrib import admin
from .models import Movie, Show, Booking

# Register Movie only once
@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['title', 'duration_minutes', 'poster']

# Register other models
admin.site.register(Show)
admin.site.register(Booking)
