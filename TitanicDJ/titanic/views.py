from django.http.response import HttpResponse
from rest_framework import viewsets
from titanic.models import Titanic
from rest_framework.response import Response
from titanic import TiML2
from titanic.serializers import TitanicSerializer

#Change queryset and serializer_class.

class TitanicViewSet(viewsets.ModelViewSet): #ModelViewSet is a set of 5 views Django makes (create/delete/update etc).
    queryset = Titanic.objects.all().order_by('-id') #-id is descending order. Note: Titanic is the model here. Can also filter using Titanic.objects.filter(subject__icontains='exam')
    serializer_class = TitanicSerializer                #subject is the column and icontains is ignore case. Will search for 'exam' in the column regardless of case.

#this overwrites the method. View creates 5 sets and during the create phase, we're overwriting it since it not only has to store to DB but also show prediction.
    def create (self, request, *args, **kwargs):  
        viewsets.ModelViewSet.create(self,request,*args,**kwargs) #write on the db as usual.
        ob=Titanic.objects.latest('id') #pull the latest object and predict survival.
        sur=TiML2.pred(ob) #Predict 
        return Response ({"status": "Success", "Survived": sur, 'temp': args}) #returns json of prediction.



# class UserViewSet(viewsets.ModelViewSet):
#     queryset=User.objects.all().order_by('-id')
#     serializer_class=UseSerializer
