from flask_restful import Resource
import constant as con
import numpy as np
from sklearn import preprocessing 
import pickle
from sklearn.svm import SVC 


Income=[{"result" :'<=50K'}, {"result":'>50K'}]

class PythonAPI(Resource):
  def get(self, val):
    values = val.split("_")

    #reshape values
    valarray=np.asarray(values[:10])
    valarray=valarray.reshape(10,1).T

    #scale values
    scaled_values=con.scaler_pkl.transform(valarray)
    #predict output
    output=con.svc_pkl.predict(scaled_values)

    #convert output into categorical variable
    incomerange=Income[output[0]]

    #return output
    return(incomerange) , 200

  def put(self, val):
    values = val.split("_")

    #reshape values
    valarray=np.asarray(values[:10])
    valarray=valarray.reshape(10,1).T

    #scale values
    scaled_values=con.scaler_pkl.transform(valarray)
    #predict output
    output=con.svc_pkl.predict(scaled_values)

    #convert output into categorical variable
    incomerange=Income[output[0]]

    #return output
    return(incomerange) , 200
    