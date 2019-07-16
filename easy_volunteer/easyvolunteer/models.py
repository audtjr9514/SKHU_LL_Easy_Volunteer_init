from django.db import models
from django.contrib.auth.models import AbstractUser

# 일반 유저
class GeneralUser(AbstractUser):
    codeNum = models.IntegerField()     # 주민 번호
    phoneNum = models.IntegerField()    # 핸드폰 번호
    job = models.ForeignKey('Job', on_delete=models.CASCADE) # 직업
    license = models.CharField(max_length=20)   # 자격증
    level = models.IntegerField(default=1)      # 레벨
    point = models.IntegerField(default=0)      # 가지고 있는포인트
    area = models.ForeignKey('Area', on_delete=models.CASCADE) # 지역
    another = models.CharField(max_length=100)  # 비고
    image = models.ImageField(upload_to='images/', blank=True)  # 이미지
    is_organ = models.BooleanField(default=False)
    organ = models.OneToOneField('Organ')
    def __str(self):
        return self.username

# 기관 유저에 대해 이어줄 테이블 
class Organ(model.Model):
    name = models.CharField(max_length=20)      # 기관명
    crew = models.CharField(max_length=20)      # 소속
    area = models.ForeignKey('Area', on_delete=models.CASCADE)  # 지역
    head = models.CharField(max_length=20)      # 책임자명
    phoneNum = models.IntegerField()            # 핸드폰 번호
    image = models.ImageField(upload_to='images/', blank=True)  # 이미지
    def __str(self):
        return self.name

# 봉사 활동 -> 일반 유저와 기관 유저와 연결
class Service(models.Model):
    name = models.CharField(max_length=40)  # 봉사활동명
    Essential = models.BooleanField(default=True)   # 필수 퀘스트인지의 여부
    Finish = models.BooleanField(default=False)     # 봉사활동의 등록 마감 여부
    point = models.IntegerField()                   # 봉사활동에 해당하는 포인트
    level = models.IntegerField()                   # 어느 레벨에서 열리는지의 레벨
    organ = models.ForeignKey('OrganUser', on_delete=models.CASCADE)    # 기관
    user = models.ManyToManyField('GeneralUser')    # 이에 대한 퀘스트를 할 유저
    number = models.IntegerField(default=15)        # 봉사활동에 참여할 수 있는 최대의 유저 _ 일반 유저가 참여할 때 마다 1씩 차감
    emergency = models.BooleanField(blank=False)    # 긴급 봉사인지의 여부
    image = models.ImageField(upload_to='images/', blank=True)  # 이미지
    def __str__(self):
        return self.name

# 지역
class Area(models.Model):
    area = models.CharField(max_length=20)  # 지역
    def __str__(self):
        return self.area

# 직업
class Job(models.Model):
    job = models.CharField(max_length=20)   # 직업
    def __str__(self):
        return self.name

# 상품
class Product(models.Model):
    name = models.CharField(max_length=30)  # 상품명
    brand = models.ForeignKey('Brand', on_delete=models.CASCADE) # 상품의 브랜드
    point = models.IntegerField()           # 해당 상품의 포인트
    image = models.ImageField(upload_to='images/', blank=True)
    def __str__(self):
        return self.name

# 브랜드
class Brand(models.Model):
    name = models.CharField(max_length=20)  # 브랜드명
    image = models.ImageField(upload_to='images/', blank=True)  # 브랜드 이미지
    def __str__(self):
        return self.name

# Create your models here.
