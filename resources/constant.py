from sklearn import preprocessing
import pickle

with open("scaler.pkl", 'rb') as file1:
    scaler_pkl = pickle.load(file1)

#predict output
from sklearn.svm import SVC 
with open("adultincome.pkl", 'rb') as file2:
    svc_pkl = pickle.load(file2)

