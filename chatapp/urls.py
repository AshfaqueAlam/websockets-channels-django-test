from django.urls import path, include
from . import views

urlpatterns = [
    # path('home/', views.HomeView, name = 'home'),
    path('home/', views.HomeView.as_view()),
]