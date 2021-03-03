from django.contrib.auth import get_user_model
from django.test import TestCase

from posts.models import Post


class BlogTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        User = get_user_model()
        testuser1 = User.objects.create_user(
            username='testuser1',
            password='testpass123'
        )

        test_post = Post.objects.create(
            author=testuser1,
            title='Blog title',
            body='Body content'
        )

    def test_blog_content(self):
        post = Post.objects.last()

        author = f'{post.author}'
        title = f'{post.title}'
        body = f'{post.body}'

        self.assertEqual(author, 'testuser1')
        self.assertEqual(title, 'Blog title')
        self.assertEqual(body, 'Body content')
