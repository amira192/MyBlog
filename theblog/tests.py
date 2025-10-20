from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Post, Comment

class BlogTestCase(TestCase):

    def setUp(self):
        
        self.user = User.objects.create_user(username='test', password='12345')
        self.client.login(username='test', password='12345')
        
        
        self.post = Post.objects.create(title='Test Post', body='Test body', author=self.user)

    def test_home_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.post.title)

    def test_article_detail_view(self):
        response = self.client.get(reverse('article_detail', args=[self.post.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.post.title)
        self.assertContains(response, self.post.body)

    def test_add_post(self):
        response = self.client.post(reverse('add_post'), {
            'title': 'New Post',
            'body': 'New post body',
            'author': self.user.id
        })
        self.assertEqual(response.status_code, 302)  
        new_post = Post.objects.get(title='New Post')
        self.assertEqual(new_post.body, 'New post body')

    def test_update_post(self):
        response = self.client.post(reverse('update_post', args=[self.post.pk]), {
            'title': 'Updated Title',
            'body': 'Updated body'
        })
        self.post.refresh_from_db()
        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.post.title, 'Updated Title')
        self.assertEqual(self.post.body, 'Updated body')

    def test_delete_post(self):
        response = self.client.post(reverse('delete_post', args=[self.post.pk]))
        self.assertEqual(response.status_code, 302)
        with self.assertRaises(Post.DoesNotExist):
            Post.objects.get(pk=self.post.pk)

    def test_like_post(self):
        
        self.assertEqual(self.post.likes.count(), 0)

        
        response = self.client.get(reverse('like_post', args=[self.post.pk]))
        self.post.refresh_from_db()
        self.assertEqual(self.post.likes.count(), 1)
        self.assertIn(self.user, self.post.likes.all())
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('article_detail', args=[self.post.pk]))

        
        response = self.client.get(reverse('like_post', args=[self.post.pk]))
        self.post.refresh_from_db()
        self.assertEqual(self.post.likes.count(), 0)

    def test_add_comment(self):
        response = self.client.post(reverse('article_detail', args=[self.post.pk]), {
            'body': 'Test comment'
        })
        self.assertEqual(response.status_code, 302)
        comment = Comment.objects.get(body='Test comment')
        self.assertEqual(comment.post, self.post)
        self.assertEqual(comment.user, self.user)

    def test_search_results(self):
        response = self.client.get(reverse('search-results'), {'q': 'Test'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.post.title)
