from django.conf import settings
from django.db import models
from imagekit.models import ProcessedImageField
#이미지 원하는 사이즈로 트리밍 해줌
from imagekit.processors import ResizeToFill


def user_path(instance, filename):
    #instance->포토의 이름, filename-> 파일 이름을 받아온다
    from random import choice
    import string
    
    arr = [choice(string.ascii_letters) for _ in range(8)]
    pid = ''.join(arr)
    #파일 확장자명
    extension = filename.split('.')[-1]
    return 'accounts/{}/{}/{}'.format(instance.user.username, pid, extension)

# Create your models here.
class Profile(models.Model):
    #사용자 정보는 같은 사람이 여러개일수 없으니까 한쪽이 지워지게 되면 양쪽이 지워질 수 있도록, 하나의 유저정보만 가질 수 있도록(on delete 부분)
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE)
    nickname = models.CharField('별명', max_length=20, unique=True)  
    picture = ProcessedImageField(upload_to=user_path,
                                   processors=[ResizeToFill(150,150)],
                                   format='JPEG',
                                   options={'quality':90},
                                   blank=True)
    about = models.CharField(max_length=300, blank=True)
    GENDER_C = (
        ('선택안함', '선택안함'),
        ('여성', '여성'),
        ('남성', '남성'),
    )
    gender = models.CharField('성별(선택사항)', max_length=10, choices=GENDER_C, default='N')
    
    def __str__(self):
        return self.nickname
    