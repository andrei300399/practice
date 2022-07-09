from django.test import TestCase
from models import Post

class PostTestCase(TestCase):

    def test_first(self):
        """simle 1==1"""
        self.assertEqual(1, 1)

    def test_creation_post(self):
        post1 = Post.objects.create_user(
            title='username1',
            text='email1@email.ru',
            author='password',
        )

        post2 = Post.objects.create_user(
            title='username2',
            text='email1@email.ru222',
            author='password22',
        )

        self.assertEqual(2, Post.objects.count())
        get_post2 = Post.objects.get(title="username2")
        self.assertEqual(get_post2.title, post2.title)

    def test_view_post(self):
        response = self.client.get('127.0.0.1:8000')
        self.assertEqual(response.status_code, 200)
