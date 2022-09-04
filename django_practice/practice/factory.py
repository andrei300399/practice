import factory
import factory.django

from .models import Post


class PostFactory(factory.django.DjangoModelFactory):
    title = factory.Faker('lexify')
    text = factory.Faker('lexify')
    author = factory.Faker('name')
    pub_date = factory.Faker('date_time')
    count_likes = factory.Faker('random_number')

    class Meta:
        model = Post