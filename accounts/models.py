from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    # nickname 필드 추가
    nickname = models.CharField(max_length=30)

    # 객체의 문자열 표현 정리 : User view에서 쓸 때 username이 return 됨
    def __str__(self):
        return self.username

