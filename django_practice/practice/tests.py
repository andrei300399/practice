import datetime
from django.test import TestCase
from practice.models import Post
from django.urls import reverse
from unittest.mock import patch
from .factory import PostFactory
import allure


class PostTestCase(TestCase):

    def test_first(self):
        """simle 1==1"""
        self.assertEqual(1, 1)


    def test_creation_post_model(self):
        with allure.step("Создание первого поста"):
            Post.objects.create(
                title='post_title_1',
                text='post_text_1',
                author='post_author_1',
                pub_date=datetime.datetime.now(),
                count_likes=5
            )

        with allure.step("Создание второго поста"):
            post2 = Post.objects.create(
                title='post_title_2',
                text='post_text_2',
                author='post_author_2',
                pub_date=datetime.datetime.now(),
                count_likes=15
            )
        with allure.step("Проверка созданных постов"):
            self.assertEqual(2, Post.objects.count())
            get_post2 = Post.objects.get(title="post_title_2")
            self.assertEqual(get_post2.title, post2.title)

    def test_view_get_posts(self):
        with allure.step("Создание 10 постов"):
            posts = PostFactory.create_batch(10)
            with allure.step("Открыть главную страницу ср всеми постами"):
                with patch.object(Post.objects, 'values', return_value=posts):
                    url = reverse("practice:index")
                    response = self.client.get(url)
                    self.assertEqual(response.status_code, 200)
                    with allure.step("Проверка созданных постов"):
                        for post in posts:
                            self.assertIn(post.title, str(response.content))
                            self.assertIn(post.text, str(response.content))
                            self.assertIn(post.author, str(response.content))
                            self.assertIn(str(post.count_likes), str(response.content))

    def test_creation_post_view(self):
        data_mock = {
            "add_title": "create_title_1",
            "add_text": "create_text_1",
            "add_author": "create_author_1",
            "add_count_likes": 5,
        }
        with allure.step("Создание поста"):
            post = PostFactory.build()
            with patch.object(Post.objects, 'create', return_value=post):
                response_create = self.client.post(reverse("practice:add_post"), data_mock)
                self.assertEqual(response_create.status_code, 302)
                with allure.step("Проверка, что созданный пост отображается на странице"):
                    with patch.object(Post.objects, 'values', return_value=[post]):
                        url = reverse("practice:index")
                        response = self.client.get(url)
                        self.assertEqual(response.status_code, 200)
                        self.assertNotIn(data_mock["add_title"], str(response.content))
                        self.assertNotIn(data_mock["add_text"], str(response.content))
                        self.assertNotIn(data_mock["add_author"], str(response.content))
                        self.assertIn(post.title, str(response.content))
                        self.assertIn(post.text, str(response.content))
                        self.assertIn(post.author, str(response.content))
                        self.assertIn(str(post.count_likes), str(response.content))

    def test_delete_post_model(self):
        with allure.step("Создание первого поста"):
            Post.objects.create(
                title='post_title_1',
                text='post_text_1',
                author='post_author_1',
                pub_date=datetime.datetime.now(),
                count_likes=5
            )
        with allure.step("Создание второго поста"):
            post2 = Post.objects.create(
                title='post_title_2',
                text='post_text_2',
                author='post_author_2',
                pub_date=datetime.datetime.now(),
                count_likes=15
            )
        with allure.step("Удаление второго поста"):
            post_delete = Post.objects.get(title=post2.title)
            post_delete.delete()

        with allure.step("Проверка удаления второго поста"):
            get_post2 = Post.objects.all()
            self.assertNotIn(post_delete, get_post2)



