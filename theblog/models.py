from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
from datetime import timedelta



class Post(models.Model):
    title=models.CharField(max_length=255)
    title_blog=models.CharField(max_length=255, default="Blog")
    author= models.ForeignKey(User,on_delete=models.CASCADE)
    body=models.TextField()
    image = models.ImageField(upload_to='blog_images/', blank=True, null=True)
    date=models.DateTimeField(default=timezone.now)
    likes = models.ManyToManyField(User, related_name='liked_posts', blank=True)
    
    def __str__(self):
        return self.title + '|' + str(self.author)
    
    @property
    def title_tag(self):
        return self.title + " | " + self.title_blog
    def get_absolute_url(self):
        return reverse('article_detail', args=(self.id,))
    
    def total_likes(self):
        return self.likes.count()
    
class Comment(models.Model):
    post= models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    date=models.DateTimeField(default=timezone.now)
    def __str__(self):
        return f"Comment by {self.user.username} on {self.post.title}"
    
def default_expiry():
    return timezone.now() + timedelta(seconds=5)

class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    message = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField(default=default_expiry)

    def __str__(self):
        return f"Notification for {self.user.username}: {self.message}"