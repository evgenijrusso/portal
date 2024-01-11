from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Post

class NewsTests(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@email.com',
            password=''
        )

        self.post = Post.objects.create(
            title='A good title',
            content='Nice body content and another',
            author=self.user,
        )

        def test_string_representation(self):
            post = Post(title='A sample title')
            self.assertEqual(str(post), post.title)

        def test_get_absolute_url(self):  # new
            self.assertEqual(self.post.get_absolute_url(), '/post/1/')

        def test_post_content(self):
            self.assertEqual(f'{self.post.title}', 'A good title')
            self.assertEqual(f'{self.post.author}', 'testuser')
            self.assertEqual(f'{self.post.content}', 'Nice body content and another')
