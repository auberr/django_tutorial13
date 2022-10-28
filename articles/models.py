from django.db import models
from django.contrib.auth.models import User # 나중에 커스텀 유저를 사용할때 다 바꿔야 된다.
from django.contrib.auth import get_user_model # 지금 유저모델을 사용
# Create your models here.

class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content = models.TextField()

    def __str__(self):
        return str(self.title)
    
