from django.db import models

# Create your models here.
# 게시물과 관련된 클래스 생성
class Article(models.Model):
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    contents = models.TextField()
    url = models.URLField()
    email = models.EmailField() 
    cdate = models.DateTimeField(auto_now_add=True)     # 게시물이 생성된 날짜,시간 # 게시물이 생성이 될 때 자동으로 입력