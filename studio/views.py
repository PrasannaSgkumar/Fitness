from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import FitnessClass, Booking
from .serializers import FitnessClassSerializer, BookingSerializer
from django.utils.timezone import now

class ClassListAPIView(APIView):
    def get(self, request):
        classes = FitnessClass.objects.filter(datetime__gte=now())
        serializer = FitnessClassSerializer(classes, many=True)
        return Response(serializer.data)

class BookClassAPIView(APIView):
    def post(self, request):
        data = request.data
        try:
            fitness_class = FitnessClass.objects.get(id=data["class_id"])
        except FitnessClass.DoesNotExist:
            return Response({"error": "Class not found."}, status=404)
        
        if fitness_class.available_slots <= 0:
            return Response({"error": "No slots available."}, status=400)

        booking = Booking.objects.create(
            fitness_class=fitness_class,
            client_name=data["client_name"],
            client_email=data["client_email"]
        )
        fitness_class.available_slots -= 1
        fitness_class.save()

        return Response(BookingSerializer(booking).data, status=201)

class BookingListByEmailAPIView(APIView):
    def get(self, request):
        email = request.query_params.get("client_email")
        if not email:
            return Response({"error": "client_email is required"}, status=400)
        bookings = Booking.objects.filter(client_email=email)
        return Response(BookingSerializer(bookings, many=True).data)


class CreateFitnessClassAPIView(APIView):
    def post(self, request):
        serializer = FitnessClassSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
