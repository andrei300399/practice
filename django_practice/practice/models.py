from django.db import models

class Post(models.Model):
    title = models.CharField('Заголовок', max_length=100)
    text = models.TextField('Текст поста')
    author = models.CharField('Автор', max_length=100)
    pub_date = models.DateTimeField('Дата публикации', auto_now=True)
    count_likes = models.IntegerField('Количество лайков')

    def __str__(self):
        return self.title