from django.shortcuts import render

# Create your views here.
from rating.models import RatingReview
from rest_framework.views import APIView
from rating.serializers import RatingReviewSerializer
from rest_framework.response import Response
from rest_framework import status

class RatingView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = RatingReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)