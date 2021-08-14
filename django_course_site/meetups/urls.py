from django.urls import path
from django.urls.resolvers import URLPattern

from . import views

urlpatterns = [
    path('meetups/', views.index) # our-domain.com/meetups
]