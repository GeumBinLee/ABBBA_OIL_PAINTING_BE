from django.urls import path
from inquiries import views

urlpatterns = [

      path('',views.InquiryView.as_view(), name='inquiry_view'),
      path('<int:inquiry_id>/',views.InquiryDetailView.as_view(), name='inquiry_detail_view'),
      path('<int:inquiry_id>/comment/',views.CommentView.as_view(), name='comment_view'),
      path('<int:inquiry_id>/comment/<int:comment_id>/',views.CommentDetailView.as_view(), name='comment_Detail_view'),

]