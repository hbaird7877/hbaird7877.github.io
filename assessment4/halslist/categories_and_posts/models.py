from django.db import models

from django.conf import settings

# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=200)
    creation_date = models.DateField()
    

    def __str__(self):
        return f"{self.category_name} {self.creation_date}"

class Post(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='posts')
    post_title = models.CharField(max_length=200)
    poster_name = models.CharField(max_length=200)
    creation_date = models.DateField()
    post_text = models.TextField()
    telephone = models.CharField(max_length=15)
    email = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f"{self.poster_name} {self.post_title}"