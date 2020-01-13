#READ DATA
import numpy as np
import pandas as pd
from sklearn import preprocessing 
data1=pd.read_csv('C:/Users/dears/Desktop/python-heroku/pythonapi/resources/adultincome.csv')
data1.columns=['Age', 'Work Class', 'Final Weight', 'Education', 'Education Number', 'Marital Status', 'Occupation',
          'Relationship', 'Race', 'Sex', 'Capital Gain', 'Capital Loss', 'Hours per Week', 'Country', 'Income']

data1.loc[:,:].replace('?',np.nan,inplace=True)


data1.fillna({'Work Class':'private','Occupation':'Prof-speciality','Country':'United-States'},inplace=True)


data1['Education'].replace(' Preschool', 'school',inplace=True)
data1['Education'].replace(' 10th', 'school',inplace=True)
data1['Education'].replace(' 11th', 'school',inplace=True)
data1['Education'].replace(' 12th', 'school',inplace=True)
data1['Education'].replace(' 1st-4th', 'school',inplace=True)
data1['Education'].replace(' 5th-6th', 'school',inplace=True)
data1['Education'].replace(' 7th-8th', 'school',inplace=True)
data1['Education'].replace(' 9th', 'school',inplace=True)
data1['Education'].replace(' HS-Grad', 'HighGrad',inplace=True)
data1['Education'].replace(' HS-grad', 'HighGrad',inplace=True)
data1['Education'].replace(' Some-college', 'CommunityCollege',inplace=True)
data1['Education'].replace(' Assoc-acdm', 'CommunityCollege',inplace=True)
data1['Education'].replace(' Assoc-voc', 'CommunityCollege',inplace=True)
data1['Education'].replace(' Bachelors', 'Bachelors',inplace=True)
data1['Education'].replace(' Masters', 'Masters',inplace=True)
data1['Education'].replace(' Prof-school', 'Masters',inplace=True)
data1['Education'].replace(' Doctorate', 'Doctorate',inplace=True)

data1.drop(['Education Number'], axis = 1, inplace = True)  #one to one mapping of edu nd edu no.

data1.drop(['Final Weight'], axis = 1, inplace = True) #0 correlation

from sklearn.preprocessing import LabelEncoder
labelEncoder = LabelEncoder()

l=[1,2,3,4,5,6,7,11,12]
for i in l:
    data1[data1.columns[i]] = labelEncoder.fit_transform(data1[data1.columns[i]])

X = data1.iloc[:,0:10]  #independent columns
y = data1.iloc[:,-1]    #target column i.e income range

minmax=preprocessing.MinMaxScaler(feature_range=(0,1))
minmax.fit(X)

minmax_data=minmax.transform(X)

import pickle
pkl_filename = "scaler.pkl"
with open(pkl_filename, 'wb') as file:
    pickle.dump(minmax, file)

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(X,y,test_size=0.25)

y_train=y_train.astype('int')

#only outline classification is done using svm-works with hyperplanes
from sklearn.svm import SVC
svc=SVC(kernel='rbf',probability=True)
svc_classifier=svc.fit(x_train,y_train)



#predict on test data
y_predict=svc.predict(x_test)
y_predict

from sklearn.metrics import accuracy_score,recall_score,roc_auc_score,confusion_matrix
from sklearn import metrics

print("\n Accuracy score:%f" %(accuracy_score(y_test,y_predict)*100))
print("\n Recall score:%f" %(recall_score(y_test,y_predict)*100))
print("\n ROC score:%f\n" %(roc_auc_score(y_test,y_predict)*100))
print("\n Precision value is\n",metrics.classification_report(y_test,y_predict))
print(confusion_matrix(y_test,y_predict))

pkl_filename = "adultincome.pkl"
with open(pkl_filename, 'wb') as file:
    pickle.dump(svc, file)
