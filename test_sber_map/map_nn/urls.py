from django.urls import path
from map_nn import views

urlpatterns = [
    path('nizhny_novgorod/', views.city_map)
]
