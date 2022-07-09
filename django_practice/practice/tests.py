import datetime

from django.test import TestCase
from practice.models import Post
from django.urls import reverse

class PostTestCase(TestCase):

    def test_first(self):
        """simle 1==1"""
        self.assertEqual(1, 1)

    def test_creation_post(self):
        post1 = Post.objects.create(
            title='username1',
            text='email1@email.ru',
            author='password',
            pub_date=datetime.datetime.now(),
            count_likes=5
        )

        post2 = Post.objects.create(
            title='username2',
            text='email1@email.ru222',
            author='password22',
            pub_date=datetime.datetime.now(),
            count_likes=5
        )

        self.assertEqual(2, Post.objects.count())
        get_post2 = Post.objects.get(title="username2")
        self.assertEqual(get_post2.title, post2.title)

    def test_view_post(self):
        url = reverse("practice:index")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
