from django.urls import path
from .views import map_view, locations_data

urlpatterns = [
    path('', map_view, name='map_views'),
    path('locations_data', locations_data, name='locations_data'),
]