from django.contrib.auth import get_user_model
from django.test import TestCase

from posts.models import Post


class ArticleTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        User = get_user_model()
        testuser1 = User.objects.create_user(
            username='testuser1',
            password='testpass123'
        )

        test_post = Post.objects.create(
            author=testuser1,
            title='Article title',
            body='Article content'
        )

    def test_article_content(self):
        post = Post.objects.last()

        author = f'{post.author}'
        title = f'{post.title}'
        body = f'{post.body}'

        self.assertEqual(author, 'testuser1')
        self.assertEqual(title, 'Article title')
        self.assertEqual(body, 'Article content')
