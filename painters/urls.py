from django.urls import path
from painters import views

urlpatterns = [
        # path('download/<int:pk>', views.Download_view, name="download"), # 미구현
        path('convert/', views.ConvertView.as_view(), name='convert_view'),
        path("painting/<int:id>/", views.ImageView.as_view(), name="image_view"),
]