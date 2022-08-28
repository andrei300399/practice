import datetime

from django.test import TestCase
from practice.models import Post
from selenium.webdriver.common.by import By
from django.urls import reverse

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager


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

    def test_add_and_delete_post_ui(self):
        selenium = webdriver.Chrome(executable_path=ChromeDriverManager(path='./').install())
        selenium.get('http://127.0.0.1:8000/')
        input_title = selenium.find_element('id','id_add_title')
        input_text = selenium.find_element('id','id_add_text')
        input_author = selenium.find_element('id','id_add_author')
        input_count_likes = selenium.find_element('id','id_add_count_likes')

        submit = selenium.find_element(By.CSS_SELECTOR,'button[type=submit]')

        input_title.send_keys('Title ui selenium')
        input_text.send_keys('Text ui selenium')
        input_author.send_keys('Author ui selenium')
        input_count_likes.send_keys('98')

        submit.send_keys(Keys.RETURN)

        assert 'Title ui selenium' in selenium.page_source
        assert 'Text ui selenium' in selenium.page_source
        assert 'Author ui selenium' in selenium.page_source
        assert '98' in selenium.page_source

        delete_button = selenium.find_element(By.XPATH, '//p[contains(text(),"Author ui selenium")]/..//a')
        delete_button.send_keys(Keys.RETURN)

        assert 'Title ui selenium' not in selenium.page_source
        assert 'Text ui selenium' not in selenium.page_source
        assert 'Author ui selenium' not in selenium.page_source
        assert '98' not in selenium.page_source


