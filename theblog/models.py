from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone



class Post(models.Model):
    title=models.CharField(max_length=255)
    title_blog=models.CharField(max_length=255, default="Blog")
    author= models.ForeignKey(User,on_delete=models.CASCADE)
    body=models.TextField()
    image = models.ImageField(upload_to='blog_images/', blank=True, null=True)
    date=models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.title + '|' + str(self.author)
    @property
    def title_tag(self):
        return self.title + " | " + self.title_blog
    def get_absolute_url(self):
        return reverse('article_detail', args=(str(self.id)))
        # return reverse('home')
# Create your models here.
