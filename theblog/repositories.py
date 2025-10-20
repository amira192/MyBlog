
from .models import Post
from django.db.models import Count

class PostRepository:
    @staticmethod
    def get_all_posts():
        return Post.objects.all()

    @staticmethod
    def get_post_by_id(pk):
        return Post.objects.get(pk=pk)

    @staticmethod
    def get_posts_with_author_and_likes():
        return Post.objects.select_related('author').prefetch_related('likes', 'comments').all()

    @staticmethod
    def get_top_liked_posts(limit=5):
        return Post.objects.annotate(num_likes=Count('likes')).order_by('-num_likes')[:limit]
