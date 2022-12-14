from curses import use_default_colors
from django.shortcuts import render

# Create your views here.
from rating.models import RatingReview
from rest_framework.views import APIView
from rating.serializers import RatingReviewSerializer
from rest_framework.response import Response
from rest_framework import status
import numpy as np

class RatingView(APIView):
    def get(self, request, id, *args, **kwargs):
        rates = [i.rating for i in RatingReview.objects.filter(user_id=id)]
        if len(rates) == 0:
            rating = 0
        else:
            rating = np.average(rates)
        
        print(rates, rating)

        return Response({"Rating": rating, "Rates": rates})

    def post(self, request, *args, **kwargs):
        data = request.data
        rating = RatingReview.objects.create(
            user_id=data["user_id"], 
            que_1=data["que_1"], 
            que_2=data["que_2"], 
            que_3=data["que_3"], 
            que_4=data["que_4"], 
            que_5=data["que_5"],    
            rating=0    
        )

        return Response({"Message":"Success"})

        # serializer = RatingReviewSerializer(data=request.data)
        # print(serializer)
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(serializer.data, status=status.HTTP_201_CREATED)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)