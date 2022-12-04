from django.db import models
from users.models import User
from image_optimizer.fields import OptimizedImageField


class Painter(models.Model):
    name = models.CharField(max_length=10)
    style = OptimizedImageField(upload_to="uploads/style/%Y/%m/%d", optimized_image_output_size=(300, 300), optimized_image_resize_method="cover", null=True, blank=True)


class Painting(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    painter = models.ForeignKey(Painter, on_delete=models.CASCADE)
    picture = OptimizedImageField(upload_to="uploads/picture/%Y/%m/%d", optimized_image_output_size=(300, 300), optimized_image_resize_method="cover", null=True, blank=True)
    painting = OptimizedImageField(upload_to="uploads/painting/%Y/%m/%d", optimized_image_output_size=(300, 300), optimized_image_resize_method="cover", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)