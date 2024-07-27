from django.db import models
from product.models import Car
# Create your models here.
class userComment(models.Model):
    car = models.ForeignKey(Car,related_name='comments',on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.name