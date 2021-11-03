from imblearn.over_sampling import ADASYN
from collections import Counter
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import warnings
import pickle


pd.set_option('display.max_columns',None)
warnings.filterwarnings(action='ignore')


df = pd.read_csv(r"C:\Users\Lenovo\PycharmProjects\GermanBankCreditCard\SouthGermanCredit\Preprocess.csv")
df.drop(['Unnamed: 0'],axis=1,inplace=True)


df.isnull().sum()


q1 = df.quantile(0.25)
q3 = df.quantile(0.75)
IQR = q3-q1


((df < (q1-1.5*IQR)) | (df > (q3+1.5*IQR))).sum()


columns=['duration','purpose','amount','other_debtors','age','other_installment_plans','housing','number_credits','job',
        'people_liable','foreign_worker']
for i in columns:
    q75,q25=np.percentile(df[i],[75,25])
    iqr=q75 - q25
    minimum = q25 - 1.5*iqr
    maximum = q75 + 1.5*iqr
    df.loc[df[i] < minimum, i] = minimum
    df.loc[df[i] > maximum, i] = maximum


((df < (q1-1.5*IQR)) | (df > (q3+1.5*IQR))).sum()


df.skew()

col=['amount','savings','number_credits']
for i in col:
    df[i]=np.log(df[i]+1)


df.skew()


for i in df.columns:
    sns.displot(data=df,x=i,kde=True)


del df['other_debtors']
del df['other_installment_plans']
del df['housing']
del df['job']
del df['people_liable']
del df['foreign_worker']


scaling = [feature for feature in df.columns if feature not in ['credit_risk']]


from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaler.fit(df[scaling])


scaler.transform(df[scaling])


df2=pd.DataFrame(scaler.transform(df[scaling]),columns=df[scaling].columns)


final=pd.concat([df[['credit_risk']].reset_index(drop=True),df2],axis=1)
final.head()


final.to_csv(r'C:\Users\Lenovo\PycharmProjects\GermanBankCreditCard\SouthGermanCredit\Final_Model.csv')


file = 'Scaler_Credit_Data.pkl'

pickle.dump(scaler,open(file,'wb'))