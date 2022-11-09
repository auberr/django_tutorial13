from django.db import models
from users.models import User # 나중에 커스텀 유저를 사용할때 다 바꿔야 된다.
# from django.contrib.auth import get_user_model # 지금 유저모델을 사용
# Create your models here.

class Category(models.Model):
    name = models.CharField("이름", max_length=50)
    description = models.TextField("설명")

    def __str__(self):
        return self.name

class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    category = models.ManyToManyField(Category, verbose_name="카테고리")
    content = models.TextField()

    def __str__(self):
        return f"{self.title} {self.user.username} 님이 작성하신 글입니다."
    
class Comment(models.Model):
    user = models.ForeignKey(User, verbose_name="작성자", on_delete=models.CASCADE)
    article = models.ForeignKey(Article, verbose_name="게시글", on_delete=models.CASCADE)
    contents = models.TextField("본문")

    def __str__(self):
        return str(self.article.title+self.contents)
