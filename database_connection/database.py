# Database Name : South German Bank Data
# Keyspace Name : credit
# Table Name : credit_data

from cassandra.auth import PlainTextAuthProvider
from cassandra.cluster import Cluster
from application_logging.logger import logger
import pandas as pd
import csv

logger = logger('log_Files/Database.log')


class dataBaseOperation:

    def __init__(self):

        logger.info('INFO', 'Trying To Connect With The Database')
        self.keyspace = 'credit'

        self.table_name = 'credit_data'

        self.client_id = 'fDFMepzLgZIZqCkXgbEEeffc'

        self.client_secret = 'dqpA4MgjHlqiKrSBMh,OdE_cNhsy_6Zv.3hSFgA5C2AIkPtQxMQcep1NOovoYapYKgzBL1nj6xxD5c7JH6FYcbsEIX8EwFo8Un4W5BGtHqZi.j81q4HnCNLRp3oLtzS7'

        self.cloud_config = {
            'secure_connect_bundle': r"C:\Users\Lenovo\PycharmProjects\GermanBankCreditCard\secure-connect-south-german-bank-data.zip"}

        auth_provider = PlainTextAuthProvider(self.client_id, self.client_secret)
        cluster = Cluster(cloud=self.cloud_config, auth_provider=auth_provider)
        self.session = cluster.connect()
        logger.info('INFO', 'The Connection Is Created')

    def usekeyspace(self):

        try:

            logger.info('INFO', 'Using The Keyspace That We Created At Time of Database Creating')
            self.session.execute("USE {keyspace};".format(keyspace=self.keyspace))

            # print('Using The energy Keyspace')
            logger.info('INFO', 'The {keyspace} Is Selected'.format(keyspace=self.keyspace))

        except Exception as e:
            raise Exception(f"(useKeySpace) - Their Is Something Wrong About useKeySpace Method \n" + str(e))

    def createtable(self):

        try:

            logger.info('INFO', 'Table Is Creating Inside The Selected Keyspace')
            self.session.execute("USE {keyspace};".format(keyspace=self.keyspace))

            self.session.execute(
                "CREATE TABLE {table_name}(ID int PRIMARY KEY,status int, duration int,credit_history int,purpose int,"
                "amount int,savings int,employment_duration int,installment_rate int,personal_status_sex int,"
                "other_debtors int,present_residence int,property int, age int, other_installment_plans int,"
                "housing int, number_credits int, job int, people_liable int, telephone int,foreign_worker int,"
                "credit_risk int);".format(table_name=self.table_name))

            # print('Table Is Created Inside The Keyspace')

            logger.info('INFO', 'The Table Is Created Inside The {keyspace} With Name {table_name}'.format(
                        keyspace=self.keyspace, table_name=self.table_name))

        except Exception as e:
            raise Exception(f"(createTable) - Their Is Something Wrong About Creating Table Method \n" + str(e))

    def insertintotable(self):

        try:

            logger.info('INFO', 'Inserting The Data Into DATABASE')
            file = "SouthGermanCredit\SouthGermanCredit.csv"
            with open(file, mode='r') as f:
                next(f)

                reader = csv.reader(f, delimiter='\n')
                for i in reader:

                    data = ','.join([value for value in i])
                    self.session.execute("USE {keyspace};".format(keyspace=self.keyspace))

                    self.session.execute(
                        "INSERT INTO {table_name} (ID,status,duration,credit_history,purpose,amount,savings,"
                        "employment_duration,installment_rate,personal_status_sex,other_debtors,present_residence,"
                        "property,age,other_installment_plans,housing,number_credits,job,people_liable,telephone,"
                        "foreign_worker,credit_risk) VALUES ({data});".format(table_name=self.table_name, data=data))

                # print('Data Is Inseted')
                logger.info('INFO', 'All The Data Entered Into The {keyspace} Having Table Name {table_name}'.
                            format(keyspace=self.keyspace, table_name=self.table_name))

        except Exception as e:
            raise Exception(f"(insertintotable) - Their Is Something Wrong About Insert Into Data Method \n" + str(e))

    def getdatafromdatabase(self):

        try:

            logger.info('INFO', 'Trying To Get The Data From The DataBase')
            df = pd.DataFrame()

            query = "SELECT * FROM {keyspace}.{table_name};".format(keyspace=self.keyspace, table_name=self.table_name)
            for row in self.session.execute(query):

                df = df.append(pd.DataFrame([row]))

            logger.info('INFO', 'We Gathered The Data From DataBase {}'.format(df))
        except Exception as e:
            raise Exception(f"(getData) - Their Is Something Wrong About getData Method \n" + str(e))
