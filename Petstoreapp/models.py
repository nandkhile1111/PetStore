from django.db import models

# Create your models here.
    
class Category(models.Model):
    cid = models.AutoField(primary_key=True)
    name = models.CharField(max_length =255)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length = 255)
    price = models.IntegerField()
    detail = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    image = models.ImageField(upload_to="productimages/", null=True)

    def __str__(self):
        return self.name