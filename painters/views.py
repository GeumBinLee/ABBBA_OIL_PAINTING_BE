from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
import mimetypes
from uuid import uuid4
import os
from django.http import HttpResponse, Http404
import urllib
from painters.models import Painting, Painter
from painters.serializers import ImageCreateSerializer
from painters.serializers import ImageCreateSerializer
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from uuid import uuid4
import os
from painters.serializers import ImageCreateSerializer


# 아직 미구현. 추후에 추가 예정.
def Download_view(request, pk):
    painting = get_object_or_404(Painting, pk=pk)
    url = painting.painting.url[1:]
    file_url = urllib.parse.unquote(url)
    
    if os.path.exists(file_url):
        with open(file_url, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type=mimetypes.guess_type(file_url)[0])
        return HttpResponse({"response":response, "href":painting.painting})
    raise Http404

    

class ConvertView(APIView):
    def post(self, request):
        serializer = ImageCreateSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(user_id=request.user.id) # save시에는 데이터베이스의 테이블의 필드명으로 들어간다. request로 보낼 때는 모델링의 필드명 기준으로 들어간다.
        
        paint = Painting.objects.get(id=serializer.data["id"])
        
        painter_id = paint.painter_id
        painter = Painter.objects.get(id=painter_id)
        style = painter.style
        
        image_painter = str(style)
        image_uuid = uuid4().hex

        # style transfer 명령어 python cli.py 변환하고자하는이미지 변환하고자하는스타일 -s 사이즈 --initial-iterations 정확도(50전후로) -o 저장하고자하는파일명과 경로
        path = os.getcwd()
        os.system(f"python3 {path}/painters/style_transfer/cli.py {path}/{serializer.data['picture'][1:]} {path}/media/{image_painter} -s 156 -ii 100 -o {path}/media/uploads/painting/{image_uuid}.png")
        
        paint.painting = f"/uploads/painting/{image_uuid}.png"
        paint.save()
        return Response(serializer.data, status=status.HTTP_200_OK)


class ImageView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request, id):
        painting = Painting.objects.filter(id=id)
        serializer = ImageCreateSerializer(painting, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)