from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .serializers import APIsSerializer
from .models import APIs
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
# Create your views here.

def index(request):
    return HttpResponse("test")

@api_view(['GET'])
def getImages(request):
    res=[] #create an empty list
    for img in APIs.objects.all(): #run on every row in the table...
        res.append({"title":img.title,
                "content":img.content,
               "image":str( img.image)
                }) #append row by to row to res list
    return JsonResponse(res,safe=False) #return array as json response


class APIViews(APIView):
    parser_class=(MultiPartParser,FormParser)
    def post(self,request,*args,**kwargs):
        api_serializer=APIsSerializer(data=request.data)
        if api_serializer.is_valid():
            api_serializer.save()
            return Response(api_serializer.data,status=status.HTTP_201_CREATED)
        else:
            print('error',api_serializer.errors)
            return Response(api_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
