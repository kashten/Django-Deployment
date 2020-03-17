
import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
import pickle
import os

df = pd.read_csv ("titanic.csv")

def pre_process (df):

    def get_title(name):
        if '.' in name:
            return name.split(',')[1].split(',')[0].strip()
        else:
            return 'Unknown'
        
    def title_map (title):
        if title in ['Mr']:
            return 1
        elif title in ['Master']:
            return 3
        elif title in ['Miss','Ms','Mlle']:
            return 4
        elif title in ['Mme','Mrs']:
            return 5
        else:
            return 2
        
    df['title'] = df['Name'].apply(get_title).apply(title_map)
    df = df.drop(['PassengerId','Name','Ticket'], axis=1)
    df['Sex'] = df['Sex'].replace(['male','female'], [0,1])
    df['Cabin'] = df['Cabin'].isna()
    df = pd.get_dummies(df)
    df['Age'][df["Age"].isna()] = df['Age'].mean()
    mf=df['Fare'].mean()
    df['Fare']=df['Fare']>mf
    df['Fare']=df['Fare'].astype(int)
    return df    


def training (df):
    
    df = pre_process(df)
    y=df['Survived']
    X = df.drop('Survived', axis=1)
    dummyRow = pd.DataFrame(np.zeros(len(X.columns)).reshape(1,len(X.columns)), columns=X.columns) #creates this for test prediction.
    dummyRow.to_csv("dummyRow.csv", index=False)

    model = LogisticRegression()
    model.fit(X,y)

    pickle_file = "pickle_model.pkl"
    with open (pickle_file, 'wb') as file: #wb - write/open file in binary mode.
        pickle.dump(model,file)


    print (model.score(X,y))
    yp = model.predict(X)
    print ("Sur",sum(yp!=0))
    print ("Not Sur", sum(yp==0))
    print(confusion_matrix(y, yp))
    
    
def pred(ob):
    d1 = ob.to_dict() #convert object into dictionary and create a df.
    df = pd.DataFrame(d1, index=[0])
    df.drop("Survived", axis=1, inplace=True) #Dropping target feature before pre-processing.
    df = pre_process(df)
    dummyrow_filename = 'dummyRow.csv'
    dummyrow_filename = os.path.dirname(__file__)+"/" + dummyrow_filename  #dummyRow is used for the dummified columns (Embarked)
    df2 = pd.read_csv(dummyrow_filename)                                       #dummyRow is all the columns during training with  1 row of 0 values.
    for c1 in df.columns: #Add each column from df to df2.
        df2[c1]=df[c1]
   #Load the pickled model.
    pickle_filename = "pickle_model.pkl"
    pickle_filename=os.path.dirname(__file__)+"/"+pickle_filename #__file__ is current file (TiML2). Need to specify the os path.
    with open (pickle_filename, 'rb') as file:
        model = pickle.load(file) 
    pred = model.predict(df2)
    return pred
    
    
if __name__ == "__main__":
    df = pd.read_csv("titanic.csv")
    training(df)
    #print ("Python - This will run if the file is run as a main, and not a support file")



