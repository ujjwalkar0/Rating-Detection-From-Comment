from django.contrib import admin
from django.urls import path, include
from rating.views import RatingView

urlpatterns = [
    path('', RatingView.as_view(),),
    path('<int:id>/', RatingView.as_view(),),
]