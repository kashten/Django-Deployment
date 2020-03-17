from django.http.response import HttpResponse
from rest_framework import viewsets
from titanic.models import Titanic
from rest_framework.response import Response
from titanic import TiML2
from titanic.serializers import TitanicSerializer

class TitanicViewSet(viewsets.ModelViewSet):
    queryset = Titanic.objects.all().order_by('-id')
    serializer_class = TitanicSerializer

    def create (self, request, *args, **kwargs):
        viewsets.ModelViewSet.create(self,request,*args,**kwargs)
        ob=Titanic.objects.latest('id')
        sur=TiML2.pred(ob)
        return Response ({"status": "Success", "Survived": sur, 'temp': args})

# class UserViewSet(viewsets.ModelViewSet):
#     queryset=User.objects.all().order_by('-id')
#     serializer_class=UseSerializer
