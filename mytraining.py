import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
import pickle

def data_split(data,ratio):
    np.random.seed(42)
    shuffle=np.random.permutation(len(data))
    test_size=int(len(data)*ratio)
    test_indices=shuffle[:test_size]
    train_indices=shuffle[test_size:]
    return data.iloc[train_indices],data.iloc[test_indices]

if __name__ == '__main__':
    df=pd.read_csv('data.csv')
    train,test=data_split(df,0.2)
    x_train=train[['age','fever','bodypain','difficulty_in_breath','chest_pain','Comorbidity','cough',
    'running_nose','tiredness','blurring_of_speech','loss_of_taste_or_smell','pneumonia','Sore Throat','Diarrhea','Conjunctivitis','Headache','Rash']].to_numpy()
    x_test=test[['age','fever','bodypain','difficulty_in_breath','chest_pain','Comorbidity','cough',
    'running_nose','tiredness','blurring_of_speech','loss_of_taste_or_smell','pneumonia',"Sore Throat","Diarrhea","Conjunctivitis","Headache","Rash"]].to_numpy()
    y_train=train[['infection_probabilty']].to_numpy().reshape(2060 ,)
    y_test=test[['infection_probabilty']].to_numpy().reshape(515,)
    clf=LogisticRegression()
    clf.fit(x_train,y_train)

    file=open('project','wb')
    pickle.dump(clf,file)
    file.close()   
    
    
    
    
    
    
    
    
        