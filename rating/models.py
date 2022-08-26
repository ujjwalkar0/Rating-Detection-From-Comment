from django.db import models
from mentalHealth.mentalHealth import detect_mental_health

class RatingReview(models.Model):
    user_id = models.IntegerField(default=None)
    que_1 = models.TextField(default=None)
    que_2 = models.TextField(default=None)
    que_3 = models.TextField(default=None)
    que_4 = models.TextField(default=None)
    que_5 = models.TextField(default=None)
    
    rating = models.IntegerField(default=None)

    def save(self, *args, **kwargs):
        if detect_mental_health(self.que_1)=='unstressed':
            self.rating += 1
        if detect_mental_health(self.que_2)=='unstressed':
            self.rating += 1
        if detect_mental_health(self.que_3)=='unstressed':
            self.rating += 1
        if detect_mental_health(self.que_4)=='unstressed':
            self.rating += 1
        if detect_mental_health(self.que_5)=='unstressed':
            self.rating += 1
        super(RatingReview, self).save(*args, **kwargs)