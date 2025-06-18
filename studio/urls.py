from django.urls import path
from .views import *

urlpatterns = [
    path('classes/', ClassListAPIView.as_view()),
    path('book/', BookClassAPIView.as_view()),
    path('bookings/', BookingListByEmailAPIView.as_view()),
    path('classes/create/', CreateFitnessClassAPIView.as_view()),

]
