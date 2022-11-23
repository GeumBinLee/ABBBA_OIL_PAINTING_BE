
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from inquiries.serializers import CommentSerializer, CommentCreateSerializer
from inquiries.models import Inquiry, Comment
from inquiries.serializers import InquiryCreateSerializer, InquirySerializer


class InquiryView(APIView):

    def get(self, request):
        if request.user.is_admin == 1:
            inquiry = Inquiry.objects.all()
            serializer = InquirySerializer(inquiry, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        else:
            inquiry = Inquiry.objects.filter(user = request.user)
            serializer = InquirySerializer(inquiry, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self,request):
        serializer = InquiryCreateSerializer(data = request.data)
        if serializer.is_valid():
            
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class InquiryDetailView(APIView):

    def get(self, request, inquiry_id):
        inquiry = get_object_or_404(Inquiry, id= inquiry_id)
        if request.user.is_admin == 1:
            serializer = InquirySerializer(inquiry)
            return Response(serializer.data, status = status.HTTP_200_OK)
        else:
            if  request.user ==inquiry.user:
                serializer = InquirySerializer(inquiry)
                return Response(serializer.data, status = status.HTTP_200_OK)
            else:
                return Response("권한이 없습니다!", status = status.HTTP_403_FORBIDDEN)

    def delete(self,request,inquiry_id):
        inquiry = get_object_or_404(Inquiry, id= inquiry_id)
        if request.user == inquiry.user:
            inquiry.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response("권한이 없습니다!", status = status.HTTP_403_FORBIDDEN)


# # 댓글 관련 view
class CommentView(APIView):
    
    def get(self, request, inquiry_id):
        inquiry = Inquiry.objects.get(id= inquiry_id)
        comments = inquiry.comment_set.all()
        serializer = CommentSerializer(comments, many =True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self,request, inquiry_id):
        serializer = CommentCreateSerializer(data = request.data)
        if serializer.is_valid():
            
            serializer.save(user=request.user, inquiry_id = inquiry_id)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CommentDetailView(APIView):

    def put(self, request, inquiry_id, comment_id):
        comment = get_object_or_404(Comment, id= comment_id)
        if request.user == comment.user:
            serializer = CommentCreateSerializer(comment, data = request.data)
            if serializer.is_valid(): 
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response("권한이 없습니다", status = status.HTTP_403_FORBIDDEN)

    
    def delete(self, request, inquiry_id, comment_id):
        comment = get_object_or_404(Comment,id= comment_id)
        if request.user == comment.user:
            comment.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response("권한이 없습니다", status = status.HTTP_403_FORBIDDEN)
