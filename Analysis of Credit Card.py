from pandas_profiling import ProfileReport
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import warnings
get_ipython().run_line_magic('matplotlib', 'inline')


pd.set_option('display.max_columns',None)
warnings.filterwarnings(action='ignore',message='^internal gelsd')


df = pd.read_csv(r"C:\Users\Lenovo\PycharmProjects\GermanBankCreditCard\SouthGermanCredit\SouthGermanCredit.asc",sep=' ')
df


df=df.rename(columns={'laufkont':'status', 'laufzeit':'duration', 'moral':'credit_history', 'verw':'purpose', 
                      'hoehe':'amount', 'sparkont':'savings', 'beszeit':'employment_duration', 'rate':'installment_rate',
                      'famges':'personal_status_sex', 'buerge':'other_debtors', 'wohnzeit':'present_residence',
                      'verm':'property', 'alter':'age', 'weitkred':'other_installment_plans', 'wohn':'housing',
                      'bishkred':'number_credits', 'beruf':'job', 'pers':'people_liable', 'telef':'telephone',
                      'gastarb':'foreign_worker', 'kredit':'credit_risk'})


df.info()


numerical_feature = [feature for feature in df.columns if df[feature].dtypes != "O"]


print('Number of Numerical Feature :', len(numerical_feature))


for feature in numerical_feature:
    print('The feature is {} and number of categories are {}'.format(feature,len(df[feature].unique())))


discrete_variable=[feature for feature in numerical_feature if len(df[feature].unique())<9]


print('Discrete Variable Feature : {}'.format(len(discrete_variable)))


continous_variable=[feature for feature in numerical_feature if feature not in df[discrete_variable]]


print('Continous Variable Feature : {}'.format(len(continous_variable)))


df.isnull().sum()


sns.set_theme(style='darkgrid')
sns.countplot(x='credit_risk',data=df)


sns.set_theme(style='darkgrid')
sns.countplot(x='foreign_worker',hue='credit_risk',data=df)


sns.set_theme(style='darkgrid')
sns.countplot(x='credit_risk',hue='purpose',data=df)


plt.hist(x='amount',bins=30,data=df)


df[df['credit_risk']==0]


plt.hist(data=df[df['credit_risk']==0],x='amount')
plt.title('Bad Loans Amount Histogram')


max(df[df['credit_risk']==0]['amount'])

plt.figure(figsize=(25,25),facecolor='white')
plotnumber = 1

for i in discrete_variable:
    # There Are 17 Feature In Discrete Variable
    if plotnumber <= 17:
        ax = plt.subplot(5,4,plotnumber)
        sns.countplot(x=i,data=df[discrete_variable])
        plt.xlabel(i,fontsize=20)
    plotnumber += 1
plt.show()


plt.figure(figsize=(10,10))
plotnumber = 1

for i in continous_variable:
    # There Are 4 Feature In Continous Variable
    if plotnumber <= 4:
        ax = plt.subplot(2,2,plotnumber)
        sns.histplot(x=i,data=df[continous_variable])
        plt.xlabel(i,fontsize=20)
    plotnumber += 1
plt.show()


df.to_csv(r'C:\Users\Lenovo\PycharmProjects\GermanBankCreditCard\SouthGermanCredit\Preprocess.csv')
