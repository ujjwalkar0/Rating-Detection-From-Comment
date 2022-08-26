from rest_framework.serializers import ModelSerializer
from rating.models import RatingReview

class RatingReviewSerializer(ModelSerializer):
    class Meta:
        models = RatingReview
        fields = '__all__'