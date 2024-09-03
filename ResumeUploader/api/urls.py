from django.urls import path
from . import views

urlpatterns = [
    path('resume/',views.ProfileView.as_view(),name="resume"),
]
