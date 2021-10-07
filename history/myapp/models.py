from django.db import models

# Create your models here.


 class Questions(models.Model):
     title = models.CharField(max_lenght=255)
     content = models.TextField(blank=True)
     created_at = models.DateTimeField(auto_now_add=True)
     photo = models.ImageField(upload_to='photos/%y/%m/%d/')

