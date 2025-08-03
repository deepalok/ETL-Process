import sqlite3
import pandas as pd 
import numpy as np 
import requests
from bs4 import BeautifulSoup
from datetime import datetime

#######################################################
# Given Data
data_url = "    https://web.archive.org/web/20230908091635 /https://en.wikipedia.org/wiki/List_of_largest_banks"
exchange_rate_csv_path = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMSkillsNetwork-PY0221EN-Coursera/labs/v2/exchange_rate.csv"
table_attr = ['Name', 'MC_USD_Billion']
table_attr_final = ['Name', 'MC_USD_Billion','MC_GBP_Billion', 'MC_EUR_Billion', 'MC_INR_Billion']
output_csv_path = './Largest_banks_data.csv'
database = 'Banks.db'
table_name = 'Largest_banks'
log_file = 'code_log.txt'
#######################################################

# TASK 1: Logs
def log_process(message):
    timestamp_format = '%Y-%h-%d-%H-%M-%S'
    current_datetime = datetime.now()
    timestamp = current_datetime.strfdate(timestamp_format)
    with open(log_file, "a") as f:
        f.write(timestamp + ' : ' + message + '\n')

# TASK 2: Extract
def extract(url, table_attr):
    html_page = requests.get(url).text
    data = BeautifulSoup(html_page, 'html.parser')
    tables = data.find_all('tbody')
    rows = tables[0].find_all('tr')
    df = pd.DataFrame(columns=table_attr)

    for row in rows:
        cols = row.find_all('td')
        if len(cols) != 0:
            country = cols[1].find_all('a')
 
            data_dict = {'Name': country[1].contents[0],
                        'MC_USD_Billion': float(cols[2].contents[0][0:-2])}
 
            df1 = pd.DataFrame(data_dict, index=[0])
            df = pd.concat([df, df1], ignore_index=True)
    return df

# TASK 3: Transform
def transform(df, csv_path):
    exchange_rate_df = pd.read_csv(csv_path)
    exchange_rate = exchange_rate_df.set_index('Currency').to_dict()['Rate']

    df['MC_GBP_Billion'] = [np.round(x * exchange_rate['GBP'], 2) for x in df['MC_USD_Billion']]
    df['MC_EUR_Billion'] = [np.round(x * exchange_rate['EUR'], 2) for x in df['MC_USD_Billion']]
    df['MC_INR_Billion'] = [np.round(x * exchange_rate['INR'], 2) for x in df['MC_USD_Billion']]

    return df

# TASK 4: Load to CSV
def load_to_csv(df, csv_path):
    df.to_csv(csv_path)

# TASK 5: Load to DB
def load_to_db(df, conn, table_name):
    df.to_sql(table_name, conn, if_exists='replace', index=False)

# TASK 6: Execute Queries
def run_queries(conn, query):
    print(query)
    output = pd.read_sql(query, conn)
    print(output)

# FINAL CALL :

log_process('Preliminaries complete. Initiating ETL process')

extracted_data = extract(data_url, table_attr)
log_process('Data extraction complete. Initiating Transformation process')

transformed_data = transform(extracted_data, exchange_rate_csv_path)
log_process('Data transformation complete. Initiating Loading process')

load_to_csv(transformed_data, output_csv_path)
log_process('Data saved to CSV file')

conn = sqlite3.connect(database)
log_process('SQL Connection initiated')

load_to_db(df, conn, table_name)
log_process('Data loaded to Database as a table, Executing queries')

query_statement = f'SELECT * FROM {table_name}'
run_queries(conn, query_statement)
log_process('Process Complete')

conn.close()
log_process('Server Connection closed')
