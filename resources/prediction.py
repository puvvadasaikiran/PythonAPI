values=[90,'private','HS-grad','Widowed','Prof-speciality','Not-in-family','White','Female',0,43556,40,'United-States']
# ['Age', 'Work Class', 'Education', 'Marital Status', 'Occupation','Relationship', 'Race', 'Sex', 'Capital Gain', 'Capital Loss','Hours per Week', 'Country']
#create lists with categories
Work_Class=['Federal-gov', 'Local-gov', 'Never-worked', 'Private', 'Self-emp-inc', 'Self-emp-not-inc', 'State-gov', 'Without-pay', 'private']
Education=['10th', '11th', '12th', '1st-4th', '5th-6th', '7th-8th', '9th', 'Assoc-acdm', 'Assoc-voc', 'Bachelors', 'Doctorate', 'HS-grad', 'Masters', 'Preschool', 'Prof-school', 'Some-college']
Marital_Status=['Divorced', 'Married-AF-spouse', 'Married-civ-spouse', 'Married-spouse-absent', 'Never-married', 'Separated', 'Widowed']
Occupation=['Adm-clerical', 'Armed-Forces', 'Craft-repair', 'Exec-managerial', 'Farming-fishing', 'Handlers-cleaners', 'Machine-op-inspct', 'Other-service', 'Priv-house-serv', 'Prof-speciality', 'Prof-specialty', 'Protective-serv', 'Sales', 'Tech-support', 'Transport-moving']
Relationship=['Husband', 'Not-in-family', 'Other-relative', 'Own-child', 'Unmarried', 'Wife']
Race=['Amer-Indian-Eskimo', 'Asian-Pac-Islander', 'Black', 'Other', 'White']
Sex=['Female', 'Male']
Country=['Cambodia', 'Canada', 'China', 'Columbia', 'Cuba', 'Dominican-Republic', 'Ecuador', 'El-Salvador', 'England', 'France', 'Germany', 'Greece', 'Guatemala', 'Haiti', 'Holand-Netherlands', 'Honduras', 'Hong', 'Hungary', 'India', 'Iran', 'Ireland', 'Italy', 'Jamaica', 'Japan', 'Laos', 'Mexico', 'Nicaragua', 'Outlying-US(Guam-USVI-etc)', 'Peru', 'Philippines', 'Poland', 'Portugal', 'Puerto-Rico', 'Scotland', 'South', 'Taiwan', 'Thailand', 'Trinadad&Tobago', 'United-States', 'Vietnam', 'Yugoslavia']



#read entries into list named values

#encode categorical values into numerical codes
values[1]=Work_Class.index(values[1])
values[2]=Education.index(values[2])
values[3]=Marital_Status.index(values[3])
values[4]=Occupation.index(values[4])
values[5]=Relationship.index(values[5])
values[6]=Race.index(values[6])
values[7]=Sex.index(values[7])
values[11]=Country.index(values[11])
val=""


import constant as con

for i in values:
    val=val+str(i)+" "

def predict(val):
    #unzip values
    values = val.split()
    
    #reshape values
    import numpy as np
    valarray=np.asarray(values[:10])
    valarray=valarray.reshape(10,1).T

    #scale values
    from sklearn import preprocessing 
    import pickle

    scaled_values=con.scaler_pkl.transform(valarray)

    #predict output
    from sklearn.svm import SVC 

    output=con.svc_pkl.predict(scaled_values)

    #convert output into categorical variable
    incomerange=Income[output[0]]

    #return output
    return(incomerange)

print(predict(val))

