from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from users.models import User
from articles.models import Category, Article
from faker import Faker
from articles.serializers import ArticleSerializer, ArticleCreateSerializer

class ArticleCreateTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user_data = {'email': 'john@john.com', 'password': 'johnpassword'}
        cls.category_data = Category.objects.create()
        cls.article_data = {"title": "some title", "content": "some content", "category": ["1"]}        
        cls.user = User.objects.create_user('john@john.com', 'johnpassword')

    def setUp(self):
        self.access_token = self.client.post(reverse('token_obtain_pair'), self.user_data).data['access']

    def test_fail_if_not_logged_in(self):
        url = reverse("article_view")
        response = self.client.post(url, self.article_data)
        self.assertEqual(response.status_code, 401)

    def test_create_article(self):
        response = self.client.post(
            path = reverse("article_view"),
            data=self.article_data,
            HTTP_AUTHORIZATION = f"Bearer {self.access_token}"
        )
        print(response.data)
        print(response.data["message"])
        self.assertEqual(response.data["message"], "글 작성 완료!!")


    # def setUp(self):
    #     self.user_data = {'email': 'john@john.com', 'password': 'johnpassword'}
    #     self.article_data = {'title': 'some title', 'content': 'some content', 'category': 1}
    #     self.user = User.objects.create_user('john@john.com', 'johnpassword')
    #     self.access_token = self.client.post(reverse('token_obtain_pair'), self.user_data).data['access']

# Create your tests here.


class ArticleReadTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.faker = Faker()
        cls.articles=[]
        for i in range(10):
            cls.author = User.objects.create_user(cls.faker.name(), cls.faker.word())
            cls.articles.append(Article.objects.create(title=cls.faker.sentence(), content=cls.faker.text(), author=cls.author))
        
    def test_get_article(self):
        for article in self.articles:
            url = article.get_absolute_url()
            response = self.client.get(url)
            serializer = ArticleSerializer(article).data
            for key, value in serializer.items():
                self.assertEqual(response.data[key], value)
                print(key, value)
            # self.assertEqual(article.title, response.data[key], value)