from django.db import models # 장고 모델 함수 지정
from users.models import User
from image_optimizer.fields import OptimizedImageField


class Painter(models.Model):
    character1 = models.CharField(max_length=10)
    character2 = models.CharField(max_length=10)
    character3 = models.CharField(max_length=10)
    class meta:
        db_table = 'painters' # 데이터베이스 테이블 이름 새로 지정

class Painting(models.Model) :
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    painter = models.ForeignKey(Painter, on_delete=models.CASCADE)
    
    picture= OptimizedImageField(
        upload_to="uploads/picture/%Y/%m/%d",
        optimized_image_output_size=(300, 300),
        optimized_image_resize_method="cover",  #  "crop", "cover", "contain", "width", "height", "thumbnail" or None
        null=True, blank=True
    )
    painting= OptimizedImageField(
        upload_to="uploads/painting/%Y/%m/%d",
        optimized_image_output_size=(300, 300),
        optimized_image_resize_method="cover",  #  "crop", "cover", "contain", "width", "height", "thumbnail" or None
        null=True, blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)