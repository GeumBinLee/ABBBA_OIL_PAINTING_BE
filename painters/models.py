from django.db import models # 장고 모델 함수 지정

# Create your models here.
class Painter(models.Model):
    character_1 = models.varchar(10, null=False) # 캐릭터 1
    character_2 = models.varchar(10, null=False) # 캐릭터 2
    character_3 = models.varchar(10, null=False) # 캐릭터 3
    class meta:
        db_table = 'painters' # 데이터베이스 테이블 이름 새로 지정