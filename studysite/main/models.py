from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Topic(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Room(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)        #CharField와 TextField는 비슷한데 TextField는 조금 더 Large함. 텍스트(김)와 단순 문자열의 차이. 이름은 기껏해야 10글자 내외인데 설명은 김. 
    #null=True는 DB 수준에서 NULL값을 허용한다는 의미. blank=True는 폼 레벨에서 필수가 아니라는 이야기=비워도 유효성 검사 통과.
    #participants = 
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)            
    #auto_now와 auto_now_add의 차이점. auto_now는 스냅샷을 찍었을 때마다, auto_now _add는 업데이트 할 때만.

    def __str__(self):
        return self.name
    
class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)   #일대다 관계에서 참조된 객체(Room)과 관련된 모든 Message들도 삭제된다는 소리임.
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    #django user model 구글링해서 공식 document 참조하기.

    def __str__(self):
        return self.name