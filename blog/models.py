from django.db import models
from django.utils import timezone
from django.conf import settings

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=50)
    hotel_Main_Img = models.ImageField(upload_to='images/')
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    

    def publish(self):
        self.published_date = timezone.now()
        self.save()    

class Gallery(models.Model): 
    name = models.CharField(max_length=50) 
    hotel_Main_Img = models.ImageField(upload_to='images/')
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)


    def __str__(self):
        return self.name
    

    def publish(self):
        self.published_date = timezone.now()
        self.save()