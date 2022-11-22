from rest_framework import serializers
from inquiries.models import Inquiry, Comment

class InquirySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inquiry
        fields = "__all__"

class InquiryCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inquiry
        fields = ("pk","title","content","created_at",)


class CommentSerializer(serializers.ModelSerializer):
     class Meta:
        model = Comment
        fields = "__all__"

class CommentCreateSerializer(serializers.ModelSerializer):
     class Meta:
        model = Comment
        fields = ("cmt_content",)