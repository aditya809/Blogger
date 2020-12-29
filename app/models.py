from django.db import models

class SocialLink(models.Model):
    name=models.CharField(max_length=30)
    url=models.URLField()

    def __str__(self):
        return self.name

class Blogs(models.Model):
    title = models.CharField(max_length=100)
    short_description = models.TextField(max_length=200)
    # image_name = models.CharField(max_length=50)
    image_photo = models.ImageField(upload_to='images/',default='NULL') 
    url = models.URLField()

    def __str__(self):
         return self.title