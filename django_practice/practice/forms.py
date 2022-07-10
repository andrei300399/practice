from django import forms

class AddPostForm(forms.Form):
    add_title = forms.CharField(label='Заголовок поста', max_length=100)
    add_text = forms.CharField(label='Текст поста', max_length=100)
    add_author = forms.CharField(label='Автор поста', max_length=100)
    add_count_likes = forms.IntegerField(label='Количество лайков')
