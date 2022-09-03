import datetime

from django.test import TestCase
from practice.models import Post
from django.urls import reverse






class PostTestCase(TestCase):

    def test_first(self):
        """simle 1==1"""
        self.assertEqual(1, 1)

    def test_creation_post_model(self):
        Post.objects.create(
            title='post_title_1',
            text='post_text_1',
            author='post_author_1',
            pub_date=datetime.datetime.now(),
            count_likes=5
        )

        post2 = Post.objects.create(
            title='post_title_2',
            text='post_text_2',
            author='post_author_2',
            pub_date=datetime.datetime.now(),
            count_likes=15
        )

        self.assertEqual(2, Post.objects.count())
        get_post2 = Post.objects.get(title="post_title_2")
        self.assertEqual(get_post2.title, post2.title)

    def test_view_get_posts(self):
        url = reverse("practice:index")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_creation_post_view(self):
        data = {
            "add_title": "create_title_1",
            "add_text": "create_text_1",
            "add_author": "create_author_1",
            "add_count_likes": 5,
        }

        self.client.post(reverse("practice:add_post"), data)
        url = reverse("practice:index")
        response = self.client.get(url)
        self.assertIn(data["add_title"], str(response.content))
        self.assertIn(data["add_text"], str(response.content))
        self.assertIn(data["add_author"], str(response.content))
        self.assertIn(str(data["add_count_likes"]), str(response.content))

    def test_delete_post_model(self):
        Post.objects.create(
            title='post_title_1',
            text='post_text_1',
            author='post_author_1',
            pub_date=datetime.datetime.now(),
            count_likes=5
        )

        post2 = Post.objects.create(
            title='post_title_2',
            text='post_text_2',
            author='post_author_2',
            pub_date=datetime.datetime.now(),
            count_likes=15
        )

        post_delete = Post.objects.get(title=post2.title)
        post_delete.delete()

        get_post2 = Post.objects.all()
        self.assertNotIn(post_delete, get_post2)



