from django.shortcuts import render, get_object_or_404, redirect
import mimetypes
import os
from django.http import HttpResponse, Http404
import urllib
from django.conf import settings
from .models import Painter, Painting

"""
def Download_view(request, pk):
    painting = get_object_or_404(Painting, pk=pk)
    url = painting.image.url[1:]
    file_url = urllib.parse.unquote(url)
    
    if os.path.exists(file_url):
        with open(file_url, 'rb') as fh:
            # quote_file_url = urllib.parse.quote(painting.filename.encode('utf-8'))
            response = HttpResponse(fh.read(), content_type=mimetypes.guess_type(file_url)[0])
            # response['Content-Disposition'] = 'attachment;filename*=UTF-8\'\'%s' % quote_file_url
            return response
        raise Http404
"""    
    
