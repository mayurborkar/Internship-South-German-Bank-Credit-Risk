# Internship-South-German-Bank-Credit-Risk

## Table of Content
- Introduction
- Approach
- User Interface
- Deployment Link
- File Structure
- Installation
- Technology Used
- Document

## Introduction
Normally, most of the bank's wealth is obtained from providing credit loans so that a marketing bank must be able to reduce the risk of non-performing credit loans. The risk
of providing loans can be minimized by studying patterns from existing lending data. One technique that you can use to solve this problem is to use data mining techniques.
Data mining makes it possible to find hidden information from large data sets by way of classification. The goal of this project, you have to build a model to predict whether the person, described by the attributes of the dataset, is a good (1) or a bad (0) credit risk

**Input variables are:**
~~~
1. laufkont = status
2. laufzeit = duration
3. moral = credit_history
4. verw = purpose
5. hoehe = amount
6. sparkont = savings
7. beszeit = employment_duration
8. rate = installment_rate
9. famges = personal_status_sex
10. buerge = other_debtors
11. wohnzeit = present_residence
12. verm = property
13. alter = age
14. weitkred = other_installment_plans
15. wohn = housing
16. bishkred = number_credits
17. beruf = job
18. pers = people_liable
19. telef = telephone
20. gastarb = foreign_worker
~~~

**Output variables:**

`1. kredit = credit_risk`

## Approach
~~~
1. Data Exploration     : I started exploring dataset using pandas,numpy,matplotlib and seaborn. 

2. Data visualization   : Ploted graphs to get insights about dependend and independed variables. 

3. Feature Engineering  :  All The Value Are Arrange In One Range.

4. Model Selection I    :  Tested all base models to check the base accuracy.
                       
5. Model Selection II   :  Performed Hyperparameter tuning using gridsearchCV.

6. Pickle File          :  Selected model as per best accuracy and created pickle file using Pickle .

7. Webpage & deployment :  1. Created a web form that takes all the necessary inputs from user and shows output.
                           2. Frist We had Deploy at Heroku Platform
                           3. After that We had deployed project on AWS Elastic Net
~~~

## User Interface
The Prediction of Credit Risk Final Model Run in Local Enviornment

1. Main Page :

![Screenshot (94)](https://user-images.githubusercontent.com/62636740/139243173-98a35c5f-d7b8-4246-9287-0d9e4d2dd668.png)

2. Result Page :

![Screenshot (93)](https://user-images.githubusercontent.com/62636740/139243363-4c46d61b-8c29-4492-b766-311153d4b443.png)

## Deployment Link

Heroku Link : https://south-german-bank-credit-risk.herokuapp.com/

Heroku Link For Data Report : https://south-german-bank-credit-risk.herokuapp.com/report

AWS Link : http://creditriskofgermanbank-env.eba-upbvpmsv.us-east-2.elasticbeanstalk.com/

AWS Link For Data Report : http://creditriskofgermanbank-env.eba-upbvpmsv.us-east-2.elasticbeanstalk.com/report

## File Structure
~~~
Project
|
|
|
application_logging--|--logger.py
|
|
|
database_coonection--|
|                    |--Database.py
|                            
|
images-------------------------|--credit_card.jpg
|                              |--Credit_card.webp
|
|
SouthGermanCredit--------------|
|                              |---codeable.txt
|                              |---Databse Credit.csv
|                              |---Final_Model.csv
|                              |---Preprocess.csv
|                              |---read_SouthGermanCredit.R
|                              |---SouthGermanCredit.asc
|
|logFiles----------------------|--application.log
|                              |--Database.log
|
|
|Static
|
|
|
templates----------------------|  
|                              |---index.html
|                              |---result.html
|                              |---German_Credit_Data.html
|venv
|
|app.py
|
|Credit_Data_RF.pkl
|
|Procfile
|
|requirements.txt
|
|runtime.txt
|
|Scaler_Credit_Data.pkl
|
|secure-coonect-energyefficiency.zip
~~~

## Installtion
The Code is written in Python 3.8.11. If you don't have Python installed you can find it [your link here](https://www.python.org/downloads/). If you are using a lower version of Python you can upgrade using the pip package, ensuring you have the latest version of pip. To install the required packages and libraries, run this command in the project directory after [cloning](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository) the repository.

~~~
Create a Virtual Env with conda create "Your Env name"
~~~
~~~
pip install -r requirements.txt
~~~
~~~
Run app.py file
~~~

## Technology Used
~~~
1. Python
2. Sklearn
3. Pandas
4. Numpy
5. Flask
6. HTML
7. CSS
8. Cassendra
9. AWS
10. Heroku
~~~

## Document
Below providing the link of all the document that are required for creating the project.

Link: [Document Link](https://drive.google.com/drive/folders/1XqY3PVwtXR0G0rJfvl1DI3XU7m_Zqu29?usp=sharing)
