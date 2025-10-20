from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Post
from .models import Post, Notification

@receiver(post_save, sender=Post)
def notify_post_created(sender, instance, created, **kwargs):
    if created:
        print(f"✅ A new post was created: {instance.title} by {instance.author}")

@receiver(post_delete, sender=Post)
def notify_post_deleted(sender, instance, **kwargs):
    print(f"🗑️ The post '{instance.title}' was deleted.")

from .models import Post, Notification

@receiver(post_save, sender=Post)
def post_created(sender, instance, created, **kwargs):
    if created:
        Notification.objects.create(message=f"New post added: {instance.title}")