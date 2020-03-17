from django.db import models

class Titanic(models.Model):
    PassengerId = models.CharField(max_length=50)
    Survived = models.IntegerField(null=True, blank=True)
    Pclass = models.IntegerField(default=0)
    Age = models.IntegerField()
    Name = models.CharField(max_length=50)
    Sex = models.CharField(max_length=6)
    SibSp = models.IntegerField()
    Parch=models.IntegerField()
    Ticket = models.CharField(max_length =10)
    Fare = models.FloatField(default=0)
    Cabin = models.CharField(max_length =10, null=True, blank =True)
    Embarked = models.CharField(max_length =10)


#the data is converteed into a dictionary, since the object needs to fed into a dataframe. Dictionary converts into the dataframe.

    def to_dict(self): #dictionary helps in making a dataframe.
        return {
        'PassengerId': self.PassengerId,
        'Survived': self.Survived,
        'Pclass': self.Pclass,
        'Name':self.Name,
        'Sex':self.Sex,
        'Age':self.Age,
        'SibSp':self.SibSp,
        'Parch':self.Parch,
        'Ticket':self.Ticket,
        'Fare':self.Fare,
        'Cabin':self.Cabin,
        'Embarked':self.Embarked
        
        }

