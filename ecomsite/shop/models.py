from django.db import models

# Create your models here.
class Products(models.Model):

    def __str__(self):
        return self.title
    
    title = models.CharField(max_length=200)
    price = models.FloatField()
    discount_price = models.FloatField()
    category = models.CharField(max_length=200)
    description = models.TextField()
    image = models.CharField(max_length=300)


