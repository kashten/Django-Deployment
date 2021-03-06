from rest_framework import serializers
from titanic.models import Titanic
from django.contrib.auth.models import User

class TitanicSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Titanic
        fields = "__all__"
        #fields = ('PassengerId',	'Survived'	,'Pclass',	'Name'	,'Sex',	'Age',	'SibSp',	'Parch',	'Ticket',	'Fare'	,'Cabin'	,'Embarked')

# class UserSerializer(serializers.HyperlinkedModelSerializer): #this is for the login user (if needed)
#     class Meta:
#         model = User
#         fields= ('username','password')