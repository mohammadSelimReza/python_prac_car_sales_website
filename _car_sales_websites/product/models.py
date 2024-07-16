from django.db import models

# Create your models here.
class Brand(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=100,unique=True, null=True,blank=True)
    
    def __str__(self) -> str:
        return self.name

class Car(models.Model):
    brand_name = models.ForeignKey(Brand,related_name='car_brand',on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=10,decimal_places=2)
    quantity = models.PositiveIntegerField()
    image = models.ImageField(upload_to='media/car_images/')
    def __str__(self) -> str:
        return self.title    
    